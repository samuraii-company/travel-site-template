from fastapi import FastAPI, HTTPException, status, Request, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from db import Database
from models import User, Orders
import uvicorn

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

db = Database()
app = FastAPI(docs_url="/documentation", redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

origins = ["https://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[" * "],
    allow_headers=[" * "],
)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def save_post(request: Request, email: Orders = Depends(Orders.as_form)):
    await db.insert_orders(insert_data=email.dict())
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/orders")
async def get_data_by_id():
    responce = await db.get_all_orders()
    if responce:
        return responce
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"orders not found"
    )

@app.get("/api")
async def get_data():
    responce = await db.get_all()
    return responce


@app.get("/api/{user_id}", response_model=User)
async def get_data_by_id(user_id: int):
    responce = await db.get_one(id=user_id)
    if responce:
        return responce
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id: {user_id} not found"
    )


@app.post("/api/create", response_model=User)
async def post_data(user_data: User):
    responce = await db.insert(insert_data=user_data.dict())
    if responce:
        return responce
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Something went wrong"
    )


@app.put("/api/update/{user_id}")
async def update_data(user_id: int, employee: str):
    responce = await db.update(
        id=user_id,
        employee=employee
    )
    if responce:
        return "data was Successfully updated"
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id: {user_id} not found"
    )


@app.get("/api/delete/{user_id}")
async def delete_data(user_id: int):
    responce = await db.delete(id=user_id)
    if responce:
        return "data was Successfully deleted"
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id: {user_id} not found, something went wrong"
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)