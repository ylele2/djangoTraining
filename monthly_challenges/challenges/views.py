from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
'''
def january(request):
    return HttpResponse("This is January Month")

def february(request):
    return HttpResponse("This is February Month")
'''
monthly_challenges ={
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
    "december": "This is december!!"

}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/"+redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This is not a valid month")
    
