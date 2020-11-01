from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def select(requests):
    if requests.method == "GET":
        return render(requests,"data_select.html")