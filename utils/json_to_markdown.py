import json


def transform_to_markdown(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            data = json.loads(line)
            outfile.write(f"id : {data['id']}\n")
            outfile.write(f"name : {data['name']}\n")
            outfile.write("instruction :\n")
            outfile.write("```gherkin\n")
            outfile.write(data['instruction'] + '\n')
            outfile.write("```\n")
            outfile.write("input = ")
            outfile.write(json.dumps(data['instances'][0]['input']) + "\n")
            outfile.write("output:\n")
            outfile.write("```python\n")
            outfile.write(data['instances'][0]['output'] + "\n")
            outfile.write("```\n\n")


# transform_to_markdown(input_file="path_to_input_file", output_file="path_to_output_file")
