from django.shortcuts import HttpResponse

def addToOrder(request):
    if request.method == 'POST':
        drinkType = request.POST.get('drink',None)
        print(drinkType)
