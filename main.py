

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import smtplib
import os
from email.message import EmailMessage

app = FastAPI()

# --- Static a Templates ---
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- Domovská stránka ---
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- Health check ---
@app.get("/health")
async def health():
    return {"status": "ok"}

# --- Endpoint pro odeslání mailu přes Gmail SMTP ---
@app.post("/send")
async def send_message(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    print(f"📩 Přijata zpráva od: {name} ({email})")
    
    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    if not smtp_email or not smtp_password:
        print("❌ CHYBA: SMTP_EMAIL nebo SMTP_PASSWORD nejsou nastavené!")
        return JSONResponse(
            {"status": "error", "message": "Server není správně nakonfigurován."},
            status_code=500
        )
    
    try:
        msg = EmailMessage()
        msg['Subject'] = f'Nová zpráva z portfolia od {name}'
        msg['From'] = smtp_email
        msg['To'] = smtp_email  # Posílá sám sobě
        msg['Reply-To'] = email  # Aby ses mohl odpovědět přímo odesílateli
        msg.set_content(f"Od: {name}\nEmail: {email}\n\nZpráva:\n{message}")

        print(f"📧 Odesílám email přes Gmail SMTP ({smtp_email})...")
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(smtp_email, smtp_password)
            smtp.send_message(msg)
        
        print("✅ Email úspěšně odeslán!")
        return JSONResponse({"status": "ok", "message": "Email odeslán."})
    
    except smtplib.SMTPAuthenticationError:
        print("❌ CHYBA: Neplatné přihlašovací údaje! Zkontroluj App Password.")
        return JSONResponse(
            {"status": "error", "message": "Chyba autentizace SMTP."},
            status_code=500
        )
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return JSONResponse(
            {"status": "error", "message": str(e)},
            status_code=500
        )