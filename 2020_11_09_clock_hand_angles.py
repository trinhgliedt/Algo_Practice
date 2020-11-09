# Page 44 algo book
# Clock Hand Angles
# Traditional clocks are increasingly uncommon, but most can still read rotating hands of hours, minutes,
# and seconds.
# Create function clockHandAngles(seconds) that, given the number of seconds since 12:00:00, will
# print the angles (in degrees) of the hour, minute and second hands. As a quick review, there are 360
# degrees in a full arc rotation. Treat “straight-up” 12:00:00 as 0 degrees for all hands.
import math
def clockHandAngles(x):
    rawMins = math.floor(x/60)
    seconds = x%60
    hours = math.floor(rawMins/60)
    mins = rawMins%60
    hAngle = 0; mAngle = 0; sAngle = 0
    hAngle = hours*360/60
    mAngle = mins*360/60
    sAngle = seconds*360/60
    print("hours: ", hours, ", minutes: ", mins, ", seconds: ", seconds);
    print("hAngle: ", hAngle, ", mAngle: ", mAngle, ", sAngle: ", sAngle);
clockHandAngles(53181);