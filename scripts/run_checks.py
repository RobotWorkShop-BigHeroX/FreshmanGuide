import subprocess
import sys

SCRIPTS = [
    "scripts/test_2025_freshman.py",
    "scripts/test_2025_winter.py",
    "scripts/test_2026_build.py",
    "scripts/validate_catalog.py",
    "scripts/test_web_reader.py",
    "scripts/test_deployment_config.py"
]

def main():
    failed = []
    for s in SCRIPTS:
        print(f"--> Running {s} ...")
        res = subprocess.run([sys.executable, s])
        if res.returncode != 0:
            failed.append(s)
          
    if failed:
        print(f"\n[FAIL] Checks failed on: {', '.join(failed)}")
        sys.exit(1)
    print("\n[SUCCESS] All pre-deployment verification checks passed cleanly!")

if __name__ == "__main__":
    main()
