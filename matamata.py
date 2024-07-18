import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)
from third_party.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup
from output_parser import summary_parser, summary

load_dotenv()
def cari_linkedin(name:str) -> tuple[summary, str]:
    linkedin_link = lookup(name=name)
    data = scrape_linkedin_profile(linkedin_link, mock=False)
    
    # create a prompt template
    summary_template = """
    given the information below
    \n
    {information}
    \n
    I want you to create :\n
    1. short summary of the information\n
    2. 3 fun facts about them\n
    2. how to approach and get closer with the person in the information (max 3 points)\n
    
    
    \n\n\n\n
    I WANT YOU TO ANSWER IN BAHASA INDONESIA
    \n{format_instructions}
    """
    summary_prompt = PromptTemplate(
        input_variables=["information"], template=summary_template, partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    # instantiate llm model
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
        temperature=0.2,
    )

    chain = summary_prompt | llm | summary_parser
    
    #running the chain
    res:summary = chain.invoke(input={"information": data})
    
    return res, data.get('profile_pic_url')

if __name__ == "__main__":
    print('GetToKnow')
    print('==========')
    print(cari_linkedin('Eden Marco'))
