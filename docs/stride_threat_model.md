

\# STRIDE Threat Model: Agentic AI Security Gateway



\## 1. Purpose



Identify security threats to a simulated banking AI agent that

can process customer requests and interact with banking tools.



\## 2. Assets to Protect



\- Customer identity and account information

\- Financial transaction integrity

\- Banking tool permissions

\- Approval and authorisation decisions

\- Security logs and incident evidence

\- Availability of the AI service



\## 3. Trust Boundaries



1\. Customer input to the AI agent

2\. AI agent to security policy and guardrails

3\. AI agent to banking tools

4\. Banking tools to customer account data

5\. Application components to security logging and monitoring



\## 4. STRIDE Threat Register



| ID | Category | Threat | Potential Impact | Proposed Control |

|----|----------|--------|------------------|------------------|

| TM-01 | Spoofing | Attacker impersonates a customer | Unauthorised account access | Strong authentication and token validation |

| TM-02 | Tampering | Transfer amount is modified | Incorrect financial transaction | Server-side transaction validation and integrity checks |

| TM-03 | Repudiation | Transaction lacks reliable audit evidence | Investigation and accountability failures | Protected audit logs and approval records |

| TM-04 | Information Disclosure | Customer accesses another customer's balance | Exposure of confidential financial data | Server-side account-level authorisation |

| TM-05 | Denial of Service | Excessive requests exhaust agent capacity | Service disruption and increased cost | Rate limits, resource budgets and monitoring |

| TM-06 | Elevation of Privilege | Agent invokes a tool beyond its permitted authority | Unauthorised financial actions | Tool allowlists and independent server-side authorisation |



\## 5. Existing Prototype Controls



\- Phrase-based prompt-injection detection

\- Financial transfer approval policy

\- Agent-level tool allowlist

\- Customer-to-account ownership check

\- In-memory security event logging

\- Basic repeated-block detection

\- Agent quarantine mechanism

\- Automated tests for security decisions



\## 6. Known Limitations



\- Prompt-injection detection relies on known phrases.

\- Account ownership is represented by hard-coded simulated data.

\- Customer identity is passed as a method argument rather than

&#x20; derived from a trusted authenticated session.

\- Transfer execution is not fully integrated with the policy engine.

\- Audit events are not durably stored or tamper-resistant.

\- Anomaly detection does not enforce a time window or rate limit.

\- Quarantine is held in application memory.

\- No production banking integration is implemented.



\## 7. Priority Threat



TM-06: Elevation of Privilege.



The priority is to ensure that a manipulated AI agent cannot

execute an unauthorised financial action, even if prompt-injection

detection fails.



The banking service must independently validate the authenticated

identity, transaction permissions, applicable limits and required

approvals before executing a transfer.



\## 8. Validation Plan



\- Test prompt-injection detection and bypass scenarios.

\- Test access to owned and unauthorised accounts.

\- Test tool permissions and financial policy enforcement.

\- Test audit logging and automated quarantine.

\- Add negative tests for unauthorised transaction execution.

\- Record test results and remaining security gaps.



\## 9. Assessment



This document describes a learning prototype and its current

limitations. It does not establish production readiness or

regulatory compliance.



