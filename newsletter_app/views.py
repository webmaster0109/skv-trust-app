from django.shortcuts import render, redirect
from .models import Newsletter
from django.http import JsonResponse

def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Newsletter.objects.create(email=email, is_subscribed=True, is_active=True)
        return JsonResponse({'message': 'Newsletter subscribed successfully'}, status=200)
    return JsonResponse({'message': 'Invalid request'}, status=400)


