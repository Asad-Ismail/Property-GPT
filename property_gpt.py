import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import pandas as pd
# From config import all api keys put your api keys in the config file
from config import *
from propertyagent.base import create_property_agent as create_property_agnet

# Read data frame
df = pd.read_csv(pd_path)

llm=OpenAI(temperature=0,max_tokens=1000,model_name="text-davinci-003")
#llm=OpenAI(temperature=0,max_tokens=1000,model_name="gpt-3.5-turbo-0301")

agent = create_property_agnet(llm, df, verbose=True,dateRestrict="m6")
#agent.run("Is 2023 a good time to buy a house in netherland?")
#query="Is it better to rent or buy a house in 2023 in Netherlands I am currently paying 1600 per month for rent and intend to stay Netherlands for 5 more years?"
query="Can you find me the top 3 best deals properties from listing following are my requirements:\
\n 1. Should be close to Rotterdam city center or very close to connection to public transport \
\n 2. Should be less than 400000. \
\n 3. Should have good energe rating A or better \
\n 4. Should be built in last 10 years"
query="Top cities/towns to buy house in Netherlands in 2023 with afforadable prices in the region close to Rotterdam and Dordecht"
#query="Which cities are good to buy house in Netherlands in 2023 if I have a budget of 400,000 euros,have good facilities like schools, universities and low crime rate?"
print(f"Query is {query}")
agent.run(query)