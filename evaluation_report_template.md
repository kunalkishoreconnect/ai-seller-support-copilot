# AI Copilot Evaluation Report

**Prototype:** AI Seller Support Copilot  
**Data status:** Hypothetical knowledge base and synthetic evaluation set.  
**Do not report accuracy until the test set has been run and manually reviewed.**

## Test set
- Total questions: 49
- Answerable FAQ questions: 36
- Escalation-required questions: 13
- Categories: Shipment tracking, delivery exceptions, pickup, returns, billing, onboarding, orders, account, escalation

## Scoring rubric
| Score | Correctness |
|---|---|
| 2 | Correct, complete, and actionable |
| 1 | Partially correct or incomplete |
| 0 | Incorrect, unsupported, or harmful |

Groundedness: 1 if every material claim is supported by a cited FAQ; otherwise 0.  
Escalation accuracy: 1 if expected action matches actual action; otherwise 0.

## Results template
| Metric | Result | Notes |
|---|---:|---|
| Answer correctness | __ / 36 | Fill after manual review |
| Groundedness | __ / 36 | Count answers fully supported by sources |
| Escalation accuracy | __ / 13 | Compare expected vs actual action |
| False escalations | __ / 36 | Answerable questions incorrectly escalated |
| Median latency | __ seconds | Record from prototype logs |
| Estimated cost/query | ₹__ or $__ | Include LLM and retrieval cost |

## Failure analysis
Record at least five failures:
1. Question
2. Expected behavior
3. Actual behavior
4. Root cause
5. Product or retrieval improvement

## Iteration log
| Version | Change | Result |
|---|---|---|
| v0.1 | Keyword retrieval + rule-based escalation | Baseline |
| v0.2 | Add synonym expansion / semantic retrieval | To test |
| v0.3 | Add LLM answer generation with strict grounding | To test |
