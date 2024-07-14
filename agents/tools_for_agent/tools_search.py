from langchain_community.utilities import SerpAPIWrapper
import os
from dotenv import load_dotenv

load_dotenv()


def get_profile_url_serpapi(name:str):
    """
    Search for linkedin profile page
    """
    params = {
        'gl' : 'id'
    }
    search = SerpAPIWrapper(params=params, serpapi_api_key= os.getenv("SERPAPI_API_KEY"))
    res = search.results(f"{name} linkedin profile page")
    return res['organic_results'][0]['link']

if __name__ == "__main__":
    print(get_profile_url_serpapi("Hilmi Atha Putra"))

