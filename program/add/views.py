from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    a = ""
    b = ""
    total = 0
    if request.GET:
        a = int(request.GET["a"])
        b = int(request.GET["b"])
        opt = request.GET["name"]
        print(opt)
        if opt == "ADD":
            total = a - b
        if opt == "SUB":
            total = a - b
        if opt =="MUL":
            total = a * b
        if opt =="DIV":
            total = a / b

        print(total)
    return render(request, "add.html", {'a': a, 'b': b, 'total': total,'add':add})

