import os
import requests
import random
import vonage
from textwrap import dedent
from dotenv import load_dotenv


# File paths (assign first!)
FACTS_FILE = "duck_facts.txt"
SENT_FILE = "sent_facts.txt"
RECIPIENTS_FILE = "recipients.txt"
WELCOMED_FILE = "welcomed_recipients.txt"

if not os.path.exists(FACTS_FILE):
    raise FileNotFoundError(f"Cannot find {FACTS_FILE} in the current directory.")

# Vonage credentials from env vars
VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VONAGE_VIRTUAL_NUMBER = os.getenv("VONAGE_VIRTUAL_NUMBER")

if not all([VONAGE_API_KEY, VONAGE_API_SECRET, VONAGE_VIRTUAL_NUMBER]):
    raise EnvironmentError("Vonage credentials (API key, secret, virtual number) must be set in environment variables.")

# Vonage client setup
client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
sms = vonage.Sms(client)


# Load facts
with open(FACTS_FILE, "r") as f:
    all_facts = [line.strip() for line in f if line.strip()]

# Load sent facts
sent_facts = []
if os.path.exists(SENT_FILE):
    with open(SENT_FILE, "r") as f:
        sent_facts = [line.strip() for line in f]

# Load recipients
with open(RECIPIENTS_FILE, "r") as f:
    recipients = [line.strip() for line in f if line.strip()]

# Load welcomed recipients
welcomed = []
if os.path.exists(WELCOMED_FILE):
    with open(WELCOMED_FILE, "r") as f:
        welcomed = [line.strip() for line in f]

# Choose a fact that hasn't been sent
unsent_facts = list(set(all_facts) - set(sent_facts))
if not unsent_facts:
    unsent_facts = all_facts
    sent_facts = []

fact = random.choice(unsent_facts)
fact_message = f"🦆 Prepare of a moment of pure duck-lightenment - your brain pond is about to get a fresh ripple because here comes your Duck Fact of the Day! Duck Fact: {fact}"

# Send SMS function
def send_sms(to_number, message):
    response = sms.send_message({
        "from": VONAGE_VIRTUAL_NUMBER,
        "to": to_number,
        "text": message,
    })
    print(f"Sending to {to_number}: {response}")

# Send messages
for number in recipients:
    send_sms(number, fact_message)

# Save the sent fact
with open(SENT_FILE, "a") as f:
    f.write(fact + "\n")