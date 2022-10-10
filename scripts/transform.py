import pandas as pd

# Read the data
df=pd.read_csv('/workspaces/DE-Project-Repo-Durga/data/covid_19_data.csv')

# Transform the data
df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
df['Province/State']=df['Province/State'].str.upper()
df['Country/Region']=df['Country/Region'].str.upper()
df['Last Update']=pd.to_datetime(df['Last Update'])
df['Confirmed']=df['Confirmed'].astype(int)
df['Deaths']=df['Deaths'].astype(int)

df1=df.groupby(['ObservationDate','Country/Region'])['Confirmed','Deaths'].sum().reset_index()
df1['Active']=df1['Confirmed']-df1['Deaths']
df1['Country/Region']=df1['Country/Region'].str.upper()
df1['ObservationDate']=df1['ObservationDate'].dt.strftime('%Y-%m-%d')
df1['ObservationDate']=pd.to_datetime(df1['ObservationDate'])

# Write the data
df1.to_csv('/workspaces/DE-Project-Repo-Durga/data/covid_19_data_transformed.csv',index=False)