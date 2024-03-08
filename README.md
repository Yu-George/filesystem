# Filesystem

Simple File System implementation of cd, ls, mkdir and touch complete with unit tests.

## Prerequisites

- Python 3.10 or higher

## Installation

Clone the repository:

```bash
git clone https://github.com/Yu-George/filesystem.git
```

## Usage
Run the File System script using Python 3.10:

```
python main.py
```

Run the tests using Python 3.10:
```
python main.py
```

## Documentation
Commands:

`cd`: Takes in the directory path the user would like to change to. Supports moving to deeper subdirectories (eg: `cd dir1/dir2`). Additionally you can use `cd ..` to move back to parent directory and `cd` or `cd ~` to change to root.

`ls`: Lists all directories and files within the current directory

`touch`: Takes a file name at creates a file with given name (eg: `touch file.txt`)

`mkdir`: Creates a directory with user given path. Supports creating subdirectories on deeper levels (eg: `mkdir dir1/dir2`). Also multple directories on the same level (eg: `mkdir dir1 dir2`)

`exit`: Exits the program
