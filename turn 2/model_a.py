import pytest

def forecast_budget(allocation, interest_rate=0.05, time_period=1, compounding_freq=1):

	if compounding_freq <= 0:
		raise ValueError("Compounding frequency must be a positive integer")

	future_value = allocation * (1 + interest_rate/compounding_freq) ** (compounding_freq * time_period)
	return future_value

@pytest.mark.parametrize("allocation, interest_rate, time_period, compounding_freq, expected_future_value", [
	(1000, 0.05, 2, 1, 1102.5),	# Test case 1: Annual compounding
	(1000, 0.05, 2, 4, 1102.5),	# Test case 2: Quarterly compounding
	(1000, 0.05, 2, 12, 1102.5),	# Test case 3: Monthly compounding
	(2000, 0.08, 3, 2, 2469.32),	# Test case 4: Different allocation, interest rate, and time period with Semi-annual compounding
	(500, 0.03, 1, 4, 506.25),	# Test case 5: Quarterly compounding
])
def test_forecast_budget_with_compounding(allocation, interest_rate, time_period, compounding_freq, expected_future_value):
	future_value = forecast_budget(allocation, interest_rate, time_period, compounding_freq)
	assert future_value == pytest.approx(expected_future_value, 0.01)

# Test for invalid compounding frequency
def test_invalid_compounding_freq():
	with pytest.raises(ValueError):
		forecast_budget(1000, compounding_freq=-1)

if __name__ == "__main__":
	pytest.main()
