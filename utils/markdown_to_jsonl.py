import json


def markdown_to_jsonl(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        tasks = []
        task = None
        for line in infile:
            line = line.strip()
            if line.startswith("id :"):
                if task:
                    tasks.append(task)
                task = {'is_classification': False}
                task['id'] = line.split(" : ")[1]
            elif line.startswith("name :"):
                task['name'] = line.split(" : ")[1]
            elif line == "instruction :":
                instruction_lines = []
                while True:
                    next_line = infile.readline().strip()
                    if next_line.startswith("input") or next_line.startswith("output"):
                        break
                    instruction_lines.append(next_line)
                task['instruction'] = "\n\t".join(instruction_lines)
            elif line.startswith("```python"):
                output_lines = []
                while True:
                    next_line = infile.readline().strip()
                    if next_line.startswith("```"):
                        break
                    output_lines.append(next_line)
                if 'instances' not in task:
                    task['instances'] = [{'input': "", 'output': ''}]
                task['instances'][0]['output'] = "\n".join(output_lines)
        if task:
            tasks.append(task)
        for t in tasks:
            # Rearrange the dictionary to place the is_classification key as the last key
            t['is_classification'] = t.pop('is_classification')
            json.dump(t, outfile)
            outfile.write('\n')


# markdown_to_jsonl(input_file="path_to_input_file", output_file="path_to_output_file")
