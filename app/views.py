from django.shortcuts import render

# Create your views here. 


from django.http import HttpResponse

def chandu(request):
    return HttpResponse('chandu and shilpa are bestfriends')
