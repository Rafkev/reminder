import datetime
import time
import webbrowser

def set_reminder():
    reminder_msg = input("Enter your reminder message: ")
    reminder_time = input("Enter the time for the reminder (format: HH:MM): ")

    try:
        reminder_hour, reminder_minute = map(int, reminder_time.split(':'))
        reminder_datetime = datetime.datetime.now().replace(hour=reminder_hour, minute=reminder_minute, second=0, microsecond=0)
        return reminder_datetime, reminder_msg
    except ValueError:
        print("Invalid time format. Please use HH:MM format.")
        return None, None

def main():
    print("Welcome to Reminder App")
    reminder_datetime, reminder_msg = set_reminder()

    if reminder_datetime and reminder_msg:
        now = datetime.datetime.now()
        while now < reminder_datetime:
            time.sleep(1)
            now = datetime.datetime.now()
        
        print("\nREMINDER:", reminder_msg)
        print("It's time to", reminder_msg)
        webbrowser.open_new_tab('reminder.html')

if __name__ == "__main__":
    main()
