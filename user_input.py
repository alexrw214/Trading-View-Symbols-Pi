import time

def get_lines_params():
	starttime = input("Line start time: ")
	startval = float(input("Line start value: "))
	endtime = input("Line end time: ")
	endval = float(input("Line end value: "))

	return (starttime, startval, endtime, endval)


def get_open_times():
	opentime = input("Hour the market opens (9am is 9). If always open, return \"False\": ")
	if opentime == "False":
		opentime = False
		closetime = False
	else: 
		opentime = int(opentime)
		closetime = int(input("Market close time (5pm is 17): "))


	weekend_close = input("Does this market close on weekends? (True or False): ")
	if weekend_close == "True":
		weekend_close = True
	else:
		weekend_close = False


	holiday_close = input("Does this market close on US Holidays? (True or False): ")
	if holiday_close == "True":
		holiday_close = True
	else:
		holiday_close = False


	return (opentime, closetime, weekend_close, holiday_close)



