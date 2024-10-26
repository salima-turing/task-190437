import pytest

def forecast_expenses(allocation, revenue):
	total_expense = 0
	for key, value in allocation.items():
		expense = revenue * (value/100)
		total_expense += expense
		allocation[key] = expense
	allocation['Total Expense'] = total_expense
	allocation['Profit'] = revenue - total_expense
	return allocation

@pytest.mark.parametrize("test_input, expected_output", [
	({"Sales": 60, "Marketing": 20, "Operations": 20}, {"Sales": 360.0, "Marketing": 120.0, "Operations": 120.0, "Total Expense": 600.0, "Profit": -240.0}),
	({"R&D": 30, "QA": 40, "Dev": 30}, {"R&D": 108.0, "QA": 144.0, "Dev": 108.0, "Total Expense": 360.0, "Profit": 72.0}),
	({"Advertising": 15, "Staff": 70, "Supplies": 15}, {"Advertising": 54.0, "Staff": 252.0, "Supplies": 54.0, "Total Expense": 360.0, "Profit": -108.0}),
])
def test_forecast_expenses(test_input, expected_output):
	revenue = 600
	result = forecast_expenses(test_input, revenue)
	for key, value in expected_output.items():
		assert pytest.approx(result[key], 0.01) == value

if __name__ == "__main__":
	pytest.main()
