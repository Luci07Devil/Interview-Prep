import yaml

def read_yaml(input_file):
    try:
        with open(input_file, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print("Error: Input file not found.")
        return None
    except yaml.YAMLError as e:
        print("Error: Failed to parse YAML data:", e)
        return None

def write_yaml(data, output_file):
    try:
        with open(output_file, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
        print("YAML data has been written to", output_file)
    except IOError:
        print("Error: Unable to write to output file.")
    except yaml.YAMLError as e:
        print("Error: Failed to serialize YAML data:", e)

if __name__ == "__main__":
    input_file = "input.yaml"
    output_file = "output.yaml"

    # Read YAML data from input file
    yaml_data = read_yaml(input_file)
    
    # If YAML data is successfully read, write it to the output file
    if yaml_data:
        write_yaml(yaml_data, output_file)
