Assessing Water Quality through Turbidity:

The homework03 directory consists of two Python3 files: analyze_water.py and test_analyze_water.py.

analyze_water.py: The first script reads from a given water quality data set (a .json file) and prints:
1) The current average water turbidity of the most recent five measurements
2) If the current turbidity is above or below the safe threhold for use
3) The minimum time required to return below a safe threshold (if the current turbidity is above it)
Note: If the current turbidity is already below the safe threshold, the minimum time defaults to 0.

test_analyze_water.py: The second script has unit tests that tests two functions in analyze_water.py that perform simple sanity checks to make sure the the math and/or output type is correct. 
Function 1, turbidity(a0,I90): This function calculates turbidity in NTU units (0 - 40) by multiplying the calibration constant, a0, and the ninety degree detector current, I90.
Function 2, minimum_time(Ts,T0,d): This function calculates the minimum time required to return below a safe threshold with the following equation: Ts > T0(1-d)**b [b = log(Ts/T0)/log(1-d)] where
	Ts = Turbidity threshold for safe water
	T0 = Current turbidity
	d = Decay factor per hour, expressed as a decimal
	b = Hours elapsed	  

This folder exists to simulate a realistic problem/situation in an aerospace setting for checking precautions in order to eliminate risks and promote safety. 

In order to run the code, insert into the command line from Linux:
1) python3 analyze_water.py (to print the information explained above)
2) pytest test_analyze_water.py (to check individual functions)

Example Output:

$ python3 analyze_water.py
Average turbidity based on most recent five measurements = 1.1566 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 7.20 hours


$ pytest test_analyze_water.py
========================================================= test session starts =========================================================
platform linux -- Python 3.8.10, pytest-7.2.1, pluggy-1.0.0
rootdir: ...
collected 2 items                                                                                                                     

test_analyze_water.py ..                                                                                                        [100%]

========================================================== 2 passed in 0.07s ==========================================================

