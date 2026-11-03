# Password Strength Checker – Test Report

## Project
Python Password Strength Checker

## Test Cases

| No. | Test Password | Expected Result |
|---|---|---|
| 1 | hello | Invalid – too short |
| 2 | Hello123 | Invalid – missing special character |
| 3 | Hello123@ | Valid |
| 4 | Hello 123@ | Invalid – contains spaces |
| 5 | python123@ | Invalid – missing uppercase |
| 6 | PYTHON123@ | Invalid – missing lowercase |

## Testing Status
Testing in progress.

## Conclusion
The program is being tested to check password validation rules.
