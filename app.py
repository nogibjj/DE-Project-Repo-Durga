'''Webapp'''
import uvicorn
from fastapi import FastAPI
import dblib.dbfunctions as db

app = FastAPI()

@app.get("/")
async def root():
    '''Root'''
    return {"message": "Hello Databricks"}

@app.get("/getMaxWithdrawal")
async def get_max_withdrawal():
    """Return the max withdrawal amount"""
    result = db.get_max_withdrawal()
    return {"Max Withdrawl Amount": result}

@app.get("/getMaxDeposit")
async def get_max_deposit():
    """Return the max deposit amount"""
    result = db.get_max_deposit()
    return {"Max Deposit Amount": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
