# Building Generative AI Solutions

## Getting Started

### Installation
1. Clone the repository:
   ```sh
   git clone git@github.com:yourusername/building-generative-ai-solutions.git
   cd building-generative-ai-solutions
   ```
2. Install dependencies with [uv](https://github.com/astral-sh/uv):
   ```sh
   uv sync
   ```

### Environment Variables
Set the following environment variables to configure OpenAI access:
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_MODEL`: (Optional) The model to use (e.g., `gpt-3.5-turbo`)

Example:
```sh
export OPENAI_API_KEY=sk-...yourkey...
export OPENAI_MODEL=gpt-3.5-turbo
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

Or with custom options:
```sh
homematch generate --n-neighborhoods 5 --n-quirks 4 --min-listings 2 --max-listings 10 --output data/listings.jsonl
```

See all available commands and options with:
```sh
homematch --help
homematch generate --help
```
