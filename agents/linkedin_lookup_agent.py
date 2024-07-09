

import os
from dotenv import load_dotenv
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain import hub

from tools_for_agent.tools_search import get_profile_url_serpapi

load_dotenv()

def lookup(name:str) -> str:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
        temperature=0,
    )
    
    template = '''
    given the full name of the person below \n
    {name}
    \n
    I want you to get me a link to their linkedin profile. The answer should be only the link.
    '''
    
    prompt = PromptTemplate(
        input_variables=["name"], template=template
    )
    
    tools_agent = [
        Tool(
            name='Crawl google for linkedin profile page',
            func=get_profile_url_serpapi,
            description='Useful when you need get the Linkedin page URL',
        )
    ]
    
    react_prompt = hub.pull('hwchase17/react')
    
    agent = create_react_agent(
        llm=llm,
        prompt=react_prompt,
        tools=tools_agent,
    )
    
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools_agent, 
        verbose=True
    )
    
    result = agent_executor.invoke(
        input={'input':template.format_prompt(name=name)},
        )
    
    linkedin_url = result['output']
    
    return linkedin_url






if __name__ == '__main__':
    print(lookup('Eden Marco'))