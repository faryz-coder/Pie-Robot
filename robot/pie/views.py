from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html")

def direction(request):

    movement = request.POST['UP']


    # def stop():
    #     print("Robot Stop ")
    #     al.off()
    #     af.off()
    #     ar.off()
    #     motorAll.stop()
    #     time.sleep(5)
    #
    # if movement == 'up':
    #     print("Robot Moving Forward ")
    #     af.on()
    #     motorAll.forward(100)
    #     time.sleep(5)
    #     stop()
    #
    # elif movement == 'back':
    #     print("Robot Moving Backward ")
    #     af.off()
    #     ab.on()
    #     motorAll.reverse(100)
    #     time.sleep(5)
    #     stop()
    #
    # elif movement == 'left':
    #     print("Robot Moving Left ")
    #     ab.off()
    #     al.on()
    #     m1.reverse(100)
    #     m2.forward(100)
    #     m3.reverse(100)
    #     m4.forward(100)
    #     time.sleep(5)
    #     stop()
    #
    # elif movement == 'right':
    #     print("Robot Moving Right ")
    #     ar.on()
    #     al.off()
    #     m1.forward(100)
    #     m2.reverse(100)
    #     m3.forward(100)
    #     m4.reverse(100)
    #     time.sleep(5)
    #     stop()

    return HttpResponse('Return data to ajax call')
