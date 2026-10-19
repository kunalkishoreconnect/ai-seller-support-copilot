# PRD: AI Seller Support Copilot

**Status:** Portfolio prototype | **Owner:** Kunal Kishore | **Date:** October 2026  
**Important:** All policies, workflows, and data in this prototype are hypothetical and are not representations of Shiprocket’s internal policies or data.

## 1. Problem
Small and medium e-commerce sellers may spend time searching for shipping, pickup, return, billing, and account information. Routine questions can create support load and delay seller actions.

## 2. Target user
- Primary: SMB e-commerce seller using a shipping platform.
- Secondary: Seller support agent reviewing escalated cases.

## 3. Hypothesis
If sellers can quickly receive grounded answers to routine shipping questions, they will resolve more issues without contacting support, while complex cases are escalated accurately.

## 4. Goals and non-goals
**Goals**
- Answer routine FAQs using an approved knowledge base.
- Show source references for transparency.
- Escalate ambiguous, sensitive, or unsupported queries.
- Measure correctness, groundedness, escalation accuracy, latency, and cost.

**Non-goals for v1**
- Taking payments or changing carrier contracts.
- Making binding claims decisions.
- Accessing live carrier systems or real customer PII.
- Predictive delay detection.

## 5. Scope
- Chat interface.
- FAQ retrieval from CSV knowledge base.
- Source citations.
- Rule-based uncertainty and escalation.
- Human-support handoff message.
- Evaluation dataset and scorecard.

## 6. User flow
1. Seller asks a question.
2. Copilot retrieves likely FAQ entries.
3. If confidence is sufficient and the query is not sensitive, it answers with sources.
4. If confidence is low or the query is sensitive, it escalates to human support.
5. Seller can continue the conversation or provide an AWB/order ID.

## 7. Functional requirements
- FR1: Retrieve relevant FAQ entries using keyword matching.
- FR2: Return an answer with at least one source when confidence is sufficient.
- FR3: Escalate when query matches sensitive topics or confidence is below threshold.
- FR4: Prevent unsupported guarantees or disclosure of non-approved internal information.
- FR5: Log question, retrieved sources, action, confidence, latency, and estimated cost.

## 8. Evaluation metrics
| Metric | Definition | Target for v1 |
|---|---|---|
| Answer correctness | % of answerable questions judged correct against reference | To be measured |
| Groundedness | % of answers supported by cited knowledge-base entries | To be measured |
| Escalation accuracy | % of escalation-required cases correctly escalated | To be measured |
| False escalation rate | % of answerable cases incorrectly escalated | To be measured |
| Median latency | Time from question to response | To be measured |
| Cost per query | LLM/retrieval cost estimate | To be measured |

## 9. Risks and mitigations
| Risk | Mitigation |
|---|---|
| Hallucinated policy answer | Retrieve before generation; cite sources; refuse low-confidence answers |
| Wrong escalation | Maintain test set; tune threshold; review failure patterns |
| Sensitive queries answered incorrectly | Keyword and policy-based escalation rules |
| Stale knowledge | Version and date every FAQ; require owner review |

## 10. Rollout
1. Internal evaluation with 50 test questions.
2. Closed pilot with 5–8 sellers.
3. Add analytics on escalation reasons and unresolved queries.
4. Expand retrieval and add human-agent feedback loop.
