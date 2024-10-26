import pytest


def forecast_budget(allocation, interest_rate=0.05, time_period=1):
    """
    Simple forecasting function that calculates the future value of an allocation
    with a given interest rate over a specific time period.
    """
    future_value = allocation * (1 + interest_rate) ** time_period
    return future_value


@pytest.mark.parametrize("allocation, expected_future_value", [
    (1000, 1050),  # Test case 1: Default interest rate and time period
    (2000, 2100),  # Test case 2: Default interest rate and time period
    (500, 525),  # Test case 3: Default interest rate and time period
    (1500, 1627.5),  # Test case 4: Default interest rate and time period
    (3000, 3464.1),  # Test case 5: Default interest rate and time period
    # Add more test cases for different allocations
])
def test_forecast_budget_default_params(allocation, expected_future_value):
    """
    Test the forecast_budget function with default interest rate and time period.
    """
    future_value = forecast_budget(allocation)
    assert future_value == pytest.approx(expected_future_value, 0.01)


@pytest.mark.parametrize("allocation, interest_rate, expected_future_value", [
    (1000, 0.03, 1030),  # Test case 6: Different interest rate
    (2000, 0.07, 2140),  # Test case 7: Different interest rate
    (1000, 0.08, 1080),  # Test case 8: Different interest rate
])
def test_forecast_budget_custom_interest_rate(allocation, interest_rate, expected_future_value):
    """
    Test the forecast_budget function with custom interest rate.
    """
    future_value = forecast_budget(allocation, interest_rate=interest_rate)
    assert future_value == pytest.approx(expected_future_value, 0.01)


if __name__ == "__main__":
    pytest.main()
