# Import the datetime module
from datetime import datetime, timedelta

# Get the current date and time
current_datetime = datetime.now()

# Display the current date and time
print("Current date and time:", current_datetime)

# Display only the current date
print("Current date:", current_datetime.date())

# Display only the current time
print("Current time:", current_datetime.time())

# Add 5 days to the current date
future_date = current_datetime + timedelta(days=5)
print("Date after 5 days:", future_date.date())

# Subtract 3 days from the current date
past_date = current_datetime - timedelta(days=3)
print("Date 3 days ago:", past_date.date())
