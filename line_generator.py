def date_dict_gen(starttime, startval, endtime, endval, opentime, closetime, weekend, holiday_close):

    
    from datetime import datetime, timedelta
    from dateutil import parser
    import time
    import holidays
    

    us_holidays = holidays.UnitedStates()
    starttime = parser.parse(starttime)
    endtime = parser.parse(endtime)
    
    #list of datetimes in range
    datelist = []

    #Dictionary to create price thresholds for datetimes
    date_dict = {}

    #Time to iterate starts at starttime
    temptime = starttime

    while not temptime > endtime:
        
        #Take into account weekdays into timeline
        #weekend = True means closed on weekends
        if weekend and (temptime).isoweekday() not in range(1,6):
            temptime += timedelta(hours=1)

        #Check if ticker is open during day 
        elif opentime and temptime.hour not in range(opentime,closetime):
            temptime += timedelta(hours=1)

        #Close on US holidays
        #holiday_close = True means closed on US Holidays
        elif holiday_close and (temptime in us_holidays):
            temptime += timedelta(hours=1)

        #If valid time, append to datelist and increment a minute
        else:
            datelist.append(temptime)
            temptime += timedelta(minutes=1)
            
    for i in range(0,len(datelist)):
        date_dict[datelist[i]] =round(startval + i*(endval-startval)/len(datelist),2) 
            
    return date_dict