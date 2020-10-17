from django.shortcuts import render
from django.http import HttpResponse
from pie import PiMotor

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


    def stop():
        print("Robot Stop ")
        al.off()
        af.off()
        ar.off()
        motorAll.stop()
        time.sleep(5)

    if movement == 'up':
        print("Robot Moving Forward ")
        af.on()
        motorAll.forward(100)
        time.sleep(5)
        stop()

    elif movement == 'back':
        print("Robot Moving Backward ")
        af.off()
        ab.on()
        motorAll.reverse(100)
        time.sleep(5)
        stop()

    elif movement == 'left':
        print("Robot Moving Left ")
        ab.off()
        al.on()
        m1.reverse(100)
        m2.forward(100)
        m3.reverse(100)
        m4.forward(100)
        time.sleep(5)
        stop()

    elif movement == 'right':
        print("Robot Moving Right ")
        ar.on()
        al.off()
        m1.forward(100)
        m2.reverse(100)
        m3.forward(100)
        m4.reverse(100)
        time.sleep(5)
        stop()

    return HttpResponse('Return data to ajax call : movement {}'.format(movement))
