def extract_elements(input_file, output_file, num_elements):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()[:num_elements]

    with open(output_file, 'w') as f_out:
        for line in lines:
            f_out.write(line)


# extract_elements(input_file="path_to_input_file", output_file="path_to_output_file")
