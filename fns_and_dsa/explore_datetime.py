
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # return it so we can reuse it in the next function

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days and calculates the future date.
    Prints the future date in the format YYYY-MM-DD
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

def main():
    """
    Main function to run the datetime exploration.
    """
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
