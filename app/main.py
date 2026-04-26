from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="PrimeCoreClinic")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body style="font-family:Arial;text-align:center;margin-top:50px">
            <h1>PrimeCoreClinic SaaS</h1>
            <p>IA de vendas para clínicas de estética</p>
        </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status":"ok"}
