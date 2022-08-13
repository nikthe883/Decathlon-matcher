from typing import Optional
from fastapi import FastAPI,Request
import sqlite3
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

file_path = "Databases\Matching_Philosophy\Decathlon_matching_philosophy_EN.db"
@app.get("/")
def index(request: Request):
    con = sqlite3.connect(file_path)
    cursor = con.cursor()

    cursor.execute("select * from Decathlon where [product] like 'BASKET BALL'")
    data = cursor.fetchall()
    return templates.TemplateResponse("index.html", {"request": request, "basket": data})

def search_job(query: str):
    con = sqlite3.connect(file_path)
    cursor = con.cursor()

    cursor.execute("select * from Decathlon where [product] like ?", (f"%{query}%",))
    data = cursor.fetchall()
    return data

@app.get('/search')
def search(request: Request, query: Optional[str] = None):
    data = search_job(query)
    return templates.TemplateResponse("index.html", {"request": request, "basket": data})