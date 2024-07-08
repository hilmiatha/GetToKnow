import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)
from third_party.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()

    # create a prompt template
    summary_template = """
    given the information below
    \n
    {information}
    \n
    I want you to create :\n
    1. short summary of the information\n
    2. how to attract and get closer with the person in the information\n
    """
    summary_prompt = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # instantiate llm model
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
        temperature=0.2,
    )

    # creating a chain
    information_test = "Jamal Musiala (born 26 February 2003) is a German professional footballer who plays as an attacking midfielder and winger for \
        Bundesliga club Bayern Munich and the Germany national team. Nicknamed 'Bambi' for his technical dribbling ability, he is considered to be one of the best young players in the world.[10] \
        Born in Germany to a Nigerian-British father and Polish-German mother, he was raised from the age of seven in England. Musiala has played \
            for both Germany and England national teams at youth level, and eventually pledged his allegiance to the German Football Association for \
                future games in February 2021. He has represented the side at UEFA Euro 2020, the 2022 FIFA World Cup, and UEFA Euro 2024."
    linkedin_data = scrape_linkedin_profile(
        "https://www.linkedin.com/in/jamal-musiala-8b9a0b1b9/", mock=True
    )
    
    chain = summary_prompt | llm
    
    #running the chain
    res = chain.invoke(input={"information": linkedin_data})
    print(res.content)
