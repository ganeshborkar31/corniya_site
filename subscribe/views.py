from django.shortcuts import render, redirect
from .forms import SubscriptionForm

def under_construction(request):
    message = ""
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Thank you! We will notify you when the site is ready."
        else:
            message = "This email is already subscribed."
    else:
        form = SubscriptionForm()

    return render(request, 'subscribe/under_construction.html', {'form': form, 'message': message})
