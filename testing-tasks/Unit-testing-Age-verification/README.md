# Unit Testing - Age Verification Program

This Python program takes the user's age as input and returns a classification based on age groups. The program includes unit tests to ensure accurate functionality.

## Usage

To use the program, run the Python script and input the user's age when prompted.

```bash
python age_classifier.py
```

## Age Classification Options

- If the respondent's age is under 18: "You are a child"
- If the respondent's age is under 70: "You are an adult"
- If the respondent's age is 70 or above: "You are a pensioner"

## Unit Tests

The program includes unit tests to validate its accuracy for the three main age groups. To run the unit tests, use the following command:

```bash
python ageTesting.py
```

## Additional

The program is also designed to handle unexpected inputs gracefully.
Run the following three custom tests to ensure robustness:

1. Test with a non-numeric input (e.g., "abc"): Ensure the program handles non-numeric input and provides a meaningful response.

2. Test with a negative age input: Check if the program correctly handles negative age values.

3. Test with a very large age input: Verify that the program behaves appropriately when given an age beyond the expected range.

