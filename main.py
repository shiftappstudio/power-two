from fastapi import FastAPI

# FastAPI app
app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}
@app.get("/api/fastapi/greet")


async def fastapi_greet():
    return {"message": "Hello from FastAPI!"}


@app.get("/api/fastapi/power/{number}")
async def power_of_two(number: int):
    """
    This function calculates the power of 2 for a given number.
    """
    result = number**2
    return {"number": number, "power_of_two": result}


