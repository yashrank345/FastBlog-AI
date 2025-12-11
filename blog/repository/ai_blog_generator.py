import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from typing import Optional

load_dotenv()

# Use a VALID Groq model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    max_tokens=1500,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

BLOG_PROMPT = """
You are an expert blog writer.
Create a detailed, engaging, SEO-friendly blog post.

Topic: "{topic}"

Your blog must include:
- Strong introduction
- Headings/subheadings
- Examples & details
- Smooth flow
- Conclusion

Return only the final blog.
"""

def generate_blog(topic: str ,context_word : Optional [str] = None ) -> str:
    prompt = BLOG_PROMPT.format(topic=topic , context_word = context_word)
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
    
