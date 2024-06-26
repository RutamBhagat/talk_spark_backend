from fastapi import APIRouter, status
from app.talk_spark import talk_spark
from app.utils.type_classes import Person_Request


router = APIRouter()


@router.post("/process", status_code=status.HTTP_201_CREATED)
async def find_person_data(person_request: Person_Request):
    person_info, profile_pic_url, full_name = talk_spark(name=person_request.name)
    response = {
        "summary": person_info.summary,
        "interesting_facts": person_info.interesting_facts,
        "topics_of_interest": person_info.topics_of_interest,
        "ice_breakers": person_info.ice_breakers,
        "profile_picture": profile_pic_url,
        "full_name": full_name,
    }
    return response
