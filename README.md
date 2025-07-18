```
Configure your LLM provider token
Depending on the provider used, set the appropriate environment variable.

This demo project uses Anthropic, and can be configured as such:

export ANTHROPIC_API_KEY="your_anthropic_key_here"

To enable automatic PR creation to the pydantic.dev repository:

export GITHUB_TOKEN="your_github_personal_access_token"
GitHub Token Permissions Required:

repo (Full control of private repositories)
workflow (Update GitHub Action workflows)
```
