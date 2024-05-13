try:
    # Path to the input file
    input_file = 'input.txt'

    # Path to the output file
    output_file = 'output.txt'

    # Read data from the input file
    with open(input_file, 'r') as infile:
        data = infile.read()

    # Write data to the output file
    with open(output_file, 'w') as outfile:
        outfile.write(data)

    print("Data has been successfully copied from '{}' to '{}'.".format(input_file, output_file))

except FileNotFoundError:
    print("Error: Input file '{}' not found.".format(input_file))
except IOError as e:
    print("Error: {}".format(e))
except Exception as e:
    print("An unexpected error occurred: {}".format(e))
