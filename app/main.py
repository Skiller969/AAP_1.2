from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return{"status": "online", "message": "Trading Dashboard API Engine active"}

@app.get("/ticker/{symbol}")
def get_ticker_info(symbbol: str):
    return{
        "ticker":symbol.upper(),
        "status": "active",
        "mock_price": 150.25
    }
