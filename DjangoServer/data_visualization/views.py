from django.shortcuts import render
from django.http import HttpResponse


def home(requests):
    f = open("../scanReports/report1.txt")
    scanText = f.read()
    f.close()

    pageText = "<h1> Home page </h1>"

    scanText = scanText.split("\n")
    print(scanText)
    for l in scanText:
        pageText += l+"<br>"
    return HttpResponse(pageText)
