# Split the Bill
A Python application for managing shared group expenses. The core logic calculates individual balances using dynamic split ratios, allowing users to define specific cost-sharing rules assigned to different categories of expenses.

## Must have features:
- ID for people splitting a bill
- Insert a bill (date, people involved, total amount, how to split)
- Support multiple ways of splitting (equal parts, percentages)
- Settle up (returns who must pay to whom)
- Settle up (resets the bill)

## Running tests
`python -m unittest tests/test_01.py`