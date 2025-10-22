from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import smtplib, os
from email.message import EmailMessage

app = FastAPI()

# --- CORS nastavení ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://michalmikulenka.vercel.app",  # tvoje FE doména
        "http://localhost:5173"  # pro lokální vývoj
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Static a Templates ---
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- Domovská stránka ---
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- Endpoint pro odeslání mailu ---
@app.post("/send")
async def send_message(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    try:
        msg = EmailMessage()
        msg['Subject'] = f'Nová zpráva od {name}'
        msg['From'] = os.getenv("SMTP_EMAIL")
        msg['To'] = os.getenv("SMTP_EMAIL")
        msg.set_content(f"Od: {name} <{email}>\n\n{message}")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(os.getenv("SMTP_EMAIL"), os.getenv("SMTP_PASSWORD"))
            smtp.send_message(msg)

        return JSONResponse({"status": "ok", "message": "Email byl úspěšně odeslán."})
    
    except Exception as e:
        print("❌ ERROR při odesílání:", e)
        return JSONResponse({"status": "error", "message": str(e)})