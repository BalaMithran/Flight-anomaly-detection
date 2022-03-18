from FlightRadar24.api import FlightRadar24API

fr_api = FlightRadar24API()
import time

dict = {}
flightid = []
flightslope = {}

for _ in range(10):
    flights = fr_api.get_flights()
    for flight in flights:
        flightid.append(flight.id)
        if flight.id in dict.keys():
            current_obs = int(flight.get_altitude().split(" ")[0])
            if dict[flight.id]["data"][-1] != current_obs:
                if dict[flight.id]["data"][-1] > current_obs:
                    slope = -1
                    if dict[flight.id]["curr_slope"] != slope:
                        dict[flight.id]["changes"] += 1
                        dict[flight.id]["curr_slope"] = slope
                else:
                    slope = 1
                    if dict[flight.id]["curr_slope"] != slope:
                        dict[flight.id]["changes"] += 1
                        dict[flight.id]["curr_slope"] = slope
                dict[flight.id]["data"].append(current_obs)
                dict[flight.id]["data"].append(current_obs)
        else:
            # dict[flight.id] = [0, 0, int(flight.get_altitude().split(" ")[0])]
            dict[flight.id] = {"curr_slope": 0, "changes": 0, "data": [int(flight.get_altitude().split(" ")[0])]}
    time.sleep(1)

for id in dict.keys():
    if dict[id]["changes"] > 1:
        print(id, dict[id])


# output sample format
# 2b2e3168 {'curr_slope': -1, 'changes': 2, 'data': [36000, 36025, 36025, 36000, 36000]}
# 2b2e31fd {'curr_slope': -1, 'changes': 2, 'data': [30950, 30975, 30975, 30950, 30950]}
# 2b2e323a {'curr_slope': 1, 'changes': 2, 'data': [30000, 29975, 29975, 30000, 30000]}
# 2b2e326e {'curr_slope': -1, 'changes': 4, 'data': [36000, 36025, 36025, 36000, 36000, 36025, 36025, 36000, 36000]}
# 2b2e33eb {'curr_slope': 1, 'changes': 2, 'data': [38025, 38000, 38000, 38025, 38025]}
# 2b2e33f3 {'curr_slope': -1, 'changes': 2, 'data': [37975, 38000, 38000, 37975, 37975]}
# 2b2e353e {'curr_slope': -1, 'changes': 2, 'data': [37975, 38000, 38000, 37975, 37975]}
# 2b2e354e {'curr_slope': -1, 'changes': 3, 'data': [33025, 33000, 33000, 33025, 33025, 33000, 33000]}
# 2b2e35ae {'curr_slope': 1, 'changes': 2, 'data': [36000, 35975, 35975, 36000, 36000]}
# 2b2e36af {'curr_slope': 1, 'changes': 2, 'data': [3615, 3572, 3572, 3395, 3395, 3392, 3392, 3402, 3402, 3405, 3405, 3421, 3421]}
# 2b2e36b2 {'curr_slope': -1, 'changes': 2, 'data': [33000, 33025, 33025, 33000, 33000]}
# 2b2e376a {'curr_slope': 1, 'changes': 3, 'data': [34575, 34600, 34600, 34575, 34575, 34600, 34600]}
