import os
import smtplib
from email.message import EmailMessage
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

SMTP_EMAIL = os.environ.get("SMTP_EMAIL")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

@app.get("/")
def rood():
    return {"message": "Server is running"}

@app.post("/send")
def send_message(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    # Vytvoření emailu
    msg = EmailMessage()
    msg['Subject'] = f'Nová zpráva od {name}'
    msg['From'] = "mikulenkawebdeveloper@gmail.com"           
    msg['To'] = "mikulenkawebdeveloper@gmail.com"              
    msg.set_content(f"Od: {name} <{email}>\n\n{message}")

    # Připojení k SMTP serveru Gmailu
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SMTP_EMAIL, SMTP_PASSWORD)
        smtp.send_message(msg)

    return {"status": "sent"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://mikulenka-web-dev.vercel.app"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)