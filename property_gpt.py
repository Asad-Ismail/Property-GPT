import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import pandas as pd
# From config import all api keys put your api keys in the config file
from config import *

# Read data frame
df = pd.read_csv(pd_path)

llm=OpenAI(temperature=0,max_tokens=1000,model_name="text-davinci-003")
#llm=OpenAI(temperature=0,max_tokens=1000,model_name="gpt-3.5-turbo-0301")


from propertyagent.base import create_property_agent as create_property_agnet
agent = create_property_agnet(llm, df, verbose=True)
#agent.run("Is 2023 a good time to buy a house in netherland?")
agent.run("Which cities are good to buy house in Netherlands in 2023 if I have a budget of 400,000 euros?")