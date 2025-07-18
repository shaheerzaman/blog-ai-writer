import httpx

from blog_writer.agents.writer import WriterAgentDeps, writer_agent


# Main function to generate blog content
async def generate_blog_post(
    topic: str,
    author: str = '',
    author_role: str = '',
    user_requirements: str = '',
    opinions: str = '',
    examples: str = '',
    reference_links: list[str] = [],
) -> str:
    """Generate a blog post about the given topic."""
    http_client = httpx.AsyncClient()

    deps = WriterAgentDeps(
        http_client=http_client,
        author=author,
        author_role=author_role,
        user_requirements=user_requirements,
        opinions=opinions,
        examples=examples,
        reference_links=reference_links,
    )

    async with http_client:
        response = await writer_agent.run(
            f'Write a blog post about {topic}.',
            deps=deps,
        )
    return response.output
