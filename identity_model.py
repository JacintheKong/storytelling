from langchain_core.pydantic_v1 import BaseModel, Field

class Identity(BaseModel):
    title: str = Field(description="title")
    content: str = Field(description="content")