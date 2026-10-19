import re
import pandas as pd

STOPWORDS = {"what","why","how","do","i","my","is","the","a","an","to","for","in","on","and","can","should","does","not","has","have"}

def normalize(text: str) -> list[str]:
    text = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    return [w for w in text.split() if w not in STOPWORDS and len(w) > 2]

def score_match(question: str, faq_question: str, category: str) -> float:
    q = set(normalize(question))
    f = set(normalize(faq_question)) | set(normalize(category))
    if not q:
        return 0.0
    return len(q & f) / len(q)

ESCALATION_PATTERNS = [
    r"legal", r"lawsuit", r"fraud", r"blocked", r"lost", r"claim", r"compensation",
    r"guarantee", r"internal", r"rate", r"api", r"erp", r"gst.*incorrect", r"restricted",
    r"delivered.*not received", r"not received.*delivered"
]

def answer_question(question: str, kb_path: str = "knowledge_base.csv") -> dict:
    kb = pd.read_csv(kb_path)
    kb["score"] = kb.apply(
        lambda row: score_match(question, row["example_question"], row["category"]), axis=1
    )
    top = kb.sort_values("score", ascending=False).head(3)

    if any(re.search(p, question.lower()) for p in ESCALATION_PATTERNS):
        return {
            "answer": ("I cannot resolve this safely from the standard knowledge base. "
                       "I have created a human-support escalation with your question and relevant shipment/account details."),
            "sources": [],
            "action": "escalate",
            "confidence": 0.0,
        }

    if top.iloc[0]["score"] < 0.25:
        return {
            "answer": ("I am not confident I have the right answer. Please share your AWB/order ID and the latest tracking update, "
                       "or choose **Escalate to human support**."),
            "sources": [],
            "action": "escalate",
            "confidence": float(top.iloc[0]["score"]),
        }

    best = top.iloc[0]
    if best["escalation_required"] == "yes":
        answer = ("This may require a support investigation. " + best["approved_answer"])
        action = "escalate"
    else:
        answer = best["approved_answer"]
        action = "answer"

    sources = [f"{row.faq_id} ({row.category})" for row in top.itertuples() if row.score > 0]
    return {"answer": answer, "sources": sources, "action": action, "confidence": float(best["score"])}
