import pytest


def forecast_budget(allocation, interest_rate, time_period, compounding_periods=1):
    """
    Calculate the future value of an allocation with a given interest rate
    over a specific time period.

    Parameters:
        allocation (float): The initial amount to be allocated.
        interest_rate (float): The annual interest rate (as a decimal).
        time_period (int): The number of years for which the forecast is to be made.
        compounding_periods (int, optional): The number of times interest is compounded per year. Defaults to 1 (simple interest).

    Returns:
        float: The future value of the allocation.
    """

    if compounding_periods == 1:  # Simple interest
        future_value = allocation * (1 + interest_rate * time_period)
    else:  # Compound interest
        future_value = allocation * (1 + interest_rate / compounding_periods) ** (compounding_periods * time_period)

    return future_value


@pytest.mark.parametrize("allocation, interest_rate, time_period, expected_future_value", [
    (1000, 0.05, 1, 1050),  # Test case 1: Simple interest, 1 year
    (2000, 0.07, 2, 2200),  # Test case 2: Simple interest, 2 years
    (500, 0.03, 3, 542.25),  # Test case 3: Simple interest, 3 years
    (1500, 0.06, 4, 1845.5),  # Test case 4: Simple interest, 4 years
    (3000, 0.08, 5, 3968.25),  # Test case 5: Simple interest, 5 years
])
def test_forecast_budget_simple_interest(allocation, interest_rate, time_period, expected_future_value):
    """Test the forecast_budget function with simple interest."""
    future_value = forecast_budget(allocation, interest_rate, time_period)
    assert future_value == pytest.approx(expected_future_value, 0.01)


@pytest.mark.parametrize("allocation, interest_rate, time_period, compounding_periods, expected_future_value", [
    (1000, 0.05, 1, 4, 1051.27),  # Test case 6: Compound interest quarterly, 1 year
    (2000, 0.07, 2, 12, 2202.08),  # Test case 7: Compound interest monthly, 2 years
    (500, 0.03, 3, 2, 541.67),  # Test case 8: Compound interest semi-annually, 3 years
    (1500, 0.06, 4, 6, 1847.03),  # Test case 9: Compound interest bi-weekly, 4 years
    (3000, 0.08, 5, 3, 3969.19),  # Test case 10: Compound interest annually, 5 years
])
def test_forecast_budget_compound_interest(allocation, interest_rate, time_period, compounding_periods,
                                           expected_future_value):
    """Test the forecast_budget function with compound interest."""
    future_value = forecast_budget(allocation, interest_rate, time_period, compounding_periods)
    assert future_value == pytest.approx(expected_future_value, 0.01)


if __name__ == "__main__":
    pytest.main()
