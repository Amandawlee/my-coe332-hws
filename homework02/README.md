The Random Generation of Five Meteor Landing Sites:

The homework02 directory consists of two Python files: generates_sites.py and calculate_trip.py. 
	generate_sites.py: The first script randomly chooses five latitudes, five longitudes, and five\
	meteorite compositions (stony, iron, and stony-iron) to simulate five meteorite landing sites\
	in Syrtis Major for a robotic vehicle on Mars. It then generates this information in a\
	dictionary with one key word, "sites", and saves this data to a .json file. 

	calculate_trip.py: The second script reads the five meotorite landing sites from the .json file\
	and calculates the times it takes for the robotic vehicle to travel to the meteorite and the time\
	it takes to get samples from the five sites (in order). 

This folder exists to simulate a realistic problem/situation in an aerospace setting which is important\
in calculating hypothetical time intervals given known information before an actual project occurs.

In order to run the code, insert into the command line from Linux:
1) python3 generate_sites.py (to generate a .json file with 5 randomly calculated meteorite landing sites)
2) python3 calculate_trip.py (to calculate time to travel from initial point to each site, time to take\
samples from sites, and total time elapsed from all five trips) 

Example Output:
leg = 1, time to travel = 13.29 hr, time to sample = 2 hr
leg = 2, time to travel = 8.75 hr, time to sample = 1 hr
leg = 3, time to travel = 4.8 hr, time to sample = 2 hr
leg = 4, time to travel = 15.05 hr, time to sample = 1 hr
leg = 5, time to travel = 13.66 hr, time to sample = 1 hr
===============================
number of legs = 5, total time elapsed = 62.55 hr

The legs represent each trip taken (calculated).
