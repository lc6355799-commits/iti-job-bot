import requests
from datetime import datetime
import pytz

# APNA TOKEN AUR CHAT_ID YAHAN DAALNA HAI
BOT_TOKEN = "8659387794:AAFxUOzlsYGsrB8EjZXQW0TY3CFtqXIs4_Q"
CHAT_ID = "7755010336" 
TRADE = "Electronic Mechanic"
STATE = "Maharashtra"

def send_msg(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, data=data)

# Maharashtra ka time IST hi hai
ist = pytz.timezone('Asia/Kolkata')
today = datetime.now(ist).strftime("%d-%m-%Y")
time_now = datetime.now(ist).strftime("%I:%M %p")

msg = f"🔥 *ITI Job Update - {today}* 🔥\n"
msg += f"⏰ *Time:* {time_now} | *State:* {STATE}\n"
msg += f"📍 *Trade:* {TRADE}\n"
msg += "━━━━━━━━━━━━━━━━━━━━\n\n"

msg += "*🏛️ GOVT JOB / APPRENTICE:*\n"
msg += "1. Apprenticeship India Portal - Nayi vacancy check kare\n"
msg += "2. Railway / OFB / BHEL - ITI quota posts\n\n"

msg += "*🏭 PRIVATE JOB:*\n"
msg += "1. Bajaj Auto, Tata Motors, Mahindra - Fresher hiring\n"
msg += "2. Local MIDC Companies - Walk-in interview\n\n"

msg += "*🎓 APPRENTICE UPDATE:*\n"
msg += "1. Roz naye portal pe check kare\n"
msg += "2. Documents ready rakhe: Aadhaar, ITI Marksheet\n\n"
msg += "━━━━━━━━━━━━━━━━━━━━\n"
msg += "🔗 *Govt Apply:* apprenticeshipindia.gov.in\n"
msg += "🔗 *Private Jobs:* naukri.com, apna.co\n"
msg += "_Roz subah 10:00 baje auto update_ ✅"

send_msg(msg)
print("Message sent to Telegram")
