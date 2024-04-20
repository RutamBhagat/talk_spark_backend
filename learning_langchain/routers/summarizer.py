from fastapi import APIRouter, status

from learning_langchain.social_summarizer import social_summerizer
from learning_langchain.utils.type_classes import Person_Request

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_todo(person_request: Person_Request):
    return social_summerizer(name=person_request.name)
