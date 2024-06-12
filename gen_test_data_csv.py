import csv
import json
import sys
import itertools

def generate_test_data(columns, data_types_config):
    test_data = []

    
    header_row = columns
    test_data.append(header_row)

    
    value_combinations = [data_types_config[data_type] for data_type in columns]

    # Generate test data rows using combinations of values
    for combination in itertools.product(*value_combinations):
        test_data.append(combination)

    return test_data

def write_to_csv(filename, test_data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(test_data)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python generate_test_data.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]

    with open(config_file, 'r') as f:
        config = json.load(f)

    columns = config['columns']
    data_types_config = config['data_types']
    output_file = config['csv_path']

    test_data = generate_test_data(columns, data_types_config)
    write_to_csv(output_file, test_data)

    print(f"Test data generated successfully and saved to {output_file}.")
