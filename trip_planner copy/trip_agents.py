from crewai import Agent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


#from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools


class TripAgents():
  def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4o", temperature=0.7)
        self.Ollama = Ollama(model="llama3", base_url="172.17.0.3:11434")



  def city_selection_agent(self):
    return Agent(
        role='City Selection Expert',
        goal='Select the best city based on weather, season, and prices',
        backstory=
        'An expert in analyzing travel data to pick ideal destinations',
        tools=[
            SearchTools.search_internet,
            #BrowserTools.scrape_and_summarize_website,
        ],
        llm=self.Ollama,
        verbose=True)

  def local_expert(self):
    return Agent(
        role='Local Expert at this city',
        goal='Provide the BEST insights about the selected city',
        backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
        tools=[
            SearchTools.search_internet,
            #BrowserTools.scrape_and_summarize_website,
        ]
        ,
        llm=self.Ollama,
        verbose=True)

  def travel_concierge(self):
    return Agent(
        role='Amazing Travel Concierge',
        goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
        backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
        tools=[
            SearchTools.search_internet,
            # BrowserTools.scrape_and_summarize_website,
            CalculatorTools.calculate,
        ],
        llm=self.Ollama,
        verbose=True)
