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
