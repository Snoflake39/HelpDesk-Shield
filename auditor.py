#!/usr/bin/env python3
import sys
from datetime import datetime

def audit_login_attempts(failed_attempts):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S']}] Running IT Security & Lockout Audit...")
    threshold = 5
    for user, attempts in failed_attempts.items():
        if attempts >= threshold:
            print(f"[!] ALERT: User '{user}' has {attempts} failed attempts. Flagged for potential lockout/brute-force check.")
        else:
            print(f"[+] User '{user}' is within safe threshold ({attempts} failures).")

if __name__ == "__main__":
    sample_logs = {
        "jsmith": 2,
        "aparker": 6,  # Exceeds threshold
        "mdavis": 1,
        "bwayne": 7    # Exceeds threshold
    }
    audit_login_attempts(sample_logs)
