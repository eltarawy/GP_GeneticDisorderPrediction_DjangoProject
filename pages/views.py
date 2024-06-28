from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'pages/about.html')  

def diseases(request):
    return render(request, 'pages/diseases.html') 
    
def contact(request):
    return render(request, 'pages/contact.html') 

def Cancer(request):
    return render(request, 'pages/Cancer.html') 

def Alzheimer(request):
    return render(request, 'pages/Alzheimer.html') 

def CysticFibrosis(request):
    return render(request, 'pages/CysticFibrosis.html') 

def Diabetes(request):
    return render(request, 'pages/Diabetes.html') 

def Hemochromatosis(request):
    return render(request, 'pages/Hemochromatosis.html') 

def LeberHereditaryOpticNeuropathy(request):
    return render(request, 'pages/LeberHereditaryOpticNeuropathy.html') 

def LeighSyndrome(request):
    return render(request, 'pages/LeighSyndrome.html') 

def MitochondrialMyopathy(request):
    return render(request, 'pages/MitochondrialMyopathy.html') 

def TaySachs(request):
    return render(request, 'pages/TaySachs.html') 

