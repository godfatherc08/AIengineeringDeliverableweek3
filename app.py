
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.title('Video GAME Ideas')
prompt = st.text_input('Prompt my ai for video game ideas') 


import os 

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper


apikey = os.environ['GROQ_API_KEY']

title_template = PromptTemplate(
    input_variables = ['idea'], 
    template='give me some ideas for a video game {idea}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='give me a video game idea based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} '
)



llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=apikey,
)

title_chain = title_template | llm
script_chain = script_template | llm

wiki = WikipediaAPIWrapper()


if prompt: 
    title = title_chain.invoke({"idea": prompt})
    research = wiki.run(prompt)
    script = script_chain.invoke({
    "title": title,
    "wikipedia_research": research
})

    st.write(title) 
    st.write(script) 