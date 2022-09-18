'''Functions to connect to the database and return a cursor object'''
from connector import querydb as qdb

def get_cursor():
    '''Return a cursor object'''
    return qdb()

#return max withdrawal amount from transactions table
def get_max_withdrawal():
    '''Return the max withdrawal amount'''
    query="SELECT MAX(WITHDRAWAL_AMT) FROM default.transaction group by ACCOUNT_NO order by MAX(WITHDRAWAL_AMT) desc limit 1"
    result = qdb(query)
    return result

#return max deposit amount from transactions table
def get_max_deposit():
    '''Return the max deposit amount'''
    query="SELECT MAX(DEPOSIT_AMT) FROM default.transaction group by ACCOUNT_NO order by MAX(DEPOSIT_AMT) desc limit 1"
    result = qdb(query)
    return result
    