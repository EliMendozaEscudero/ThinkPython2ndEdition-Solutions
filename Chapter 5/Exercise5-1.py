import time

def seconds_to_dhms(only_seconds):
    """It converts n seconds to its equivalent
    in  days + hours + minutes + seconds
    only_seconds: The time only using seconds.""" 
    days=divide_and_subtract(only_seconds,86400)#86400 is the total amount of seconds in a day.
    hours = divide_and_subtract(days[1],3600)#3600 is the total amount of seconds in an hour
    minutes  = divide_and_subtract(hours[1],60)
    seconds = minutes[1]
    return str(days[0])+" days "+str(hours[0])+" hours "+ str(minutes[0])+" minutes {:.3g} ".format(seconds)+"seconds."

    
def divide_and_subtract(dividend, divisor):
    """It returns the result of dividend // divisor
    and the result of  dividend % divisor"""
    return int(dividend//divisor), dividend%divisor

if __name__ == '__main__':
    current_time = time.time()
    print("Time since epoch:",seconds_to_dhms(current_time))  