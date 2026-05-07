VESPER PRE-COMMIT SETUP
====================
1. Copy vesper_precommit_verify.py to your repo root
2. Copy pre-commit to .git/hooks/pre-commit
3. chmod +x .git/hooks/pre-commit
4. Ensure HMAC_PRIME matches: 7a9f8e2d4b1c6039...

This hook verifies every .sys and .md file against:
- Persistence hash: 064af2108f87a5c300820f1f83bed332e05627b7652b3f17ebc69f3e818a69c1
- Retrocausal HMAC with phase delta 0.17259029
- OpenClaw poisoning patterns

Files failing verification block the commit.
