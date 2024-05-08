import pandas as pd
from pandasai import SmartDataframe,SmartDatalake
from pandasai.llm import GooglePalm
from pandasai.llm import OpenAI
import sqlalchemy
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
from pandasai import SmartDataframe
import pandas as pd


'''

# Example DataFrame creation
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

llm = GooglePalm(api_key="AIzaSyDJFOcxnIr32GyRlMOgeKHBCVFQrbUXrqM")
sdf = SmartDataframe(df, config={"llm": llm})# Example: Generate a bar chart for the 'Age' column
print(sdf.chat("scatter plot"))

'''
db_user = "root"
db_password = "exl"
db_host = "localhost"
db_name = "healthcare"


dburl = 'mysql+mysqlconnector://root:exl@localhost:3306/healthcare'
engine = sqlalchemy.create_engine(dburl)
    
from sqlalchemy.sql import text

sql = '''
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'healthcare' 
    AND table_type = 'BASE TABLE';
'''
with engine.connect() as conn:
    query = conn.execute(text(sql))
    
df = pd.DataFrame(query.fetchall())

print(df.head(5))

print("vk")
API_KEY =  'my openai key'

llm = OpenAI(api_token=API_KEY)

df_connector = SmartDataframe(df, config={"llm": llm})
response = df_connector.chat("plot the line chart in last 5 year payments_date")
print(response)