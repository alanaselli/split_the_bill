# Split the Bill
A Python application for managing shared group expenses. The core logic calculates individual balances using dynamic split ratios, allowing users to define specific cost-sharing rules assigned to different categories of expenses.

## Must have features
- ID for people splitting a bill
- Insert a bill (date, people involved, total amount, how to split)
- Support multiple ways of splitting (equal parts, percentages)
- Settle up (returns who must pay to whom)
- Settle up (resets the bill)

## Running tests
`python -m unittest tests/test_01.py`

## To-do
- Add a way to settle up
- Add a check inside the loop in `get_balances()` to skip bills where bill.is_settled  is  True .
- Write a test (e.g., test_get_balances_with_settled_bills) in test_01.py to assert that a settled bill is excluded from the balances.
- Write a test that calls `get_balances()` twice and asserts that the balances remain correct (do not double).
- Add a CLI