from ast import List
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of the person")
    interesting_facts: List[str] = Field(
        description="Two interesting facts about the person"
    )
    topics_of_interest: str = Field(description="Topic that may interest the person")
    ice_breakers: List[str] = Field(
        description="Two creative ice breakers to start a conversation with the person"
    )

    def to_dict(self):
        return {
            "summary": self.summary,
            "interesting_facts": self.interesting_facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers,
        }


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)
