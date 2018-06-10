#!/usr/bin/env python3.4
import sys
import pprint as pp
import collections


def split_time(time_str):
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

class Week:
    def __init__(self,number=0):
        self._week = { "monday":{"arrival":[],"lunch_start":[],"lunch_end":[],"departure":[]},
                      "tuesday":{"arrival":[],"lunch_start":[],"lunch_end":[],"departure":[]},
                    "wednesday":{"arrival":[],"lunch_start":[],"lunch_end":[],"departure":[]},
                     "thursday":{"arrival":[],"lunch_start":[],"lunch_end":[],"departure":[]},
                       "friday":{"arrival":[],"lunch_start":[],"lunch_end":[],"departure":[]}
            }
        self.week_number = number
    
    def get_week(self):
        return self._week
    
    def get_day(self,day):
        print("arrival \t= {}\nlunch_start \t= {}\nlunch_end \t= {}\ndeparture \t= {}\n".format(
            self._week[day]["arrival"],
            self._week[day]["lunch_start"],
            self._week[day]["lunch_end"],
            self._week[day]["departure"])
            )
        #return self._week[day]

    def get_week_num(self):
        return self.week_number

    def set_week_num(self, number):
        self.week_number = number
    
    def set_arrival(self, day, time):
        self._week[day]["arrival"] = split_time(time)


    #def set_lunch_start(self, day, time):
    #def set_lunch_end(self, day, time):
    #def set_departure(self, day, time):
    

    
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
        #arrival = split_time( input("Enter arrival time (24-hr): "))
        #leave = split_time(input("Enter leave time (24-hr): "))
        arrival = split_time("8:00")
        leave = split_time("16:00")

        day = [arrival, leave]
        week["week"+str(week_count)].update({day_of_week:day})
        #pp.pprint(week,width=10)
        pp.pprint(week)

        if day_of_week.lower() == "friday":
            week_count += 1
            week.update({"week" + str(week_count):{}})

        # Test of time split function
        #time_list = split_time("8:00")
        #print("time split up {} : {}".format(time_list[0], time_list[1]))

if __name__ == '__main__':
    main()
