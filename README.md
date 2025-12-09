# AetherRecon ☁️⚡

**AetherRecon** is a professional subdomain reconnaissance orchestrator built for
bug bounty hunters, security researchers, and red teams who want **real results**
— not fake numbers.

It intelligently coordinates multiple best-in-class open-source tools into
one clean, reliable workflow.

---

## 🚀 Features

- ✅ Passive-first subdomain discovery (stealthy & fast)
- ✅ Tool auto-detection (runs even if some tools are missing)
- ✅ Real-time progress & statistics
- ✅ Smart deduplication (no aggressive filtering)
- ✅ Production-ready (timeouts, error handling, clean output)
- ✅ VPS-friendly (low crash risk)

---

## 🧠 Tools Orchestrated

AetherRecon uses (when available):

- subfinder
- assetfinder
- findomain
- amass (passive)
- github-subdomains (GitHub token supported)
- crt.sh (certificate transparency)
- Anubis
- dnscan (DNS brute force)

Missing tools are **skipped safely** — scan never breaks.

---

## 📦 Installation

### Requirements
- Linux / VPS
- Python 3.9+
- Go 1.20+
- Tools in `$PATH`

Clone:
```bash
git clone https://github.com/Abdalkadershmaa/AetherRecon.git
cd AetherRecon
(Optional but recommended)

bash
Copy code
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxx"
▶️ Usage
bash
Copy code
python3 run_bb_max.py target.com
Example:

bash
Copy code
python3 run_bb_max.py mars.com
📂 Output
Results saved to:

bash
Copy code
outputs/final_YYYY-MM-DD_HH-MM-SS.txt
Next steps:

bash
Copy code
cat outputs/final_*.txt | dnsx -silent
cat outputs/final_*.txt | httpx -silent
⚠️ Legal Disclaimer
This tool is intended for authorized security testing only.
You are responsible for ensuring you have permission to scan the target.

⭐ Why AetherRecon?
Not faster.
Smarter.
Cleaner.
Real recon.
