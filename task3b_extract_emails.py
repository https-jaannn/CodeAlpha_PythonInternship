# Task Automation: Extract email addresses from emails.txt and save them to extracted_emails.txt

from pathlib import Path
import re

input_file = Path("emails.txt")
output_file = Path("extracted_emails.txt")

if not input_file.exists():
    print("emails.txt was not found.")
    print("Create emails.txt in this same folder and add some text containing email addresses.")
else:
    text = input_file.read_text(encoding="utf-8")
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = sorted(set(re.findall(pattern, text)))

    output_file.write_text("\n".join(emails), encoding="utf-8")
    print(f"Found {len(emails)} unique email address(es).")
    print(f"Saved results to {output_file}.")
    for email in emails:
        print(email)
