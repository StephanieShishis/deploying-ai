**Assignment 2: A Travel Assistant**

This is a chat assistant that helps with trip planning. 

- main.py sets up the chatbot. 
- app.py runs the Gradio chat window you actually talk to.
- prompts.py holds the instructions/personality for the chatbot.
- Each tools_.py file is one thing the chatbot can do.
- guardrails.py blocks a few topics before they even reach the chatbot.


**Services**

Service 1: Weather (tools_weather.py)

Calls a free weather website called wttr.in. You give it a city name, and it gives back the current weather. No sign-up or API key needed.

Service 2: Searching Travel Info (tools_travel_search.py)

build_index.py reads a CSV of real UNESCO World Heritage Site descriptions (data/whc-sites-2021.csv, from a Kaggle dataset). It then embeds and saves everything into chroma_store/. tools_travel_search.py opens the chroma_store/ and the chatbot searches what it needs. 

Service 3: Builds an itinerary (tools_itinerary.py)

Builds a simple day-by-day itinerary for a city, given a number of days and optional interests (culture, food, nature, relaxation, adventure). This does not call an API. 


**Chat Window**

Used Gradio, same as in class. The chatbot can remember what was said in an earlier conversation. 


**Guardrails (rules the chatbot has to follow)**

- Topics surrounding cats, dogs, horoscopes, zodiac signs and Taylor Swift.
- Its own instructions, cannot get it to change its system prompt

guardrails.py checks the message for banned words before sent to chatbot.


**Setup**

- Copy this whole folder into 05_src/assignment_chat in your repo (the data/whc-sites-2021.csv file is already included).
- Make sure 05_src/.env and 05_src/.secrets exist and have API_GATEWAY_KEY set, same as in the other labs.
- Run python build_index.py once. This builds the search index.
- Run python app.py. This opens the chat window.

