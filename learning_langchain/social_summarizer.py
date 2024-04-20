from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import json

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":
    load_dotenv()

    linkedin_profile_url = linkedin_lookup_agent(name="Andrew Ng")

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    3. A Topic that may interest them
    4. Two creative ice breakers to start a conversation with them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)

    information = json.dumps(linkedin_data)  # Convert dictionary to JSON string

    res = chain.invoke(information)

    print("Output Text: ", res["text"])
