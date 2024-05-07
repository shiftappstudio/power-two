from fastapi import FastAPI

# FastAPI app
app_fastapi = FastAPI()


@app_fastapi.get("/api/fastapi/greet")
async def fastapi_greet():
    return {"message": "Hello from FastAPI!"}


@app_fastapi.get("/api/fastapi/power/{number}")
async def power_of_two(number: int):
    """
    This function calculates the power of 2 for a given number.
    """
    result = number**2
    return {"number": number, "power_of_two": result}


if __name__ == "__main__":
    # FastAPI on port 8000 (modify as needed)
    import uvicorn

    uvicorn.run(app_fastapi, host="0.0.0.0", port=8000)
