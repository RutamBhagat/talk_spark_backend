import os
import json


def scrape_linkedin_profile(linkedin_url: str):
    """
    Scrape information from LinkedIn profiles,
    Manually scrape the information from LinkedIn profile
    """
    print("Linkedin URL: ", linkedin_url)
    data = None
    # Check if the LinkedIn URL is present in the response.json file
    path = f"{os.getcwd()}/learning_langchain/third_parties/temp/response.json"
    print("Path: ", path)
    try:
        with open(path, "r") as file:
            print("File Opened")
            response_data = json.load(file)
            if linkedin_url in response_data:
                print("URL Found in response.json file")
                data = response_data[linkedin_url]
                print(data)
            else:
                print("URL Not Found in response.json file")
    except FileNotFoundError:
        print("File Not Found")
        data = None

    if data:
        return data
    return data

    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # header_dic = {"Authorization": f"Bearer {os.getenv('PROXYCURL_API_KEY')}"}
    # linkedin_url = "https://www.linkedin.com/in/andrewyng/"

    # # This is the actual code
    # response = requests.get(
    #     api_endpoint,
    #     headers=header_dic,
    #     params={"url": linkedin_url},
    # )

    # # This is the dummy code to save api credits
    # # dummy_json_endpoint = "https://gist.githubusercontent.com/RutamBhagat/686abd5b0c3f12b0f143d0e026e60a20/raw/354bac6011ac17f6fbcef51a2d6e71263fe61aec/andrew-ng.json"
    # # response = requests.get(dummy_json_endpoint)

    # data = response.json()

    # # This is dictionary comprehension filtering out empty values and unwanted keys
    # data = {
    #     data_key: data_value
    #     for data_key, data_value in data.items()
    #     if data_key not in ["people_also_viewed", "certifications"]
    #     and data_value not in ([], "", None)
    # }

    # # This removes the groups profile_pic_url from the data
    # if data.get("groups"):
    #     for group_dict in data.get("groups"):
    #         group_dict.pop("profile_pic_url")

    # # Store the response in the response.json file
    # try:
    #     with open(path, "r") as file:
    #         response_data = json.load(file)
    # except FileNotFoundError:
    #     response_data = {}

    # response_data[linkedin_url] = data
    # with open(path, "w") as f:
    #     json.dump(response_data, f, indent=2)

    # return data
