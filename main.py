import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, HttpUrl
import requests
from io import BytesIO
from dotenv import load_dotenv
from docling.datamodel.base_models import DocumentStream
from docling.document_converter import DocumentConverter

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
PORT= os.getenv("PORT", 8000)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

app = FastAPI(title="Conversor HTML para Markdown")

# Middleware security
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    v
    """
    if not credentials or credentials.credentials != API_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido ou não fornecido")

class URLRequest(BaseModel):
    url: HttpUrl

@app.post("/convert", summary="Converte HTML de uma URL para Markdown", dependencies=[Depends(verify_token)])
def convert_url_to_markdown(payload: URLRequest):
    """
      Converts an HTML page into Markdown, protecting the endpoint with Bearer authentication.
    """
    # Try searching for the HTML content of the URL
    try:
        response = requests.get(payload.url, timeout=20, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Erro ao buscar a URL: {e}")
    
    html_content = response.content

    # Tenta converter or HTML to Markdown using docling
    try:
        stream = BytesIO(html_content)
        source = DocumentStream(name="page.html", stream=stream)
        converter = DocumentConverter()
        result = converter.convert(source)
        markdown = result.document.export_to_markdown()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na conversão de HTML para Markdown: {e}")
    
    return {"markdown": markdown}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
