from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="PrimeCoreClinic SaaS")

# DB simples (vai virar Postgres depois)
db_users = {}
db_leads = {}

class User(BaseModel):
    email: str
    password: str
    clinic: str

class Lead(BaseModel):
    clinic: str
    message: str

# LOGIN / REGISTRO
@app.post("/register")
def register(user: User):
    key = f"{user.clinic}:{user.email}"
    if key in db_users:
        raise HTTPException(400, "exists")
    db_users[key] = user.password
    return {"status": "registered"}

@app.post("/login")
def login(user: User):
    key = f"{user.clinic}:{user.email}"
    if db_users.get(key) != user.password:
        raise HTTPException(401, "invalid")
    return {"status": "logged"}

# IA DE VENDAS
@app.post("/ai")
def ai(lead: Lead):
    db_leads.setdefault(lead.clinic, []).append(lead.message)
    return {
        "reply": "Olá! Sou a IA da clínica. Posso te ajudar a agendar sua avaliação?",
        "status": "lead_captured"
    }

# DASHBOARD
@app.get("/dashboard/{clinic}")
def dashboard(clinic: str):
    return {
        "clinic": clinic,
        "leads": db_leads.get(clinic, [])
    }

@app.get("/")
def home():
    return {"status": "PrimeCoreClinic SaaS LIVE"}
