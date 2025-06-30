import json


def load_jsonl(file_path: str) -> list[dict]:
    def load_line(line: str) -> dict:
        return json.loads(line.strip())

    with open(file_path, "r") as f:
        return map(load_line, f.readlines())


def write_jsonl(file_path: str, listings: list[dict]) -> None:
    listings: list[str] = map(json.dumps, listings)

    with open(file_path, "w") as f:
        for listing in listings:
            f.write(listing + "\n")
