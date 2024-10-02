from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formated_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formated_date}")
display_current_datetime()

from datetime import datetime, timedelta

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

calculate_future_date()

