from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
import pandas as pd
from io import StringIO
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool

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
    question: str = Form(),
):

    _csvdata = StringIO(str(form_file.file.read(), 'utf-8'))
    csvdata = pd.read_csv(_csvdata)

    # https://python.langchain.com/docs/integrations/toolkits/python#fibonacci-example
    agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, max_tokens=1000),
        tool=PythonREPLTool(),
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    agent_executor.run(question)

    """
    1. CSV と入力文を入力し, 分析する Python コードを書かせる
    2. Python REPL で実行させる
    """

    return question