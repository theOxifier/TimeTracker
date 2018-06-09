#!/usr/bin/env python3.4
import sys
import pprint as pp
import collections

def time_split_to_int( time_str ):
    '''Split up the time string to a list in the format of [hr, min]
    in interger format

    Args: 
        time_str: time in 24:00 format as a string

    Returns:
        split_time: list of time in [hr,min]

    Raises:
        none
    '''

    hour = time_str.split(":")[0]
    minute = time_str.split(":")[1]
    time_list = [hour, minute]
    return time_list

def main():

    week = {}

    week_count = 1 
    week.update(
        {"week" + str(week_count):
            { "monday":[]
            , "tuesday":[]
            , "wednesday":[]
            , "thursday":[]
            , "friday":[]
            }
        }
    )


    # Temp window for testing
    while True:
        day_of_week = input("Enter day of the week: ")
        day_of_week = day_of_week.lower()
        #arrival = time_split_to_int( input("Enter arrival time (24-hr): "))
        #leave = time_split_to_int(input("Enter leave time (24-hr): "))
        arrival = time_split_to_int("8:00")
        leave = time_split_to_int("16:00")

        day = [arrival, leave]
        week["week"+str(week_count)].update({day_of_week:day})
        #pp.pprint(week,width=10)
        pp.pprint(week)

        if day_of_week.lower() == "friday":
            week_count += 1
            week.update({"week" + str(week_count):{}})

        # Test of time split function
        #time_list = time_split_to_int("8:00")
        #print("time split up {} : {}".format(time_list[0], time_list[1]))

if __name__ == '__main__':
    main()