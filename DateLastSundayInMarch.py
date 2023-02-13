import time

def last_sunday_of_march(year):
    # Calculate the timestamp for March 31st of the current year
    t = time.mktime((year, 3, 31, 0, 0, 0, 0, 0, 0))
    # Use the localtime function to get the weekday of March 31st
    wday = time.localtime(t)[6]
    # Subtract the weekday from March 31st to get the timestamp for the last Sunday of March
    t = t - (6 - wday) * 24 * 60 * 60
    # Use the localtime function to get the date of the last Sunday of March
    date = time.localtime(t)[:3]
    return date

# Get the current year
year = time.localtime()[0]

# Call the last_sunday_of_march function to get the date of the last Sunday of March of the current year
date = last_sunday_of_march(year)

# Print the date
print("Last Sunday of March %d: %d-%02d-%02d" % (year, date[0], date[1], date[2]))

