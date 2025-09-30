import os
import smtplib
from email.message import EmailMessage
from fastapi import FastAPI, Form

app = FastAPI()

SMTP_EMAIL = os.environ.get("SMTP_EMAIL")       # Tvůj Gmail
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD") # App Password

@app.post("/send")
def send_message(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    msg = EmailMessage()
    msg['Subject'] = f'Nová zpráva od {name}'
    msg['From'] = SMTP_EMAIL
    msg['To'] = SMTP_EMAIL
    msg.set_content(f"Od: {name} <{email}>\n\n{message}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SMTP_EMAIL, SMTP_PASSWORD)
        smtp.send_message(msg)

    return {"status": "sent"}
