# Test Data Generator

This Python script generates test data combinations based on predefined lists of values for each column. It can be useful for generating test data for automated testing, data analysis, or any other purposes where sample data is needed.

## Features

- Generates all possible combinations of values for the specified columns.
- Supports custom lists of values for each column.
- Outputs the generated test data to a CSV file.

## Usage

1. Clone the repository to your local machine:


2. Navigate to the directory containing the script and configuration file:

   ```bash
     cd ~/test_data_generator
   ```


4. Customize the `config.json` file to specify the columns and lists of values for each data type.

5. Run the script using the following command:

```python
python generate_test_data.py config.json
```


Replace `config.json` with the path to your customized configuration file.

5. The script will generate test data combinations based on the specified configuration and save the output to a CSV file.

## Configuration

The `config.json` file contains the following parameters:

- **columns**: List of column names for the test data.
- **data_types**: Dictionary specifying custom lists of values for each column. Each key is a column name, and the corresponding value is a list of predefined values.
- **csv_path**: Path to the output CSV file where the generated test data will be saved.

## Example

```json
{
 "columns": ["Name", "Age", "Height"],
 "data_types": {
     "Name": ["John", "Alice", "Bob"],
     "Age": [0, 4, 100],
     "Height": [1.2, 3.2, 4.5]
 },
 "csv_path": "test_data.csv"
}
```
This configuration will generate test data combinations for the Name, Age, and Height columns using the specified lists of values.


## test_data.csv
```csv
Name,Age,Height
John,0,1.2
John,0,3.2
John,0,4.5
John,4,1.2
John,4,3.2
John,4,4.5
John,100,1.2
John,100,3.2
John,100,4.5
Alice,0,1.2
Alice,0,3.2
Alice,0,4.5
Alice,4,1.2
Alice,4,3.2
Alice,4,4.5
Alice,100,1.2
Alice,100,3.2
Alice,100,4.5
Bob,0,1.2
Bob,0,3.2
Bob,0,4.5
Bob,4,1.2
Bob,4,3.2
Bob,4,4.5
Bob,100,1.2
Bob,100,3.2
Bob,100,4.5

```


