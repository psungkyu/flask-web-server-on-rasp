import RPi.GPIO as GPIO
import time

def led_dimming(led_pin):
    print(led_pin)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    pwm = GPIO.PWM(led_pin, 1000)

    try:
        pwm.start(0)
        for duty_cycle in range(0, 101):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.01)

        for duty_cycle in range(100, -1, -1):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.01)
            
    finally:
        pwm.stop()
        GPIO.cleanup()
