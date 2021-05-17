from typing import Optional
from fastapi import FastAPI, Depends, Header, HTTPException
from starlette.routing import Host
import uvicorn

app = FastAPI()

# for single Dependency ----------------------------------------------------------------
async def first_dependency(name: str = "Anupam"):
    return name


@app.get("/name/")
async def read_name(see_dependency: str = Depends(first_dependency)):
    if see_dependency == "Anupam Siwakoti":
        return "correct name"
    return "try again!!"


# ---------------------------------------------------------------------------------------

# for multiple Dependenies----------------------------------------------------------------
async def add(num1: int, num2: int):
    return num1 + num2


async def average(*, add: int = Depends(add), num3: int):
    return (add + num3) / 3


@app.get("/average/")
async def read_average(avg: int = Depends(average)):
    return {"Average": avg}


# -----------------------------------------------------------------------------------------

# for class Dependency----------------------------------------------------------------------


class hiring:
    def __init__(self, hire: int, delivery_place: str):
        self.hire = hire
        self.delivery_place = delivery_place


@app.get("/hire/")
async def read_hire(*, hire_class: hiring = Depends(), booking_customer: str):
    hire_details = {}
    hire_details.update(
        {
            "Customer": booking_customer,
            "Hiring number": hire_class.hire,
            "Delivery place": hire_class.delivery_place,
        }
    )
    return {"Order Details": hire_details}


# -------------------------------------------------------------------------------------------

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
