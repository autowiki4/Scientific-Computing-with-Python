'''The function below is a time calculator which accepts 3 parameters:
    start: the initial time you want to count from
    duration: the number of hours and minutes you want to add to that time
    day: this is an optional variable. this takes in the day of the week when you start this calculation and returns
            the day of the week you arrive at after the calculation.'''
def add_time(start,duration,day='None'): # day is the optional variable

    # Find the porition of the colon in the reported time interval/duration
    colon_original_time = start.index(":")

    # determine what half of the day the time is being reported in
    try:
        end = start.index(" AM")
    except:
        end = start.index(" PM")

    # extract the number of hours from the start time
    hour_original_time = int(start[:colon_original_time])

    #extraxt the number of minutes from the start time
    minute_original_time = int(start[colon_original_time+1:end])

    # Index the colon for the 'duration' variable
    colon_duration = duration.index(":")

    # extract hour from duration variable
    hour_duration = int(duration[:colon_duration])

    # etract minute from duration variable
    minute_duration = int(duration[colon_duration+1:])

    # add the minutes together
    # I used % 60 in the event that the sum of the minutes exceeds 60
    new_minute = (minute_duration + minute_original_time) % 60

    quotient_add = new_minute // 60  # left over hours if sum of minutes exceed 60

    # to display single digit minutes appropriately like a double digit like 08, or 07
    new_minute = f'0{new_minute}' if new_minute <= 9 else new_minute

    # Add the
    new_hour = hour_duration + hour_original_time + quotient_add
    # make adjustments depending on how the time is reported, whether AM or PM to add 12 more hours
    new_hour = new_hour+12 if start[colon_original_time + 4:] == 'PM' else new_hour

    # leftover days is the sum of hours exceeds 24
    leftoverdays = new_hour // 24


    # code to change the day of the week
    dict_days_of_week = {'Sunday': 1,
                         'Monday': 2,
                         'Tuesday': 3,
                         'Wednesday': 4,
                         'Thursday': 5,
                         'Friday': 6,
                         'Saturday': 7
                         }

    # Edit the value entered t=for the 'day' parameter in case the day of the week is not entered correctly like "MonDay".
    def convert_to_proper_name(raw_name):
        # convert all letter to lowercase
        work = raw_name.lower()
        # convert the first letter to uppercase as is stored in my dictionary
        new_name = work[0].upper() + work[1:]
        return new_name


    # the function convert_to_proper_name adjusts the value in case of bizarre typographical inputs like 'mONday'
    day = convert_to_proper_name(day)

    # variable to store the new day of the week after the numerical calculations have been done
    new_day_week = 'Nothing'

    # function to retrieve key of a value to be used shortly
    def get_key(val):
        for key, value in dict_days_of_week.items():
            if val == value:
                return key
            else:
                 pass

    # function to retrieve value of a key to be used later
    def get_value(keys):
        for key, value in dict_days_of_week.items():
            if keys == key:
                return value
            else:
                pass

    # execute this code only if there is a value for the day parameter to prevent errors
    if day != 'None':
        # obtain the corresponding number for the day of the week from the dictionary
        day_number = get_value(day)

        # adjust the corresponding number by adding any days from teh time addition
        new_day = (day_number + leftoverdays) % 7

        new_day_week = get_key(new_day) # obtain the corresponging day of the week aftr the addition
    else:
        pass

    # variable to store the string containing the new_time
    new_time = ''

    new_hour = new_hour % 24
    new_hour = new_hour - 12 if new_hour > 12 else new_hour

    # if tbe day of the week isn't indicated, i.e. it doesn't have a value
    if day != 'None':
        # if more than one day has passed
        if leftoverdays > 1:
            new_time = f'12:{new_minute} AM, {new_day_week} ({leftoverdays} days later)' if new_hour == 0 else f'{new_hour}:{new_minute} PM, {new_day_week} ({leftoverdays} days later)' if new_hour >= 12 else f'{new_hour}:{new_minute} AM, {new_day_week} ({leftoverdays} days later)'
        # not more than one day has gone by
        elif leftoverdays == 1:
            new_time = f'12:{new_minute} AM, {new_day_week} (next day)' if new_hour == 0 else f'{new_hour}:{new_minute} PM, {new_day_week} (next day)' if new_hour >= 12 else f'{new_hour}:{new_minute} AM, {new_day_week} (next day)'
        # a full day hasn't gone by
        elif leftoverdays < 1:
            new_time = f'{new_hour}:{new_minute} PM, {new_day_week}' if new_hour >= 12 else f'{new_hour}:{new_minute} AM, {new_day_week}'

    # if the day parameter has a value, i.e. it has a value
    elif day == 'None':
        # if more than one day has passed
        if leftoverdays > 1:
            new_time = f'12:{new_minute} AM, ({leftoverdays} days later)' if new_hour == 0 else f'{new_hour}:{new_minute} PM, ({leftoverdays} days later)' if new_hour >= 12 else f'{new_hour}:{new_minute} AM, ({leftoverdays} days later)'
        # not more than one day has gone by
        elif leftoverdays == 1:
            new_time = f'12:{new_minute} AM, (next day)' if new_hour == 0 else f'{new_hour}:{new_minute} PM, (next day)' if new_hour >= 12 else f'{new_hour}:{new_minute} AM, (next day)'
            # a full day hasn't gone by
        elif leftoverdays < 1:
            new_time = f'{new_hour}:{new_minute} PM' if new_hour >= 12 else f'{new_hour}:{new_minute} AM'
    return new_time




print(add_time("11:30 AM", "67:32", 'Monday'))
print(add_time("11:06 PM", "68:02"))