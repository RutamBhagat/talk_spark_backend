from langchain import hub
from langchain.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from app.tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
    given the full name {name_of_person} of a person I want you to give me a link to their Linkedin profile page.
    Your answer should only contain a URL 
    """
    tools_for_agent = [
        Tool(
            name="Crawl Google for Linkedin Profile",
            func=get_profile_url,
            description="Useful for when you need to get the Linkedin profile of a person",
        ),
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt,
    )
    agent_executor = AgentExecutor(
        agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True
    )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linkedin_profile_url = result["output"]
    return linkedin_profile_url
