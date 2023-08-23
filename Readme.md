# Synthetic Data Generator

## Introduction
This repo will automate basic test data generation based on schema provided by the user and would be used by both platform and domain devs.
This utility is using Pandas Faker modules to randomly generate the test data on the basis of sample raw data.

Following datatypes are currently supported
1. String
2. Integer (Int)
3. Float
4. Date
5. Boolean (Bool)
6. Timestamp
7. Email
8. Text
9. Name
10. Phone_Number

Currently, the following data sinks are supported
1. CSV
2. JSON

## Setting up the environment
To create the environment run the following commands from project root:-
* **poetry lock** - It will create the virtual environment under the location ~/Library/Caches/pypoetry/virtualenvs/com-synthetic-data-generator-*
* **source < path to virtual environment >/bin/activate** - It will activate the virtual environment
* **poetry install** - will install dependencies inside the virtual environment

## Pre-Commit and Pre-Push
Install pre commit commit-msg hook. Run the following command from the folder root

```bash
pre-commit install
```

```bash
pre-commit install --hook-type commit-msg
```

For Pre-Push hook run the following command from the folder root

```bash
cp pre-push.sh .git/hooks/pre-push
```

Ensure the Pre-Push script is executable by running the following command from the root folder

```bash
chmod +x .git/hooks/pre-push
```

## Generating Sphinx Documentation
To create your documentation, ensure that you have the necessary dependencies, including Sphinx and the Sphinx-rtd-theme. These dependencies will be installed when you set up your Poetry environment.

Follow the below steps to generate the documentation locally:

1. Open a terminal and navigate to the project's root directory.
2. **Execute the below commands only when there additions/deletions/updations in the python files/modules**

   1. Remove the files with a specific pattern from the 'docs' folder:
      ```bash
      rm docs/com_synthetic_data_generator*.rst
      ```
   2. Run the following command to generate .rst format documentation:
      ```bash
       sphinx-apidoc -o docs .
      ```

3. From the root directory and run the following command to generate the documentation in HTML format:

   ```bash
   make -C docs html
   ```

4. The generated HTML documentation can be found in [docs/_build/html](docs/_build/html) directory.

5. To view the documentation, open the [index.html](docs/_build/html/index.html) file located within the [docs/_build/html](docs/_build/html) folder using a web browser.


## Sample schema file

Below is the sample of the schema file that needs to be provided to generate mock data

* **type** - specify the column data type from the above mentioned list.
* **number_of_rows** - No. of rows to be crated
* **empty_values** - boolean identifier to specify whether empty values are required for that column. Random number of rows are assigned with emoty values. Currently supported for [String, date, timestamp, email, text, name]
* **format** - specify the format of that particular column. The format types that are available for column types are:-
  * String - format : "10" - specifies the max characters
  * Integer - format : "1000" - specifies the max range
  * Float - format : "2" - specifies the max precision after decimal point
  * Date - format : "%Y-%m-%d" - specifies the date pattern
  * Text - format : "10" - specifies the max characters

```
{
    "type" : "object",
    "number_of_rows" : 5,
    "properties" : {
        "code" : {"type" : "string", "empty_values": true},
        "name" : {"type" : "int"},
        "a" : {"type" : "integer"},
        "c" : {"type" : "float", "format": "2"},
        "dt" : {"type" : "date"},
        "ts" : {"type" : "boolean"},
        "tst" : {"type" : "TIMESTAMP"},
        "email" : {"type" : "EMAIL"},
        "nm" : {"type" : "NAME"},
        "pnm" : {"type" : "PHONE_NUMBER"},
        "tx" : {"type" : "text"}
    }
}

```

### Command Line Arguments

To generate the data run the following commands from project root:-

* **poetry run generate --input_json_schema_path=< input json schema path > --output_file_format=< csv\json > --output_path=< output folder path >** - inside the output folder path the respective data.csv or data.json file will get generated
