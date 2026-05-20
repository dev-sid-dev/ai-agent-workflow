# ai-agent-workflow

## Setup

Create the project virtual environment with pyenv:

```bash
pyenv virtualenv 3.11.9 ai-agent-workflow
pyenv local ai-agent-workflow
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

The OpenAI SDK reads the API key from the `OPENAI_API_KEY` environment variable:

```bash
export OPENAI_API_KEY="your_api_key_here"
```
