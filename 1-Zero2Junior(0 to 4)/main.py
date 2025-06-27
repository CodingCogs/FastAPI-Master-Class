from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def سلام():
    return {
        "پیام": "یاد بگیریم FastAPI بیاید",
        }