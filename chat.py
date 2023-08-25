import os
import sys
import constants
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine
from langchain import OpenAI, SQLDatabase

import urllib.parse
urllib.parse.quote_plus("Admin@123")

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# loader = TextLoader('data.txt')
# loader = DirectoryLoader("data/")
# loader = DirectoryLoader("data/", glob="*.txt")
# loader = DirectoryLoader("data/", glob="*.txt|*.pdf")

#index = VectorstoreIndexCreator().from_loaders([loader])

#print(index.query(query, llm=ChatOpenAI()))

#-------------------------------------------
engine = create_engine(f'hana://{constants.user}:{constants.password}@{constants.host}:{constants.port}')

db = SQLDatabase(engine=engine)

from langchain.chat_models import ChatOpenAI
#openai = ChatOpenAI(model_name="gpt-3.5-turbo")
openai = ChatOpenAI(model_name="gpt-3.5-turbo")

from langchain_experimental.sql import SQLDatabaseChain

chain = SQLDatabaseChain.from_llm(llm=openai, db=db,verbose=False)

#-------------------------------------------------------------------------
query = sys.argv[1]
response = chain.run(query)
print(response)

