import machine
import time

# Define GPIO pins for trigger and echo
trigger_pin = machine.Pin(2, machine.Pin.OUT)
echo_pin = machine.Pin(3, machine.Pin.IN)

def get_distance():
    # Triggering the ultrasonic sensor
    trigger_pin.off()
    time.sleep_us(2)
    trigger_pin.on()
    time.sleep_us(10)
    trigger_pin.off()
    
    # Measuring the time for the echo
    while echo_pin.value() == 0:
        pulse_time = time.ticks_us()
    
    while echo_pin.value() == 1:
        end_time = time.ticks_us()
    
    # Calculating distance in centimeters
    pulse_duration = end_time - pulse_time
    distance_cm = (pulse_duration * 0.0343) / 2
    
    return distance_cm

try:
    while True:
        distance = get_distance()
        print("Distance:", distance, "cm")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Measurement stopped by user")
