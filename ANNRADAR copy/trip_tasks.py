from crewai import Task
from textwrap import dedent
from datetime import date


class CityTasks():

  def identify_task(self, agent, origin, cities, interests, range):
    return Task(description=dedent(f"""
        Analyze and select the best city to run sustainabilty projects based 
        on specific criteria such as local sustainbility plans and initiatives, 
        greenhouse gas emission reduction potential. This task involves comparing
        multiple cities, considering factors like current sustainability initiatives,
        local government support, and potential for future growth.
        
        Your final answer must be a detailed
        report on the chosen city, and everything you found out
        about it, including the actual greenhouse gas emissions, the target for net zero emissions
        , the current and planned sustainability initiatives and other relevant information.
        {self.__tip_section()}

        Area considered: {origin}
        City Options: {cities}
        Trip Date: {range}
        Interests: {interests}
      """),
                agent=agent)

  def gather_task(self, agent, origin, interests, range):
    return Task(description=dedent(f"""
        As a local expert on this city you must compile an 
        in-depth guide for a city planner to identify sustainability projects!
        Gather information about  sustainability goals and recent accomplishments.
        
        This guide should provide a thorough overview of what 
        the city has to offer.
        
        The final answer must be a comprehensive city guide, 
        rich in sustainability insights and practical tips, 
        tailored to enhance the knowledge about the cities sustainability status.
        {self.__tip_section()}

        Trip Date: {range}
        Traveling from: {origin}
        Traveler Interests: {interests}
      """),
                agent=agent)

  def plan_task(self, agent, origin, interests, range):
    return Task(description=dedent(f"""
        Expand this guide into a a full report with key sustainability parameters
        like greenhouse gas emissions, net zero plan, number of EVs, 
        overall energy consumption and key projects.
        
        
        This report should cover all aspects of the climate neutral and 
        sustainable cit development, 
        from energy over mobility to bio diversity.
        
        Your final answer MUST be a complete expanded sustainability report,
        formatted as markdown, encompassing a detailed analysis of the city's 
        goals and achievements as well as key performance indicators related to
        sustainable urban development.
        
        # up each place, what make them special! 
        
        {self.__tip_section()}

        Trip Date: {range}
        Traveling from: {origin}
        Traveler Interests: {interests}
      """),
                agent=agent)

  def __tip_section(self):
    return "If you do your BEST WORK, you earn $1000!"
