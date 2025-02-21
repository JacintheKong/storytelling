from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from identity_model import Identity
from prompt_template import META_PROMPT
import json

def generate_story(theme, identity, openai_api_key):
    # Step 1: Generate the storytelling prompt dynamically
    meta_model = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
    storytelling_prompt = meta_model.invoke(META_PROMPT.format(identity=identity)).content

    # Step 2: Use the AI-generated storytelling prompt to create the story
    # story_prompt = ChatPromptTemplate.from_messages([
    #     ("system", storytelling_prompt),
    #     ("user", "{theme}")
    # ])
    story_prompt = ChatPromptTemplate.from_messages([
        ("system", storytelling_prompt),
        ("user", "{theme}\n\n{parser_instructions}")
    ])
    story_model = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
    output_parser = PydanticOutputParser(pydantic_object=Identity)
    chain = story_prompt | story_model | output_parser

    try:
        result = chain.invoke({
            "parser_instructions": output_parser.get_format_instructions(),
            "theme": theme
        })
        return result
    except json.JSONDecodeError as e:
        # Log error and return a message or handle it appropriately
        print("Failed to parse JSON output:", e)
        return None  # or handle as appropriate
