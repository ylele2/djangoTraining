from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
'''
def january(request):
    return HttpResponse("This is January Month")

def february(request):
    return HttpResponse("This is February Month")
'''
monthly_challenges = {
    "january": "This is january!!",
    "february": "This is february!!",
    "march": "This is march!!",
    "april": "This is april!!",
    "may": "This is may!!",
    "june": "This is June!!",
    "july": "This is july!!",
    "august": "This is august!!",
    "september": "This is september!!",
    "october": "This is october!!",
    "november": "This is november!!",
    "december": "This is december!!",
    "adhik": "This is Adhikmas"

}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    no = 1
    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li>{no}<a href=\"{month_path}\"> {capitalize_month} </a></li>"
        no += 1
    response_data = f"<ul> {list_items} </ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    # /challenges/january
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This is not a valid month</h1>")
