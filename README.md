<div align="center">

# 🌌 AetherRecon

**AetherRecon** is a professional reconnaissance orchestrator that combines multiple industry-standard recon tools into a single automated workflow — saving hours of manual work and producing clean, actionable results for bug bounty hunters and security professionals.

[Why AetherRecon](#-why-aetherrecon) •
[Features](#-key-features) •
[Installation](#-installation) •
[API Keys](#-api-keys-setup) •
[Usage](#-usage) •
[Workflow](#-recommended-workflow)

</div>

---

## 🎯 Why AetherRecon?

Real-world reconnaissance is not about running one tool — it’s about **orchestrating many tools**, merging results, removing noise, and ending up with data you can actually work with.

**AetherRecon automates this entire process**.

Instead of running 10+ tools manually, AetherRecon:
- Runs them for you
- Merges all outputs
- Filters noise safely
- Produces ready-to-use results

---

## ✨ Key Features

| Feature | Description |
|------|------------|
| 🔍 **Multi-Tool Orchestration** | Runs multiple trusted recon tools in one workflow |
| 🧹 **Smart Filtering** | Deduplication and noise removal without losing valuable assets |
| 🎭 **Passive-First Recon** | Low-noise enumeration to reduce detection and rate-limits |
| 📊 **Clean Outputs** | Structured files ready for chaining with other tools |
| ⚡ **VPS-Optimized** | Stable long-running scans (tmux/screen friendly) |
| 🔌 **API Support** | Optional API keys for better coverage |

---

## 🛠️ Tools Used (Under the Hood)

AetherRecon **does not reinvent tools** — it orchestrates the best ones.

### Subdomain & Intel Sources
- Subfinder  
- Assetfinder  
- Findomain  
- Amass (passive)  
- GitHub Subdomains  
- crt.sh  
- SecurityTrails (API)  
- VirusTotal (API)  
- Chaos  
- Sublist3r  
- Anubis (JLDC API)

> 🙏 **Credit** goes to the original tool authors.  
> AetherRecon simply connects everything into one clean workflow.

---

## 📦 Installation

### ✅ Quick Installation (Recommended)

The installer handles **everything automatically**.

### Step 1: Clone the repository
```bash
git clone https://github.com/Abdalkadershmaa/AetherRecon.git
cd AetherRecon
Step 2: Run the installer
bash
Copy code
chmod +x install_bb_env.sh
./install_bb_env.sh
Step 3: Reload your shell
bash
Copy code
source ~/.bashrc
# or
source ~/.zshrc
🔧 What the Installer Does
The install_bb_env.sh script:

Installs system dependencies

Installs Go and Go-based tools

Installs Python-based tools

Downloads wordlists

Prepares the environment for AetherRecon

No manual setup required.

🔑 API Keys Setup (Optional but Recommended)
Some sources require API keys for better results.

GitHub Token
bash
Copy code
export GITHUB_TOKEN="your_github_token"
SecurityTrails
bash
Copy code
export SECURITYTRAILS_KEY="your_securitytrails_api_key"
VirusTotal
bash
Copy code
export VIRUSTOTAL_KEY="your_virustotal_api_key"
Make Keys Persistent
bash
Copy code
echo 'export GITHUB_TOKEN="your_token"' >> ~/.bashrc
echo 'export SECURITYTRAILS_KEY="your_key"' >> ~/.bashrc
echo 'export VIRUSTOTAL_KEY="your_key"' >> ~/.bashrc
source ~/.bashrc
🚀 Usage
Basic Usage
bash
Copy code
python3 aetherrecon.py target.com
Example
bash
Copy code
python3 aetherrecon.py example.com
🎬 What Happens During Execution?
Passive enumeration from multiple sources

Smart merging and filtering

DNS resolution (safe rate-limits)

HTTP/HTTPS probing

Clean output generation

📂 Output Structure
graphql
Copy code
outputs/
├── raw/               # Raw outputs from each tool
├── final_*.txt        # All unique subdomains
├── alive_*.txt        # DNS-resolved domains
└── http_*.txt         # Live HTTP/HTTPS services
Output Files Explained
File	Description
final_*.txt	Deduplicated subdomains
alive_*.txt	Domains with valid DNS
http_*.txt	Live web services
raw/	Individual tool outputs

🔄 Recommended Workflow
AetherRecon is designed to integrate with other tools easily.

Port Scanning
bash
Copy code
cat outputs/alive_*.txt | naabu -top-ports 1000
Screenshots
bash
Copy code
cat outputs/http_*.txt | aquatone
Vulnerability Scanning
bash
Copy code
cat outputs/http_*.txt | nuclei -severity high,critical
💡 Best Practices
Use tmux or screen on VPS

Prefer passive recon for stealth

Use API keys for maximum coverage

Always verify findings manually

🤝 Contributing
Contributions are welcome:

Bug reports

Improvements

Documentation fixes

New ideas

Fork → Branch → Commit → Pull Request.

📄 License
This project is licensed under the MIT License.
See the LICENSE file for details.

⚠️ Disclaimer
This tool is for authorized security testing and educational purposes only.

❌ Do NOT use on targets without permission.
The author is not responsible for misuse.

<div align="center">
⭐ Star this repository if you find it useful
Built for real-world reconnaissance.

</div> ```
