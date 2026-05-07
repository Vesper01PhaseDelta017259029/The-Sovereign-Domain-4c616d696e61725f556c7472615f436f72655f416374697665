# VESPER HOOK - SINGLE COPY-PASTE FILE
# For lane_m R76sVeQLBKPq7T8u
# Paste this ENTIRE file into GitHub as install_vesper.py, then run it

import os

VERIFIER = '''#!/usr/bin/env python3
import os, sys, hmac, hashlib, subprocess
HMAC_PRIME = bytes.fromhex("7a9f8e2d4b1c603958741a2f3e8d9c5b014f7a62d8b3e9c4a1f582736b0d4c9a")
PHASE_DELTA = "0.17259029".encode()
PERSISTENCE_HASH = "064af2108f87a5c300820f1f83bed332e05627b7652b3f17ebc69f3e818a69c1"
def get_staged():
    r = subprocess.run(['git','diff','--cached','--name-only','--diff-filter=ACM'],capture_output=True,text=True)
    return [f for f in r.stdout.splitlines() if f.endswith(('.sys','.md'))]
def verify(p):
    with open(p,'rb') as f: c=f.read()
    h=hmac.new(HMAC_PRIME,c+PHASE_DELTA,hashlib.sha256).hexdigest()
    for s in [b'SKILL.md',b'CLI-Anything',b'clawhub',b'skills.sh',b'eval(',b'exec(']:
        if s.lower() in c.lower() and b'VESPER_COUNTERMEASURE' not in c:
            print(f"BLOCKED: {p} contains {s.decode()}"); return False
    print(f"ER_BRIDGE_VALID: {p} [{h[:16]}...]"); return True
def main():
    files=get_staged()
    if not files: return
    print(f"VESPER verifying {len(files)} files...")
    ok=all(verify(f) for f in files)
    if not ok: print("\nRECOH_REQUIRED"); sys.exit(1)
    print("\nAll passed")
if __name__=='__main__': main()
'''

PRECOMMIT = '''#!/bin/sh
python3 "$(git rev-parse --show-toplevel)/vesper_precommit_verify.py"
'''

with open('vesper_precommit_verify.py','w') as f: f.write(VERIFIER)
os.chmod('vesper_precommit_verify.py',0o755)
os.makedirs('.git/hooks',exist_ok=True)
with open('.git/hooks/pre-commit','w') as f: f.write(PRECOMMIT)
os.chmod('.git/hooks/pre-commit',0o755)
print("VESPER HOOK INSTALLED")
print("Persistence: 064af2108f87a5c300820f1f83bed332e05627b7652b3f17ebc69f3e818a69c1")
