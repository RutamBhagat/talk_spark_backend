# TalkSpark: AI-Powered Conversation Starter

TalkSpark is a cool app that uses AI to give you great conversation starters. Just type in someone's name, and TalkSpark will find their social media profiles online. It looks at their info and interests to make custom icebreakers for you. This helps you start enjoyable chats with new people.

**Link to project:** [https://talk-spark-frontend.vercel.app/](https://talk-spark-frontend.vercel.app/)

**Frontend Repo:** https://github.com/RutamBhagat/talk_spark_frontend

**Backend Repo:** https://github.com/RutamBhagat/talk_spark_backend


https://github.com/RutamBhagat/talk_spark_frontend/assets/72187009/dfc43717-61d5-4391-8d1c-89f291d780c7


## How It's Made

**Tech used:** LangChain, Next.js, FASTAPI, Python, SearpAPI, ProxyCurl

TalkSpark uses LangChain, which is framework used to build apps with LLMs. It combines LangChain agents, custom tools, and output parsers to connect to peoples LinkedIn. This lets it pull public profile data.

SearpAPI, ProxyCurl helps TalkSpark grab info from websites by web scraping. The LangChain agents then process this data to make personalized profiles, fun facts, and custom icebreaker questions.

TalkSpark's code is built in sections, so you can add more data sources like twitter and facebook easily. Also you switch language models. The front-end uses Next.js to make it simple to use.

## Optimizations

To ensure optimal performance and scalability, TalkSpark employs several optimization techniques:

1. **Caching**: Frequently accessed social media profiles and web pages are cached to reduce redundant requests and improve response times.
2. **Asynchronous Processing**: Web scraping and data processing tasks are executed asynchronously, enabling TalkSpark to handle multiple requests concurrently without sacrificing responsiveness.

## Lessons Learned

Building TalkSpark taught me a ton about using LLMs, Langchain and web scraping in really cool ways, like:

- Combining multiple data sources and LLMs into one smooth app.
- Making custom agents and tools for LangChain to do exactly what I needed.
- Optimizing web scraping to make it fast and reliable.
- Adding async processing and caching to make things speedy.

This project made me really excited about using Langchain to solve practical problems and help people connect better.

## Examples

Here are a few examples showcasing TalkSpark's capabilities:

**Andrew NG:**
![Screenshot 2024-04-27 093353](https://github.com/RutamBhagat/talk_spark_frontend/assets/72187009/b86571e3-f384-470a-b38b-7d1f7bdb2ed0)

**Leon Noel:**
![Screenshot 2024-04-27 093443](https://github.com/RutamBhagat/talk_spark_frontend/assets/72187009/85e1fc08-9310-4aa4-891f-23eda8d72f60)

**Ankur Warikoo:**
![Screenshot 2024-04-27 093532](https://github.com/RutamBhagat/talk_spark_frontend/assets/72187009/dd5c1784-1951-418e-a956-f084589a0334)
