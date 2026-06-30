import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

BOT_TOKEN = "l8659387794:AAFo8ze6NWlxg8zWOnRTs-z5qmc5SaenAE4"  # Ye mat bhoolna
CHAT_ID = "7755010336"  # @userinfobot se mila tha

def get_railway_jobs():
    try:
        # Railway Apprentice latest
        url = "https://www.apprenticeshipindia.gov.in/apprenticeship/opportunity"
        jobs = "🚂 Railway Apprentice:\n1. RRC WR Apprentice 2026 - 2409 Posts\n   Last Date: 30-June-2026\n   Link: https://www.rrc-wr.com\n\n"
        return jobs
    except:
        return "🚂 Railway: Portal check kare - apprenticeshipindia.gov.in\n\n"

def get_private_jobs():
    # Ye manually update karna padega ya API use karni padegi
    jobs = "🏭 Private Jobs:\n1. Tata Motors Pune - ITI Electronic Mechanic\n   Salary: 18k-22k | Link: naukri.com/tata-motors\n2. Bajaj Auto Waluj - Fresher Hiring\n   Walk-in: 2-July-2026 | MIDC Aurangabad\n\n"
    return jobs

def send_message():
    date = datetime.now().strftime("%d-%m-%Y")
    
    message = f"""🔥 ITI Job Alert - {date} 🔥
📍 State: Maharashtra | Trade: Electronic Mechanic
━━━━━━━━━━━━━━━━━━━━

{get_railway_jobs()}
{get_private_jobs()}

📝 Documents: Aadhaar, ITI Marksheet, Photo
⏰ Roz subah 10 baje new update

👉 Join channel: @ITI_Electronic_Jobs"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

if __name__ == "__main__":
    send_message()
