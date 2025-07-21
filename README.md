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
- `OPENAI_API_KEY`: (Optional) Your OpenAI API key. Not required for local Ollama usage.
- `CHAT_MODEL`: (Optional) The chat model to use (e.g., `gpt-4.1-nano`)
- `EMBEDDING_MODEL`: (Optional) The embedding model to use (e.g., `text-embedding-3-small`)
- `OPENAI_API_BASE`: (Optional) The API endpoint to use. If not set, it is automatically set based on your API key (see below).

**Note:**
- If `OPENAI_API_KEY` starts with `voc-`, `OPENAI_API_BASE` is set to `https://openai.vocareum.com/v1` automatically.
- If `OPENAI_API_KEY` is not set, defaults are used for local deployment with Ollama.
- You can override these values with your own API keys and endpoints for production or cloud usage.

Example:
```sh
# For cloud usage:
export OPENAI_API_KEY=sk-...yourkey...
export CHAT_MODEL=gpt-3.5-turbo
export EMBEDDING_MODEL=text-embedding-ada-002
# export OPENAI_API_BASE=http://localhost:11434/v1  # Optional, usually not needed

# For local Ollama usage, you can omit OPENAI_API_KEY:
# export CHAT_MODEL=qwen3:4b
# export EMBEDDING_MODEL=granite-embedding
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

### Search for listings example

The search feature provides an interactive conversational interface to find listings that match your preferences. It uses the generated embeddings to perform semantic search and ranks results based on your specific requirements.

Search for listings interactively:
```sh
homematch search
```

**How it works:**

1. **Interactive Conversation**: The system asks you questions about your preferences, such as:
   - How big do you want your house to be?
   - What are the 3 most important things for you in choosing this property?
   - Which amenities would you like?
   - Which transportation options are important to you?
   - How urban do you want your neighborhood to be?

2. **Semantic Search**: Your responses are summarized into a search query and used to find relevant listings from the vector store using semantic similarity.

3. **Intelligent Ranking**: Results are ranked and personalized based on your preferences, with scores indicating how well each listing matches your requirements.

4. **Rich Results**: Each result includes:
   - A personalized title
   - A tailored description highlighting how it matches your preferences
   - A relevance score

**Example interaction:**
```
🤖 How big do you want your house to be?
> I'm looking for a 2-3 bedroom apartment, around 80-100 square meters

🤖 What are 3 most important things for you in choosing this property?
> Good public transport, close to parks, and a modern kitchen

🤖 Which amenities would you like?
> Gym, parking space, and balcony

🤖 [Press Enter to search when done]
>

Searching for listings matching: 2-3 bedroom apartment, 80-100 sqm, good public transport, close to parks, modern kitchen, gym, parking, balcony

Ranked Listings:
Listing 1:
Title: Modern 2BR Apartment with Gym & Parking Near Park
Description: This 85 sqm apartment perfectly matches your needs with 2 bedrooms, a modern kitchen, and excellent public transport connections...
Score: 0.92
```

**Prerequisites for search:**
- Listings must be generated first (`homematch generate`)
- Embeddings must be created (`homematch embeddings`)
- Environment variables should be configured for your preferred LLM model
