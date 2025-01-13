from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

app = FastAPI()

@app.get('/blog')
def index(limit=10, published : bool = True, sort:Optional[str]=None):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}
    
@app.post('/blog')
def creat_blog(blog:Blog):
    return {'data': f'Blog is created with title as {blog.title}'}

@app.get('/about')
def about():
    return {'data': {'about page'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': "all unpublished blogs"}

@app.get('/blog/{id}')
def show(id:int):
    return {'data' : id}


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1", port=9000)
