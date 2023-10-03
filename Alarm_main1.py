import datetime
import time
import winsound  #for windows

def set_alarm():
    try:
        # Input alarm time from the user
        alarm_hour = int(input("Enter the alarm hour (0-23): "))
        alarm_minute = int(input("Enter the alarm minute (0-59): "))

        # Validate user input
        if 0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59:
            return alarm_hour, alarm_minute
        else:
            print("Invalid input. Please enter a valid time.")
            return set_alarm()
    except ValueError:
        print("Invalid input. Please enter a valid time.")
        return set_alarm()

def alarm_clock(alarm_hour, alarm_minute):
    while True:
        now = datetime.datetime.now()
        current_hour, current_minute = now.hour, now.minute

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Time to wake up!")
            play_alarm_sound()  # You can replace this with your preferred alarm action
            break
        else:
            time.sleep(60)  # Check the time every 60 seconds

def play_alarm_sound():
    # Play a sound as the alarm
    try:
        # You can replace the file path with your preferred alarm sound
        winsound.PlaySound("path_to_sound_file.wav", winsound.SND_FILENAME)
    except Exception as e:
        print("Failed to play alarm sound:", str(e))

if __name__ == "__main__":
    print("Welcome to Python Alarm Clock")
    alarm_hour, alarm_minute = set_alarm()
    print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")
    alarm_clock(alarm_hour, alarm_minute)
