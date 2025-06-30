.PHONY: embeddings

embeddings:
	@homematch generate --neighborhoods 3 --quirks 3 --min-listings 7 --max-listings 15 --output data/listings.jsonl
	@homematch embeddings --inputs data/listings.jsonl
