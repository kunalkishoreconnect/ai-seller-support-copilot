# Kunal Kishore — AI Seller Support Copilot

**Case 1 of an e-commerce seller-experience and logistics product portfolio.**  
This prototype explores how an AI assistant could help small and medium e-commerce sellers resolve routine shipping questions while escalating complex or sensitive cases to human support.

> **Disclaimer:** This is a learning portfolio project. The knowledge base, policies, workflows, and evaluation data are hypothetical and do not represent Shiprocket’s actual policies, data, or internal systems.

## Problem
E-commerce sellers may need quick answers about shipment tracking, pickups, returns, billing adjustments, and account setup. Searching policies or waiting for support can delay resolution and increase support load.

## Proposed solution
An AI Seller Support Copilot that:

- Answers routine questions from an approved FAQ knowledge base.
- Shows the source of each answer.
- Detects low-confidence or sensitive queries.
- Escalates legal, fraud, lost-shipment, billing-compliance, and delivery-dispute cases to human support.

## My role
- Defined the user problem, scope, and success metrics.
- Created a 46-entry hypothetical knowledge base.
- Designed retrieval, grounding, and escalation logic.
- Built a Streamlit chat prototype.
- Created a 49-question evaluation set covering normal, ambiguous, unsupported, and adversarial queries.
- Defined a measurement plan for correctness, groundedness, escalation accuracy, latency, and cost.

## Product decisions
| Decision | Rationale |
|---|---|
| Start with FAQ retrieval before advanced RAG | Establish a reliable, explainable baseline |
| Show source citations | Increase trust and make answers auditable |
| Use conservative escalation | Avoid incorrect answers on financial, legal, fraud, and lost-package issues |
| Track escalation accuracy | Prevent the assistant from becoming a dead end for sellers |
| Label all data as hypothetical | Maintain transparency and avoid implying access to real platform data |

## Evaluation plan
The prototype will be evaluated on 49 test questions:

- 36 answerable FAQ questions
- 13 escalation-required questions
- Unsupported, ambiguous, and prompt-injection scenarios

Metrics include answer correctness, groundedness, escalation accuracy, false-escalation rate, median latency, and estimated cost per query.

## Artifacts
- Streamlit chat prototype
- `knowledge_base.csv`
- `evaluation_questions.csv`
- `PRD_AI_Seller_Support_Copilot.md`
- `evaluation_report_template.md`

## Next steps
- Add semantic retrieval and LLM answer generation constrained to retrieved sources.
- Add helpfulness feedback and escalation-reason analytics.
- Run a closed pilot with 5–8 sellers.
