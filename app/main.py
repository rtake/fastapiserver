from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd
from io import StringIO


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.post("/items")
def update_item(item: Item):
    return {"item_name": item.name, "twice price": item.price * 2}

@app.post("/uploadfile/")
async def create_upload_file(
    form_file: UploadFile = File(),
    user_input_text: str = Form(),
):

    _csvdata = StringIO(str(form_file.file.read(), 'utf-8'))
    csvdata = pd.read_csv(_csvdata)
    print(csvdata)

    """
    1. CSV と入力文を入力し, 分析する Python コードを書かせる
    2. Python REPL で実行させる
    """
    
    return user_input_text