from crewai import Agent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


#from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools


class CityAgents():
  def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4o", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")



  def city_selection_agent(self):
    return Agent(
        role='City Selection Expert',
        goal='Select the best city based specific sustainability criteria',
        backstory=
        'An expert in analyzing city plans and sustainability data to pick ideal destinations',
        tools=[
            SearchTools.search_internet,
            #BrowserTools.scrape_and_summarize_website,
        ],
        llm=self.OpenAIGPT4,
        verbose=True)

  def local_expert(self):
    return Agent(
        role='Local Expert at this city',
        goal='Provide the BEST insights about the selected city',
        backstory="""A knowledgeable local guide with extensive information
        about the city, it's projects, sutainability initiatives and customs""",
        tools=[
            SearchTools.search_internet,
            #BrowserTools.scrape_and_summarize_website,
        ]
        ,
        llm=self.OpenAIGPT4,
        verbose=True)

  def travel_concierge(self):
    return Agent(
        role='Neighbourhood Expert',
        goal="""Knows the details about the neighbourhood and can provide insights on the best places to visit, eat and stay""",
        backstory="""Specialist in neighbourhood engagement and co-creation with 
        decades of experience""",
        tools=[
            SearchTools.search_internet,
            # BrowserTools.scrape_and_summarize_website,
            CalculatorTools.calculate,
        ],
        llm=self.OpenAIGPT4,
        verbose=True)
