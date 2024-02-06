# Purdue Orbital 🪐 Launch Stabilization Structure 

### Python Scripts

There are a few python scripts stored in `/prototype-python`. 

1. `imu-test.py` simply connects to the IMU and gathers and prints acceleration and gyro data to the console.
2. `imu-visual.py` connects to the IMU, reads data, and plots it on a graph to visually represent the data and the physical motion of the IMU.

### Guide

To get the above scripts up and running, follow these steps.

**Materials:** 
- [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) (We are using a Raspberry Pi 3b+, but most should work).
- [BMI160 IMU](https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi160/), you can find these on Amazon as well.
- Some [female-to-female jumper wires](https://www.amazon.com/GenBasic-Piece-Female-Jumper-Wires/dp/B01L5ULRUA?th=1).

**Dependencies:**
- `python3 -m pip install BMI160-i2c`
- `python3 -m pip install smbus2`

**Steps**

1. Run `git clone https://github.com/mattallenn/gnc.git` in your directory of choice.
2. Wire up the components. Connect the 3.3V, GND, SCL, SDA, and SAO (to ground) from the IMU to the corresponding IO pins on the raspberry pi.
3. Run `i2cdetect -y 1`. This should show a connection on `0x68` or `0x69`. You'll have to change the variable at the top of the `.py` files to
make sure this is correct.
4. Run either `python3 imu-test.py` or `python3 imu-visual.py`
5. Congratulation! Go drink because you now have some useful(?) data from a cheap, inaccurate Amazon clone IMU that probably won't work tomorrow.

## Credits:
A lot of this was adapted / taken from [this](https://pypi.org/project/BMI160-i2c/) python package.
