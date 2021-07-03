from django.shortcuts import render
from django.http import HttpResponse ,Http404, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
monthly_challenge={'january':"do not eat non vage for one month",'february': "walk at least 20 min a day",'march':None }
# Create your views here.
def index(request):
    month=list(monthly_challenge.keys())
    return render(request,"challenges/index.html",{"months":month})
    






def monthly_challengeby_number(request, month):
    months=list(monthly_challenge.keys())
    if month > len(months):
        raise Http404()
    redirect_month = months[month-1]
    redirect_value=reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_value)

def monthly_challenges(request,month):
     try:
        challenge_text=monthly_challenge[month]
        response_data=render(request,"challenges/challenge.html",{"month_name":month,"task":challenge_text})
        return HttpResponse(response_data)
     except:
        raise Http404()


                  

    


