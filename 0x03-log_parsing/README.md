# 0x03. Log Parsing

## Overview

This project focuses on parsing and processing data streams in real-time using Python. You will read from standard input (stdin), handle data in a specific format, and perform calculations based on the input data. The goal is to effectively handle data streams, parse log entries, and compute metrics based on the processed data.

## Concepts and Resources

### File I/O in Python
- **Reading from sys.stdin line by line**
- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

### Signal Handling in Python
- **Handling keyboard interruption (CTRL + C) using signal handling in Python**
- [Python Signal Handling](https://docs.python.org/3/library/signal.html)

### Data Processing
- **Parsing strings to extract specific data points**
- **Aggregating data to compute summaries**

### Regular Expressions
- **Using regular expressions to validate the format of each line**
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)

### Dictionaries in Python
- **Using dictionaries to count occurrences of status codes and accumulate file sizes**
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Exception Handling
- **Handling possible exceptions that may arise during file reading and data processing**
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

## Additional Resources
- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=5dRTK-_Bzd0)

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using `wc`

## Project Description

In this project, you will write a Python script to read and process log data from standard input. The script should:
- Read log entries line by line.
- Validate the format of each log entry using regular expressions.
- Extract specific data points such as status codes and file sizes.
- Aggregate data to compute summaries, such as the total file size and counts of each status code.
- Handle keyboard interruptions gracefully using signal handling.
- Handle exceptions that may occur during file reading and processing.

By studying the provided concepts and utilizing the resources, you will be well-prepared to complete the log parsing project.
