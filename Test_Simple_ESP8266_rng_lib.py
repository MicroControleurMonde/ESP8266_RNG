# Import library and classes
import esp8266_rng_lib

# Create an instance of RandomGenerator
rng = esp8266_rng_lib.RandomGenerator()

# Generate a random number
random_number = rng.generate()

# Display the random number generated
print(random_number)
