from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
 
monthly_challenges = {
    "january": "Eat no meat for entire month!",
    "february": "walk at leat 20 mint daily",
    "march": "learn django for at 20 mint",
    "april": None,
}
# Create your views here.
# def index(request):
#     return HttpResponse('this works!')
def index(request):
    months = list(monthly_challenges.keys())
    return render(request,'challenges/index.html',{"months":months})
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse('month-challenge',args=[month])
    #     list_items += f"<l1><a href=\"{month_path}\">{capitalized_month}<a/></li><br/>"
    # response_data = f"<ul>{list_items}</ul>"    
    # return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound('invalid month')
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge',args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string('challenges/challenge.html')
        return render(request,'challenges/challenge.html',{'text':challenge_text , "month_name": month.capitalize()})
    except:
        res_data = render_to_string('404.html')
        return HttpResponseNotFound(res_data)    
    # if month=="january":
    #     challenge_text = "Eat no meat for entire month!"
    # elif month=="february":
    #     challenge_text = "walk at leat 20 mint daily"
    # elif month == "march":
    #     challenge_text = "learn django for at 20 mint"    
    # else:
    #     return HttpResponseNotFound('This is not a valid month')        
    # return HttpResponse(response_data)    