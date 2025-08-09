import os
import requests
import random
from textwrap import dedent

# File paths (assign first!)
FACTS_FILE = "duck_facts.txt"
SENT_FILE = "sent_facts.txt"
RECIPIENTS_FILE = "recipients.txt"
WELCOMED_FILE = "welcomed_recipients.txt"

if not os.path.exists(FACTS_FILE):
    raise FileNotFoundError(f"Cannot find {FACTS_FILE} in the current directory.")

# API key from environment variable
TEXTBELT_KEY = '355950fa61b34a207c64acbc4c72c2eff2003ab8KfBbdn6JoAPRJ9dZnP473HTHV'

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

def send_sms(phone, message):
    response = requests.post('https://textbelt.com/text', {
        'phone': phone,
        'message': message,
        'key': TEXTBELT_KEY,
    })
    print(f"Sending to {phone}: {response.json()}")

# Send the fact to all recipients
for number in recipients:
    send_sms(number, fact_message)

# Save the sent fact
with open(SENT_FILE, "a") as f:
    f.write(fact + "\n")