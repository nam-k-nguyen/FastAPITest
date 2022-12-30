from fastapi import FastAPI, Response
from pydantic import BaseModel

# Global var
htmlText = ''

app = FastAPI()

class Item(BaseModel):
    html: str

@app.get("/")
def read_root():
    return Response(content=htmlText, media_type="text/html")


@app.post("/")
def create_something(item: Item):
    global htmlText
    htmlText = item.dict()['html']
    return "Set html text sucessfully."