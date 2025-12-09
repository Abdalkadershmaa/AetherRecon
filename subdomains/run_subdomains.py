#!/usr/bin/env python3
import subprocess
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python3 run_subdomains.py example.com")
    sys.exit(1)

DOMAIN = sys.argv[1]

FILES = {
    "subfinder": "subfinder.txt",
    "assetfinder": "assetfinder.txt",
    "amass": "amass.txt",
    "sublist3r": "sublist3r.txt",
}

def run(cmd, name):
    print(f"\n[+] Running {name}")
    print("    " + " ".join(cmd))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"[!] {name} failed")
        sys.exit(1)
    print(f"[✓] {name} finished")

# -------- SUBFINDER --------
run([
    "subfinder",
    "-d", DOMAIN,
    "-all",
    "-recursive",
    "-silent",
    "-o", FILES["subfinder"]
], "subfinder")

# -------- ASSETFINDER --------
run([
    "bash",
    "-lc",
    f"echo {DOMAIN} | assetfinder --subs-only > {FILES['assetfinder']}"
], "assetfinder")

# -------- AMASS (PASSIVE) --------
run([
    "amass",
    "enum",
    "-passive",
    "-d", DOMAIN,
    "-o", FILES["amass"]
], "amass")

# -------- SUBLIST3R --------
run([
    "sublist3r",
    "-d", DOMAIN,
    "-o", FILES["sublist3r"]
], "sublist3r")

# -------- MERGE ONLY --------
print("\n[+] Merging all outputs → all_raw.txt")

with open("all_raw.txt", "w") as out:
    for f in FILES.values():
        if os.path.exists(f):
            with open(f, "r", errors="ignore") as src:
                for line in src:
                    line = line.strip()
                    if line:
                        out.write(line + "\n")

print("\n[✓] DONE")
print("Files created:")
for k, v in FILES.items():
    print(f"  - {v}")
print("  - all_raw.txt")
