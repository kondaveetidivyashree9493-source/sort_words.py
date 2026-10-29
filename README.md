# Sorting Words from a File Using Python

## Aim
To read words from a file, convert uppercase words to lowercase, sort them alphabetically, and write them into another file.

## Requirements
- Python 3
- Input file named `input.txt`

## Functions Used
1. `open()` – Opens a file.
2. `read()` – Reads the file contents.
3. `split()` – Separates text into words.
4. `lower()` – Converts words to lowercase.
5. `sort()` – Sorts words alphabetically.
6. `write()` – Writes words into another file.

## Algorithm
1. Open the source file in read mode.
2. Read all words using `read().split()`.
3. Convert all words to lowercase.
4. Sort the words alphabetically.
5. Open the destination file in write mode.
6. Write each word on a separate line.
7. Display a confirmation message.

## Result
The program successfully converts words to lowercase, sorts them alphabetically, and saves them in `output.txt`.
