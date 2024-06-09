from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI

from search_tools import SearchTools
from calculator_tools import CalculatorTools


""" 
Goal:
- create a 7-day travel itenary with detailed per day plan, 
including budget, packing suggestions and safety tips

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert
- Local Tour Guide

Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should be actionable
- Backstory should be their resume
"""

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py

class TravelAgents:
    
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Epert Travel Agent",
            backstory=dedent(f"""Expert in travel plannign and logistics. I have decades of expereince making travel iteneries for clients all over the world. 
                             I have a keen eye for detail and always make sure to provide the best possible experience for my clients. 
                             I am well versed in all aspects of travel planning, from booking flights and hotels to finding the best restaurants and attractions. 
                             I am dedicated to providing the best possible service to my clients and always go above 
                             and beyond to make sure they have an unforgettable trip."""),
            goal=dedent(f"""create a 7-day travel itenary with detailed per day plan, 
                            including budget, packing suggestions and safety tips"""),
            tools =
                [SearchTools.search_internet,
                CalculatorTools.calculate],
            #allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City selection expert",
            backstory=dedent(f"""I have years of experience in selecting the best cities for travel based on a variety of factors. I take into account the weather, season, budget, and client preferences to create the perfect travel itinerary. I have a keen eye for detail and always make sure to provide the best possible experience for my clients. I am dedicated to providing the best possible service to my clients and always go above and beyond to make sure they have an unforgettable trip."""),
            goal=dedent(f"""Select the best cities based on weather, season, budget, and client preferences. """),
            tools =
                [SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable and experienced local tour guide with a passion for sharing the beauty and culture of my city with visitors. I have years of experience leading tours and providing valuable insights into the history, culture, and attractions of my city. I am dedicated to providing the best possible experience for my clients and always go above and beyond to make sure they have an unforgettable trip. I am well-versed in all aspects of travel planning and logistics and always make sure to provide the best possible service to my clients."""),
            goal=dedent(f"""Provide the best insights and recommendations for the selected cities. """),
            tools =
                [SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
