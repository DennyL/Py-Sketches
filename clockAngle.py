def clockAngle(time: str) -> int:
    """
       calculates the angle between hour-arrow
       and minute-arrow of the clock face
       given the time
       by D.L.
    """

    time = time.split(":")
    hour, minute = int(time[0]), int(time[1])

    assert hour < 24 and minute < 60, "Wrong time"

    # firstly, let's make our code independent on
    # the time system (24-hour, 12-hour) the user may choose

    if hour >= 12:
        hour -= 12
            
    # Let's make some preliminary calculations first:
    # The angle between hour marks on the clock face is
    # 30 degrees (360 degrees / 12 hours).
    # Thus, minute-arrow does 6 degree per minute (30 degrees / 5).
    # While minute-arrow makes full circle (360d) per hour,
    # hour-arrow is also moving, although falling behind it,
    # making 30 degrees per hour.
    # This delta between the two arrows may be described as 30/360.
    # Now we can calculate, how many degrees arrows do
    # in relation to one another due to the time given.

    delta = 30 / 360
    angle_minute = minute * 6
    angle_hour = (hour * 30) + (delta * minute)

    return abs(angle_minute - angle_hour)
    

print(clockAngle("12:30"))
