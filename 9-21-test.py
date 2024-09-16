# Control Program for the 9-21 GNC Test.
# Tests include:
# Test 1 (Equality test) - Open both nozzles and record acceleration to see if thrust is equal (specifically data[6])
# Test 2 (Left thrust test) - Open left valve for 1 second and record what happens. 
# Test 3 (Right thrust test)  - Open right valve for 1 second and record what happens
# Test 4 (Full use) - open one valve and let it use all air in tank, measure time and accel data
# Extra test - Test PID and try to tune


import time
import RPi.GPIO as GPIO
from BMI160_i2c import Driver

# Initialize the sensor
print('Trying to initialize the sensor...')
sensor = Driver(0x68) # change address if needed
print('Initialization done')

# Initialize the relays
relay1 = 16 # assuming left
relay2 = 15 # assuming right

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)

#--------------------------------
# 
# Test Functions
# 
#--------------------------------

# Test 1 - Equality test
# Open both nozzles and record acceleration to see if thrust is equal (specifically data[6])
# Will write data to test_data/both.csv
# Format: nozzle 1 state, nozzle 2 state, time, data[6]
def test1():
    # Create test file
    file = open("test_data/both.csv","w")
    
    # Fire both nozzles for 5 seconds and record data
    start_time = time.time()
    
    GPIO.output(relay1, GPIO.HIGH)
    GPIO.output(relay2, GPIO.HIGH)
    
    while time.time() - start_time < 5:
        data = sensor.getMotion6()
        file.write(f"{GPIO.input(relay1)},{GPIO.input(relay2)},{time.time()-start_time},{data[6]}\n")
        time.sleep(0.1)

    # Close the file
    GPIO.output(relay1, GPIO.LOW)
    GPIO.output(relay2, GPIO.LOW)
    file.close()

# Test 2 - Left thrust test
# Open left valve for 1 second and record what happens.
# Will write data to test_data/left.csv
# Format: nozzle 1 state, time, data[6]

def test2():
    # Create test file
    file = open("test_data/left.csv","w")
    
    # Power relay 1 for 1 second and record data
    start_time = time.time()
    
    GPIO.output(relay1, GPIO.HIGH)
    
    while time.time() - start_time < 1:
        data = sensor.getMotion6()
        file.write(f"{GPIO.input(relay1)},{time.time()-start_time},{data[6]}\n")
        time.sleep(0.1)

    # Close the file
    GPIO.output(relay1, GPIO.LOW)
    file.close()
    
# Test 3 - Right thrust test
# Open left valve for 1 second and record what happens.
# Will write data to test_data/right.csv
# Format: nozzle 1 state, time, data[6]
    
def test3():
    # Create test file
    file = open("test_data/right.csv","w")
    
    # Power relay 2 for 1 second and record data
    start_time = time.time()
    
    GPIO.output(relay2, GPIO.HIGH)
    
    while time.time() - start_time < 1:
        data = sensor.getMotion6()
        file.write(f"{GPIO.input(relay2)},{time.time()-start_time},{data[6]}\n")
        time.sleep(0.1)

    # Close the file
    GPIO.output(relay2, GPIO.LOW)
    file.close()


# Main control Loop
if __name__ == "main":
    print(r"""\ 
            ______  _______  ______        __    _____          __           __
           / ___/ |/ / ___/ /_  __/__ ___ / /_  / ___/__  ___  / /________  / /
          / (_ /    / /__    / / / -_|_-</ __/ / /__/ _ \/ _ \/ __/ __/ _ \/ / 
          \___/_/|_/\___/   /_/  \__/___/\__/__\___/\___/_//_/\__/_/  \___/_/  
         | | / /__ _______ (_)__  ___    <  // _ \                           
         | |/ / -_) __(_-</ / _ \/ _ \   / // // /                           
         |___/\__/_/ /___/_/\___/_//_/  /_(_)___/                            
                                                                     """)
