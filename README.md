# Season Identifier by Month Input
This is a simple Python script that determines the season (Winter, Spring, Summer, or Autumn) based on the user's input. The input can be a month number, month name, or certain special symbols.

## File
- main.py — Main script that:
  - Asks the user to input a month.
  - Identifies the season based on the input.
  - Prints the corresponding season or an error if the input is invalid.

## Example Usage
```
Копировать
Редактировать
$ python main.py
Choose a month: March
Spring
```
```
Копировать
Редактировать
$ python main.py
Choose a month: 12
Winter
```

## Notes
- Supports month numbers (e.g., 1, 12), month names (January, Feb, etc.), and some special symbols (like !, @, #).
- Invalid input will result in: Error.

## Improvements Suggested
- Sanitize and normalize input (e.g., remove extra spaces, convert to lowercase).
- Avoid including unrelated symbols (like !@, !!, etc.) unless there's a specific reason.
- Consider using a dictionary or mapping for cleaner structure.

## How to Use
1. Make sure Python 3 is installed.  
   [Download Python](https://www.python.org/downloads/)
2. Clone the repository:
   ```bash
   git clone https://github.com/CodeRyzen/Year-Season.git
   cd SudoTeachIt-PythonFastCourse
   py main.py
   ```
