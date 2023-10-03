# amazon_massive_dataset
## Brief Summary

Set up a new Python3 Development environment, install relevant dependencies, build a Python3 project with PyCharm structure, and import the provided MASSIVE Dataset. Generate en-xx.xlsx files for all languages using id, utt, and annot_utt fields, avoiding recursive algorithms. Generate separate json files for English (en), Swahili (sw), and German (de) for test, train, and dev datasets. Additionally, generate a large json file showing translations from en to xx with id and utt for all train sets. Ensure the JSON file structure is pretty printed.

## Table of Contents
- [Dependencies](#dependencies)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Dependencies

Ensure you have the following dependencies installed:
- Download Python 3.x : Click on the following link to download Python https://www.python.org/
- Download an IDE environment that well suites you i.e PyCharm https://www.jetbrains.com/help/pycharm/installation-guide.html#silent
- Setup an environment using either pip or you can use Anaconda, which will automatically create an environment for you. Click the following link to download Anaconda https://www.anaconda.com/download
- Make sure to set the Python interpreter as the environment you will be using for this project
- Pandas: You can install it using pip with
  bash
  pip install pandas
  
- openpyxl: Used to read and write Excel files. You can install it using the command
  bash
  pip install openpyxl

Dependecies that are **Pre-installed** in Python include:
- Tarfile: a standard library module in Python that provides the ability to read and create tar archives, it is also used in Unix and Linux systems to bundle files together into a single archive i.e **Amazon massive data file**



- os: A standard Python library that provides a portable way of interacting with the operating system, allowing you to perform various tasks related to file and directory operations, process management, path manipulation, runnin shell commands and more

- json: Provides functions for encoding and decoding JSON(JavaScript Object Notation) data. JSON is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate

## Getting Started

1. Clone the repository to get started:

bash
git clone https://github.com/your-username/your-project.git
cd your-project


2. Navigate to the repository
   Use the cd command to navigate to the directory where the repository was cloned.
   bash
   cd repository
   
3. Install Dependencies:
   If the code relies on external Python packages that are not part of the standard library, you may need to install them. Typically, you can find the dependencies listed in a requirements.txt file or similar. Use a tool like pip to install them:
bash
pip install -r requirements.txt


## Configuration

To configure the project for your specific environment, you may need to make the following changes:

1. **Import and Extract the Amazon massive data file**: Declare the file path and use the tarfile library to extract content from the **Amazon Massive Data file** into an already created directory.

2. **Data Directory**: Update the `data_directory` variable in the code to point to the directory containing your JSONL files.
   
   python
   data_directory = r'path/to/your/data_directory'
   

3. **Output Directory**: Update the `output_dir` variable to specify where you want to save the generated Excel files.
   
   python
   output_dir = r'path/to/your/output_directory'
   

4. **Keyword and Field**: When running the script, you can specify the keyword and field for filtering using the `--keyword` and `--field` arguments.
   
   shell
   python script_name.py --keyword your_keyword --field your_field
   
 ### Folder structure

Here's a folder structure for the project:


my-project/     # Root directory.
|- data/        # Folder used to store the massive dataset .
|- src/          # source codes.
|- output_excel_files/       # excel files folder.
|- partitions _ttd/  # folder used to store the parttitions jsonl.
|- output      # contains the combined json.
```
