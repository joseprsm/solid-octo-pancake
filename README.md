# Building Generative AI Solutions

## Getting Started

### Prerequisites
- [uv](https://github.com/astral-sh/uv) must be installed. You can install it with:
  ```sh
  pip install uv
  ```

### Installation
1. Clone the repository:
   ```sh
   git clone git@github.com:yourusername/building-generative-ai-solutions.git
   cd building-generative-ai-solutions
   ```
2. Install dependencies with uv:
   ```sh
   uv sync
   ```

### Environment Variables
Set the following environment variables to configure OpenAI access:
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `CHAT_MODEL`: (Optional) The chat model to use (e.g., `gpt-4.1-nano`)
- `EMBEDDING_MODEL`: (Optional) The embedding model to use (e.g., `text-embedding-3-small`)
- `OPENAI_API_BASE`: (Optional) The API endpoint to use. If not set, it is automatically set based on your API key (see below).

**Note:**
- If `OPENAI_API_KEY` starts with `voc-`, `OPENAI_API_BASE` is set to `https://openai.vocareum.com/v1` automatically.
- If `OPENAI_API_KEY` is not set, defaults are used for local deployment with Ollama.
- You can override these values with your own API keys and endpoints for production or cloud usage.

Example:
```sh
export OPENAI_API_KEY=sk-...yourkey...
export CHAT_MODEL=gpt-3.5-turbo
export EMBEDDING_MODEL=text-embedding-ada-002
# export OPENAI_API_BASE=http://localhost:11434/v1  # Optional, usually not needed
```

## Usage

You can use HomeMatch via the CLI after installing dependencies and setting environment variables.

### Run the HomeMatch CLI

To see available commands:
```sh
homematch --help
```

### Generate listings example

Generate listings with default options:
```sh
homematch generate
```
Or use make
make generate

Or with custom options:
```sh
homematch generate --n-neighborhoods 5 --n-quirks 4 --min-listings 2 --max-listings 10 --output data/listings.jsonl
```

See all available commands and options with:
```sh
homematch --help
homematch generate --help
```

### Generate embeddings example

Generate embeddings with default options:
```sh
homematch embeddings
```
Or use make
make embeddings  # This will run both homematch generate and homematch embeddings

Or with custom options:
```sh
homematch embeddings --input data/listings.jsonl
```

See all available options with:
```sh
homematch embeddings --help
```
