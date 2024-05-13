#python script to read and write content in csv file
import csv

input_file = 'input.csv'
output_file = 'output.csv'

try:
    with open(input_file, 'r') as csv_input_file:
        with open(output_file, 'w', newline='') as csv_output_file:
            reader = csv.DictReader(csv_input_file)
            writer = csv.DictWriter(csv_output_file, fieldnames=reader.fieldnames)

            # Write header
            writer.writeheader()

            # Copy data from input to output file
            for row in reader:
                writer.writerow(row)

    print(f"Data has been copied from '{input_file}' to '{output_file}'")

except FileNotFoundError:
    print("File not found. Please check the file path.")

except Exception as e:
    print(f"An error occurred: {e}")
