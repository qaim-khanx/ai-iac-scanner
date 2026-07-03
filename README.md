<img width="1918" height="1064" alt="Screenshot 2026-07-03 170017" src="https://github.com/user-attachments/assets/5594fae4-4b50-4ea1-94f6-9e3de902f124" />
<img width="1918" height="1064" alt="Screenshot 2026-07-03 170017" src="https://github.com/user-attachments/assets/f6f5ef21-d02b-483c-9c9e-10d21f207ede" />
# AI-Powered Terraform Security Gatekeeper

## 🚀 Overview
**AI-Powered Terraform Security Gatekeeper** is an automated, policy-driven DevSecOps solution designed to enforce infrastructure security at the CI/CD level. By integrating Generative AI as a semantic security analyst, this engine evaluates Infrastructure-as-Code (IaC) against security best practices, preventing vulnerable resource provisioning before it reaches the cloud.

---

## 💡 The Problem
In modern DevOps workflows, infrastructure misconfigurations—such as publicly exposed S3 buckets, unencrypted databases, or over-privileged IAM roles—pose a critical security risk. Relying on manual peer reviews is slow, and traditional static analysis tools (SAST) often suffer from high false-positive rates and lack the contextual reasoning required to assess complex infrastructure dependencies.

## 🛠️ The Solution
This project acts as an intelligent **"Shift-Left" Security Gate**. It intercepts `terraform plan` operations by injecting an AI-driven audit stage into the Jenkins pipeline. Using the **Google Gemini 2.0 Flash** model, it interprets Terraform configuration intent and provides actionable, human-readable feedback on potential security breaches.

---

## 🏗️ Architecture
The gatekeeper follows a modular, container-ready architecture designed for scalability:

1.  **Orchestration:** Jenkins CI pipeline triggers on git-push events.
2.  **Environment Setup:** Dynamic provisioning of a Python virtual environment (`venv`) to ensure deterministic dependency resolution.
3.  **Security Analysis Engine:** An asynchronous Python service that acts as a wrapper around the Google GenAI SDK.
4.  **Resilience Layer:** Implements **Exponential Backoff** to handle transient API `503` (Service Unavailable) and `429` (Rate Limit) errors.
5.  **Governance Layer:** Non-zero exit code triggers an immediate pipeline halt, ensuring that only "PASS" configurations proceed to the deployment phase.



---

## 📊 Key Features
* **Semantic Security Audit:** Goes beyond regex-based scanning; uses Large Language Model (LLM) reasoning to evaluate infrastructure security intent.
* **Zero-Hardcoding Policy:** Utilizes Jenkins Secret Credentials and Environment Variable injection to maintain a secure posture for API keys.
* **Pipeline Resilience:** Features an automated retry mechanism that guarantees deployment stability even during high API traffic spikes.
* **Infrastructure-as-Code Compliance:** Enforces "Policy-as-Code" standards on all `*.tf` files.

---

## 🚀 Quick Start
1. **Infrastructure Prerequisites:**
   - Jenkins installed on a Linux/Ubuntu environment.
   - Terraform CLI installed.
   - Python 3.12+ and `venv` enabled.

2. **Configuration:**
   - Navigate to **Manage Jenkins > Credentials**.
   - Add a "Secret Text" credential with the ID `GOOGLE_API_KEY`.

3. **Pipeline Execution:**
   - Point your Jenkins Pipeline to this repository.
   - The pipeline will automatically execute `Setup Environment`, `Security Scan`, and `Terraform Plan` stages.

---

## 📈 Pipeline Demonstration
| Build Stage | Security Result | Pipeline Status |
| :--- | :--- | :--- |
| **Insecure Main.tf** | `FAIL` | Blocked ❌ |
| **Secure Main.tf** | `PASS` | Proceeding ✅ |

![Security Scan Failed]("<img width="1919" height="1142" alt="Screenshot 2026-06-30 154200" src="https://github.com/user-attachments/assets/2c704971-d776-401f-9363-c2155d4986a2" />
<img width="1918" height="1064" alt="Screenshot 2026-07-03 170017" src="https://github.com/user-attachments/assets/f973ce45-4723-4092-ba1d-62bfcb9c6644" />
")

---

## 🛡️ Security & Governance
- **Shift-Left Security:** Catch vulnerabilities in the build phase, saving costs and preventing production downtime.
- **Auditability:** Every scan result is logged in the Jenkins console, providing a clear audit trail of why a configuration was approved or rejected.

---

## 🤝 Contributors
* **[Qaim Raza Khan](https://github.com/qaim-khanx)** - Lead Architecture & Implementation

