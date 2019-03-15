from datetime import datetime, timedelta
from dateutil import parser
import time
import sys
from os import system, name 
from line_generator import date_dict_gen
from user_input import get_lines_params, get_open_times
from get_tradingview_values import get_values
from emailalert import email_alert

#TradingviewAlerts92@gmail.com TradingviewAlerts9294

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')   

def clear_and_print(u_starttime, u_startval, u_endtime, u_endval, l_starttime, l_startval, l_endtime, l_endval, opentime, closetime, weekend_close, holiday_close):
 	
	clear()
	print("Symbol: "+symbol.upper())
	print("\nUpper line info...")
	print("Line start time: "+str(u_starttime))
	print("Line start value: "+str(u_startval))
	print("Line end time: "+str(u_endtime))
	print("Line end value: "+str(u_endval))
	print("\nLower line info...")
	print("Line start time: "+str(l_starttime))
	print("Line start value: "+str(l_startval))
	print("Line end time: "+str(l_endtime))
	print("Line end value: "+str(l_endval)+"\n")
	if opentime:
		print("Market open from %s:00 to %s:00." % (str(opentime), str(closetime)))
	else:
		print("Market has no closing time.")
	if weekend_close:
		print("Market open on weekends.")
	else:
		print("Market closed on weekends.")
	if holiday_close:
		print("Market closed on US Holidays.")
	else:
		print("Market open on US Holidays.") 


symbol = input("Symbol: ").title()
opentime, closetime, weekend_close, holiday_close = get_open_times()

print("\nUpper line info...")
u_starttime, u_startval, u_endtime, u_endval = get_lines_params()
upper_bound_line = date_dict_gen(u_starttime, u_startval, u_endtime, u_endval, opentime, closetime, weekend_close, holiday_close)

print("\nLower line info...")
l_starttime, l_startval, l_endtime, l_endval = get_lines_params()
lower_bound_line = date_dict_gen(l_starttime, l_startval, l_endtime, l_endval, opentime, closetime, weekend_close, holiday_close)


#Initial state of values and times
currval = get_values(symbol)
currtime = datetime.now().replace(second=0, microsecond=0)
currtime += timedelta(hours=4)

print("Current value of "+symbol.upper()+": ", currval)

#While market closed, do this loop
while (currtime not in upper_bound_line) or (currtime not in lower_bound_line):
	clear_and_print(u_starttime, u_startval, u_endtime, u_endval, l_starttime, l_startval, l_endtime, l_endval, opentime, closetime, weekend_close, holiday_close)
	sys.stdout.write("\n")

	for i in range(1,8):
		sys.stdout.write("Waiting for market to open"+"."*i+"\r")
		sys.stdout.flush()
		time.sleep(2)
	currtime = datetime.now().replace(second=0, microsecond=0)
	currtime += timedelta(hours=4)

upper_curr_bound_val = upper_bound_line[currtime]
lower_curr_bound_val = lower_bound_line[currtime]


#Monitoring values over time
while (currval < upper_curr_bound_val) or (currval > lower_curr_bound_val):
	while (currtime not in upper_bound_line) or (currtime not in lower_bound_line):
		clear_and_print(u_starttime, u_startval, u_endtime, u_endval, l_starttime, l_startval, l_endtime, l_endval, opentime, closetime, weekend_close, holiday_close)
		sys.stdout.write("\n")

		for i in range(1,8):
			sys.stdout.write("Waiting for market to open"+"."*i+"\r")
			sys.stdout.flush()
			time.sleep(2)
		currtime = datetime.now().replace(second=0, microsecond=0)
		currtime += timedelta(hours=4)

	clear_and_print(u_starttime, u_startval, u_endtime, u_endval, l_starttime, l_startval, l_endtime, l_endval, opentime, closetime, weekend_close, holiday_close)

	print("\nCurrent value of "+symbol.upper()+": ", currval)
	print("Current upper boundary value: ", upper_curr_bound_val)
	print("Current lower boundary value: ", lower_curr_bound_val)
	print("Current time is: "+str(currtime-timedelta(hours=4))+" ET ("+str(currtime)+" UTC)")


	if (currval > upper_curr_bound_val):
		print("\n\nAt "+str(currtime-timedelta(hours=4))+" ET, "+symbol.upper()+" rose above the target price line.")
		email_alert(symbol.upper(), currval, currtime, upper_curr_bound_val, lower_curr_bound_val)
		break
	if (currval < lower_curr_bound_val):
		print("\n\nAt "+str(currtime-timedelta(hours=4))+" ET, "+symbol.upper()+" fell below the target price line.")
		email_alert(symbol.upper(), currval, currtime, upper_curr_bound_val, lower_curr_bound_val)
		break
	time.sleep(60)

	currval = get_values(symbol)
	currtime = datetime.now().replace(second=0, microsecond=0)
	currtime += timedelta(hours=4)

