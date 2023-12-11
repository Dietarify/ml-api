from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def status_check():
    return {
        "status": "success",
        "message": "server is running",
        "data": None
    }
