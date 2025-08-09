import os
import vonage

# Load credentials from environment variables
VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VONAGE_VIRTUAL_NUMBER = os.getenv("VONAGE_VIRTUAL_NUMBER")
TEST_RECIPIENT = os.getenv("TEST_RECIPIENT")  # Add this to your GitHub Secrets

if not all([VONAGE_API_KEY, VONAGE_API_SECRET, VONAGE_VIRTUAL_NUMBER, TEST_RECIPIENT]):
    raise EnvironmentError("Vonage credentials and TEST_RECIPIENT must be set in environment variables.")

# Create Vonage client
client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
sms = vonage.Sms(client)

# Send a test message
response = sms.send_message({
    "from": VONAGE_VIRTUAL_NUMBER,
    "to": TEST_RECIPIENT,
    "text": "🦆 This is a test from your Duck Facts Bot!",
})

print("Vonage API response:", response)