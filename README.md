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

To run the HomeMatch example:
```sh
python -m homematch
```
