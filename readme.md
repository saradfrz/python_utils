# Utils [in progress]

## Project Description
This project provides a set of Python utility functions to standardize common operations across different projects. The functions in this project cover a variety of areas, including working with directories and files, logging, database connections, and more.

With these utility functions, you can easily perform tasks such as creating directories, reading and writing files, setting up logging for your project, connecting to databases, and executing SQL queries. The functions are designed to be reusable and customizable, allowing you to tailor them to your specific needs.

The utility functions are organized into modules, each of which covers a specific area of functionality. This makes it easy to find the functions you need and to import them into your projects. The code is well-documented and follows best practices, making it easy to understand and maintain.

This project is ideal for developers who want to standardize their development processes across multiple projects, or who want to quickly and easily perform common operations without having to write the same code over and over again. By using these utility functions, you can save time and effort, and focus on building the core functionality of your projects.

## Language
Python

## File utils 

### `read_file(filepath)`
Reads the content of a txt or html file.
#### Arguments
- `filepath` (str): File relative path. 
##### Return Value
- `str`: File contents.

### `save_file(filepath, data)`
Saves a string to a file (admits txt or html format).
#### Arguments
- `filepath` (str): File relative path
- `data` (str): File contents to be saved.
#### Return Value
- `bool`: `True` if successful.

### `def read_json(filepath)`
Reads a json file.
#### Arguments
- `filepath` (str): File relative path
#### Return Value
- `dict`: JSON contents.

### `save_json(filepath, data)`
Saves a list or a dictionary to a JSON file.
#### Arguments
- `filepath` (str): File relative path
- `data` (list/dict): File contents to be saved.
#### Return Value
- `bool`: `True` if successful.

### `read_csv(filepath, delimiter)`
This function (edit).
#### Arguments
- `arg1` (str): File relative path
- `ar2` (str): File contents to be saved.
#### Return Value
- `str`: Response of the saving operation.


### `read_csv_as_dict(filepath, delimiter)`
This function (edit).
#### Arguments
- `arg1` (str): File relative path
- `ar2` (str): File contents to be saved.
#### Return Value
- `str`: Response of the saving operation.

### `save_csv(filepath, data)`
This function (edit).
#### Arguments
- `arg1` (str): File relative path
- `ar2` (str): File contents to be saved.
#### Return Value
- `bool`: `True` if successful.

### `save_csv_dict(filepath, data)`
This function (edit).
#### Arguments
- `arg1` (str): File relative path
- `ar2` (str): File contents to be saved.
#### Return Value
- `bool`: `True` if successful.


## Dir utils

### `is_dir(mypath)`
Checks if *mypath* exists.
#### Arguments
- `mypath` (str): Relative path
#### Return Value
- `bool`: `True` if exists.


## Datetime utils: 
### `dt_now()`
Returns today's date formatted as yyyy-mm-dd.

#### Return Value
- `str`: yyyy-mm-dd. Example: "2023-02-20"

## Log utils