# Get the current time in seconds since the epoch
current_time = time.time()

# Convert a timestamp to a local time object
local_time = time.localtime(current_time)

# Format the local time object into a string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

# Parse a string representing a time into a local time object
parsed_time = time.strptime("2023-03-08 14:30:00", "%Y-%m-%d %H:%M:%S")

# Suspend the execution of the current thread for 5 seconds
time.sleep(5)
