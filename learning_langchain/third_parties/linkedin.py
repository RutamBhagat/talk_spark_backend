import os
import requests


def scrape_linkedin_profile(linkedin_url: str):
    """
    scrape information from LinkedIn profiles,
    Manually scrape the information from LinkedIn profile
    """
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # header_dic = {"Authorization": f"Bearer {os.getenv('PROXYCURL_API_KEY')}"}

    # linkedin_url = "https://www.linkedin.com/in/andrewyng/"

    ## This is the actual code

    # response = requests.get(
    #     api_endpoint,
    #     headers=header_dic,
    #     params={"url": linkedin_url},
    # )

    # This is the dummy code to save api credits
    dummy_json_endpoint = "https://gist.githubusercontent.com/RutamBhagat/686abd5b0c3f12b0f143d0e026e60a20/raw/354bac6011ac17f6fbcef51a2d6e71263fe61aec/andrew-ng.json"
    response = requests.get(dummy_json_endpoint)

    data = response.json()

    # This is dictionary comprehention filtering out empty values and unwanted keys
    data = {
        data_key: data_value
        for data_key, data_value in data.items()
        if data_key not in ["people_also_viewed", "certifications"]
        and data_value not in ([], "", None)
    }

    # This removes the groups profile_pic_url from the data
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
