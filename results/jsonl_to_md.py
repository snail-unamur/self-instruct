from dataclasses import dataclass
import json
import re

@dataclass
class Dataset:
    jsonl_path: str
    shorthand: str

MQ = Dataset("data/raw/mixed_quality_results_sample.jsonl", "MQFS")
HQ = Dataset("data/raw/high_quality_results_sample.jsonl", "HQFS")


def extract_gherkin(text):
    """Extracts the Gherkin code block from the text."""
    pattern = re.compile(
        r"```gherkin[^\S\n]*\n?(.*?)```",
        re.DOTALL | re.IGNORECASE
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else None

def extract_python(text):
    """Extracts the Python code block from the text."""
    pattern = re.compile(
        r"```python[^\S\n]*\n?(.*?)```",
        re.DOTALL | re.IGNORECASE
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else None

def format_gherkin(gherkin):
    """Formats the Gherkin code by ensuring each keyword starts on a new line."""
    return re.sub(
        r'\b(given|when|then|and|but)\b',
        r'\n   \1',
        gherkin,
        flags=re.IGNORECASE
    ).strip()


for dataset in [MQ, HQ]:
    with open(dataset.jsonl_path) as f:
        for i, scenario_raw in enumerate(f.readlines()):

            scenario_json = json.loads(scenario_raw)
            text = scenario_json["instruction"] + "\n\n" + scenario_json["input"] + "\n\n"  + scenario_json["output"]
            gherkin = extract_gherkin(text)
            gherkin = format_gherkin(gherkin) if gherkin else None
            python = extract_python(text)
            buffer = f"# {dataset.shorthand}{i + 1}"
            buffer += f"""
## Scenario
```gherkin
{gherkin}
```


## Python Implementation
```python
{python}
```


## Raw Text
{text}
"""
            with open(f"data/md/{dataset.shorthand}/{dataset.shorthand}{i + 1}.md", "w") as f:
                f.write(buffer)