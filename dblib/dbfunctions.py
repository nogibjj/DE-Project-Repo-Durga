'''Functions to connect to the database and return a cursor object'''
import sys
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '/workspaces/DE-Project-Repo-Durga')


from dblib.connector import Connector as con
#return max withdrawal amount from transactions table
def get_max_withdrawal():
    '''Return the max withdrawal amount'''
    qdb = con.Connector()
    query="SELECT MAX(WITHDRAWAL_AMT) FROM default.transaction group by ACCOUNT_NO order by MAX(WITHDRAWAL_AMT) desc limit 1"
    result = qdb.querydb(query)
    return result

#return max deposit amount from transactions table
def get_max_deposit():
    '''Return the max deposit amount'''
    qdb = con.Connector()
    query="SELECT MAX(DEPOSIT_AMT) FROM default.transaction group by ACCOUNT_NO order by MAX(DEPOSIT_AMT) desc limit 1"
    result = qdb.querydb(query)
    return result
