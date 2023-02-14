from analyze_water import turbidity, minimum_time 
import pytest

"""
These unit tests are designed to test the individual functions for analyzing water with simple constructs.
"""

def test_turbidity():
    # Check if function calculates turbidity by multiplying calibration constant and detector current with expected outcomes (int and float)
    assert turbidity(3,7) == 21
    assert turbidity(2.74,6) == 16.44


def test_minimum_time():
    # Check if function calculates the minimum time with expected outcome 
    assert minimum_time(10,1,-9) == 1

    # Check if function calculates the minimum time as type float
    assert isinstance(minimum_time(2,7,0.05), float) == True

