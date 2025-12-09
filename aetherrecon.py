#!/usr/bin/env python3
"""
BB Subdomain Orchestrator — PRO
REAL MAXIMUM MODE (No fake flags, no over-filtering)
"""

import os
import sys
import subprocess
import shutil
import time
from datetime import datetime

# =========================
# BASIC CHECK
# =========================
if len(sys.argv) != 2:
    print("Usage: python3 run_bb_pro.py target.com")
    sys.exit(1)

TARGET = sys.argv[1]
BASE = os.getcwd()
OUT = f"{BASE}/outputs"
TOOLS = f"{BASE}/tools"
WORDLIST = f"{BASE}/wordlists/dns.txt"

os.makedirs(OUT, exist_ok=True)

TS = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
FINAL_FILE = f"{OUT}/final_{TS}.txt"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

# =========================
# HELPERS
# =========================
def has_tool(cmd):
    return shutil.which(cmd) is not None

def run(cmd, outfile):
    start = time.time()
    try:
        with open(outfile, "w") as f:
            subprocess.run(
                cmd,
                shell=True,
                stdout=f,
                stderr=subprocess.DEVNULL,
                timeout=600
            )
        count = sum(1 for _ in open(outfile, "r", errors="ignore"))
        print(f"    ✓ {count} domains ({time.time() - start:.1f}s)")
        return outfile
    except subprocess.TimeoutExpired:
        print(f"    ⏱ timeout")
        open(outfile, "w").close()
        return outfile
    except Exception:
        open(outfile, "w").close()
        print(f"    ⚠ error")
        return outfile

def banner():
    print(f"""
========================================
 BB Subdomain Orchestrator — PRO
 Target : {TARGET}
 Started: {datetime.now().strftime("%H:%M:%S")}
========================================
""")

# =========================
# START
# =========================
banner()

results = []

# -------------------------
# subfinder
# -------------------------
print("[1/9] subfinder")
if has_tool("subfinder"):
    results.append(
        run(
            f"subfinder -silent -d {TARGET}",
            f"{OUT}/subfinder.txt"
        )
    )
else:
    print("    ✗ not installed")

# -------------------------
# assetfinder
# -------------------------
print("[2/9] assetfinder")
if has_tool("assetfinder"):
    results.append(
        run(
            f"assetfinder --subs-only {TARGET}",
            f"{OUT}/assetfinder.txt"
        )
    )

# -------------------------
# findomain
# -------------------------
print("[3/9] findomain")
if has_tool("findomain"):
    results.append(
        run(
            f"findomain -t {TARGET} -q",
            f"{OUT}/findomain.txt"
        )
    )

# -------------------------
# amass (PASSIVE ONLY)
# -------------------------
print("[4/9] amass (passive)")
if has_tool("amass"):
    results.append(
        run(
            f"amass enum -passive -d {TARGET}",
            f"{OUT}/amass.txt"
        )
    )

# -------------------------
# github-subdomains
# -------------------------
print("[5/9] github-subdomains")
if has_tool("github-subdomains"):
    token_arg = f"-t {GITHUB_TOKEN}" if GITHUB_TOKEN else ""
    results.append(
        run(
            f"github-subdomains -d {TARGET} {token_arg}",
            f"{OUT}/github.txt"
        )
    )
else:
    print("    ⚠ tool missing")

# -------------------------
# crt.sh
# -------------------------
print("[6/9] crt.sh")
results.append(
    run(
        f"""curl -s "https://crt.sh/?q=%25.{TARGET}&output=json" | \
           jq -r '.[].name_value' | tr '\\n' '\\n'""",
        f"{OUT}/crtsh.txt"
    )
)

# -------------------------
# Anubis
# -------------------------
print("[7/9] Anubis")
if os.path.exists(f"{TOOLS}/Anubis/anubis"):
    results.append(
        run(
            f"python3 {TOOLS}/Anubis/anubis -t {TARGET}",
            f"{OUT}/anubis.txt"
        )
    )
else:
    print("    ⚠ tool missing")

# -------------------------
# dnscan (controlled brute)
# -------------------------
print("[8/9] dnscan")
if os.path.exists(f"{TOOLS}/dnscan/dnscan.py") and os.path.exists(WORDLIST):
    results.append(
        run(
            f"python3 {TOOLS}/dnscan/dnscan.py -d {TARGET} "
            f"-w {WORDLIST} -t 20 -q",
            f"{OUT}/dnscan.txt"
        )
    )
else:
    print("    ⚠ skipped")

# -------------------------
# DEDUP (LIGHT FILTER ONLY)
# -------------------------
print("[9/9] Deduplicating")

cat_cmd = " ".join(results)
subprocess.run(
    f"cat {cat_cmd} 2>/dev/null | "
    f"tr '[:upper:]' '[:lower:]' | "
    f"sed 's/\\s//g' | "
    f"grep -E '^[a-z0-9.-]+\\.[a-z]{{2,}}$' | "
    f"sort -u > {FINAL_FILE}",
    shell=True
)

total = sum(1 for _ in open(FINAL_FILE))

# =========================
# DONE
# =========================
print(f"""
========================================
 ✅ Completed
 Total subdomains : {total}
 Output           : {FINAL_FILE}
========================================

Next steps:
  DNS check  : cat {FINAL_FILE} | dnsx -silent
  HTTP probe: cat {FINAL_FILE} | httpx -silent
""")
