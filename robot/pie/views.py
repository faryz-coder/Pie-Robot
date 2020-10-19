from django.shortcuts import render
from django.http import HttpResponse
from pie import PiMotor
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

TRIG = 29
ECHO = 31

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#Name of Individual MOTORS
m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)

#Names for Individual Arrows
ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3)
ar = PiMotor.Arrow(4)
# Create your views here.


def home(request):
    return render(request, "home.html")

def direction(request):

    movement = request.POST['UP']
    stopDistance = 5
    sleepDuration = 1.5

    def ultra():
        t = True
        distance = 0
        count=0
        while t:
         i=0
         avgDistance=0
         for i in range(5):
            GPIO.output(TRIG, False)
            time.sleep(0.1)

            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            while GPIO.input(ECHO)==0:
                pulse_start = time.time()

            while GPIO.input(ECHO)==1:
                pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start

                distance = (pulse_duration * 34300)/2
                distance = round(distance,2)
                avgDistance=avgDistance+distance

                avgDistance=avgDistance/5
                distance = int(avgDistance)
                t = False
        return distance

    def stop():
        print("Robot Stop ")
        al.off()
        af.off()
        ar.off()
        motorAll.stop()
        time.sleep(sleepDuration)

    if movement == 'up' and ultra() > stopDistance:
        print("Robot Moving Forward ")
        af.on()
        motorAll.forward(100)
        time.sleep(sleepDuration)
        stop()

    elif movement == 'back':
        print("Robot Moving Backward ")
        af.off()
        ab.on()
        motorAll.reverse(100)
        time.sleep(sleepDuration)
        stop()

    elif movement == 'left':
        print("Robot Moving Left ")
        ab.off()
        al.on()
        m1.reverse(100)
        m2.forward(100)
        m3.reverse(100)
        m4.forward(100)
        time.sleep(sleepDuration)
        stop()

    elif movement == 'right':
        print("Robot Moving Right ")
        ar.on()
        al.off()
        m1.forward(100)
        m2.reverse(100)
        m3.forward(100)
        m4.reverse(100)
        time.sleep(sleepDuration)
        stop()

    return HttpResponse('{}'.format(ultra()))
