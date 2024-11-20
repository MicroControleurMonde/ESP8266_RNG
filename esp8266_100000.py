import esp8266_rng_lib
import utime
import time

# Function to display the current time
def display_current_time():
    # Get the local time from the system clock
    current_time = time.localtime()  # Retrieve local time (struct_time format)
    
    # Manually format the hour, minute, and second
    hour = current_time[3]
    minute = current_time[4]
    second = current_time[5]
    
    # Display the time in the format: HH:MM:SS
    formatted_time = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    print("Time", formatted_time)

print("Starting the generator")
# Display the current time every second
display_current_time()

# Create an instance of RandomGenerator
rng = esp8266_rng_lib.RandomGenerator()

# Number of random numbers to generate
num_random_numbers = 100000
block_size = 10000  # Block size (10,000 values)

# Open a file to save the random numbers
file_name = 'esp8266_rng.txt'
with open(file_name, 'w') as f:
    # Measure the start time
    start_time = utime.ticks_ms()

    # Generate random numbers and write them to the file
    for i in range(num_random_numbers):
        random_number = rng.generate()
        f.write(f"{random_number}\n")

        # Display a message every 10,000 numbers generated
        if (i + 1) % block_size == 0:
            print(f"Block of {block_size} numbers generated (total {i + 1} out of {num_random_numbers})")

    # Measure the end time
    end_time = utime.ticks_ms()

# Calculate the elapsed time in seconds
elapsed_time_ms = utime.ticks_diff(end_time, start_time)
elapsed_time_s = elapsed_time_ms / 1000.0

# Calculate the throughput in bytes per second
# Each random number generated is a 64-bit integer (8 bytes)
total_bytes = num_random_numbers * 8  # 8 bytes per number
bytes_per_second = total_bytes / elapsed_time_s

# Display the results
print(f"Time taken to generate {num_random_numbers} random numbers: {elapsed_time_s:.2f} seconds")
print(f"Random number generation rate: {bytes_per_second:.2f} bytes per second")
print("Stopping the generator")
display_current_time()
