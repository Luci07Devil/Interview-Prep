import csv
#Python script to read and write json files
import json

# Input and output file paths
input_json_file = 'input.json'
output_csv_file = 'output.csv'

try:
    # Read JSON data from input file
    with open(input_json_file, 'r') as json_file:
        data = json.load(json_file)

    # Open CSV file for writing
    with open(output_csv_file, 'w', newline='') as csv_file:
        # Extract field names from the first dictionary (assuming JSON data is a list of dictionaries)
        fieldnames = list(data[0].keys())

        # Create DictWriter object with field names
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write rows
        for row in data:
            writer.writerow(row)

    print(f"Data from {input_json_file} has been written to {output_csv_file} as CSV.")

except FileNotFoundError:
    print("Error: File not found. Please check the file paths.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format. Please ensure the input file contains valid JSON data.")
except Exception as e:
    print("An error occurred:", str(e))
