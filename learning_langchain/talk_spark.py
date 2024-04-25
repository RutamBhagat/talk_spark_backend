import json
from typing import Tuple
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from learning_langchain.agents.linkedin_lookup_agent import (
    lookup as linkedin_lookup_agent,
)
from learning_langchain.output_parsers import PersonIntel, person_intel_parser
from learning_langchain.third_parties.linkedin import scrape_linkedin_profile


def talk_spark(name: str) -> Tuple[PersonIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name)

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

    return (
        output,
        linkedin_data.get("profile_pic_url"),
        linkedin_data.get("full_name"),
    )
