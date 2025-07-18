from typing import Annotated

from pydanti_ai import Agent
from pydantic import BaseModel, Field

from blog_writer.agents.shared import (
    get_guidelines,
    load_reviwer_prompt,
    load_writer_prompt,
)


class Review(BaseModel):
    score: Annotated[int, Field(ge=0, le=10)]
    """A score between 1 and 10"""

    feedback: str
    """Feedback on what can be improved. Should contain specific examples"""


reviewer_agent = Agent(
    'anthropic:claude-3-7-sonnet-latest',
    output_type=Review,
    tools=[get_guidelines],
    instructions=load_reviwer_prompt(),
)


@reviewer_agent.tool_plain
async def get_writer_instructions() -> str:
    """Get the blog post writing instructions that the writer should follow."""
    return load_writer_prompt()
