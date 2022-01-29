import winsound
from datetime import datetime as dt


def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid TIME Format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR Format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE Format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND Format! Please try again..."
        else:
            return "ok"


while True:
    alarm_time = input('Enter time in "HH:MM:SS AM/PM" format: ')

    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

while True:
    now = dt.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("WAKE UP!!!!!!!!!")
                    winsound.PlaySound('C:\\Users\\AY\\Downloads\\alarm_clock.wav', winsound.SND_FILENAME)
                    break
