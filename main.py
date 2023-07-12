# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel
# import uvicorn

# app = FastAPI()

# @app.get('/blog')
# def index(limit = 10, published : bool = True, sort:Optional[str] = None):
#     print(f"{published} | {limit}")
#     if published:
#         print(123)
#         return {'data': f"{limit} published blog from the database"}
#     else:
#         print(22)
#         return {'data': f"{limit} blogs from the database"}
    

# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data': 'All unpublished data'}


# @app.get('/blog/{id}')
# def show(id):
#     return {'data':id}


# @app.get('/blog/{id}/comments')
# def comments(id, limit: int = 10):
#     return {'data':[1,2]}


# class Blog(BaseModel):
#     title : str
#     body : str
#     published : Optional[bool]

# @app.post('/blog')
# def create_blog(request: Blog):
#     return {'data': f'blog is created as {request.title}'}

