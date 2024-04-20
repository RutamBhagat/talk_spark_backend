import json
from dotenv import load_dotenv
from typing import Tuple
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import PersonIntel, person_intel_parser


def social_summerizer(name: str) -> Tuple[PersonIntel, str]:
    load_dotenv()

    linkedin_profile_url = linkedin_lookup_agent(name="Andrew Ng")

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    3. A Topic that may interest them
    4. Two creative ice breakers to start a conversation with them
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)

    information = json.dumps(linkedin_data)  # Convert dictionary to JSON string

    res = chain.invoke(information)

    output = person_intel_parser.parse(res["text"])

    print("Output Text: ", output)

    return (output, linkedin_data.get("profile_pic_url"))


if __name__ == "__main__":
    social_summerizer(name="Andrew Ng")
