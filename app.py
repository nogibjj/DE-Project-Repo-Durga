'''Webapp'''
import uvicorn
from fastapi import FastAPI
from dblib.connector import querydb

app = FastAPI()

@app.get("/")
async def root():
    '''Root'''
    return {"message": "Hello Databricks"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""
    total = num1 + num2
    return {"total": total}


@app.get("/query")
async def query():
    """Execute a SQL query"""
    result = querydb("SELECT MAX(WITHDRAWAL_AMT) FROM default.transaction group by ACCOUNT_NO order by MAX(WITHDRAWAL_AMT) desc limit 1")
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
