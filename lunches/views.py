from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import LunchForm
from .yelp import query_api
from teams.models import Team

@login_required
def create(request, team_slug=None):
    form = LunchForm(request.POST or None)
    if form.is_valid():
        team = Team.objects.get(slug=team_slug)
        lunch = form.save(team=team)
    #     # Add the current user to the team
    #     # Since this is the first user, they will automatically be the admin and owner
    #     team.add_user(request.user)
        return redirect('teams:view', team.slug)
    return render(request, 'lunches/create.html', {'form':form})

def location_search(request, team_slug=None):
    term = request.GET.get('term')
    location = request.GET.get('location')
    print(term, location)
    result = {"results" : [result for result in query_api(term, location)]}
    #result = {"results": [{"is_claimed": True, "url": "https://www.yelp.com/biz/tony-pepperoni-pizzeria-san-diego-2?adjust_creative=QSYD1kvff-x88DS1Yn86cA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_lookup&utm_source=QSYD1kvff-x88DS1Yn86cA", "categories": [{"title": "Pizza", "alias": "pizza"}], "review_count": 38, "display_phone": "(858) 630-8400", "phone": "+18586308400", "alias": "tony-pepperoni-pizzeria-san-diego-2", "transactions": [], "rating": 4.0, "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/JNYpIGiQK2Yj9UEHMUW4kA/o.jpg", "price": "$$", "hours": [{"is_open_now": True, "open": [{"is_overnight": False, "day": 0, "start": "1100", "end": "2200"}, {"is_overnight": False, "day": 1, "start": "1100", "end": "2200"}, {"is_overnight": False, "day": 2, "start": "1100", "end": "2200"}, {"is_overnight": False, "day": 3, "start": "1100", "end": "2200"}, {"is_overnight": False, "day": 4, "start": "1100", "end": "2300"}, {"is_overnight": False, "day": 5, "start": "1100", "end": "2300"}, {"is_overnight": False, "day": 6, "start": "1100", "end": "2200"}], "hours_type": "REGULAR"}], "id": "eLXgZHNfKDHZ011HuLmEcw", "coordinates": {"latitude": 32.99274, "longitude": -117.07007}, "name": "Tony Pepperoni Pizzeria", "photos": ["https://s3-media2.fl.yelpcdn.com/bphoto/JNYpIGiQK2Yj9UEHMUW4kA/o.jpg", "https://s3-media1.fl.yelpcdn.com/bphoto/YjEhOZgLS8Co65gHpLVedQ/o.jpg", "https://s3-media4.fl.yelpcdn.com/bphoto/UjpUgsqtlbuiXVrt_ykwxQ/o.jpg"], "is_closed": False, "location": {"zip_code": "92128", "city": "San Diego", "state": "CA", "address1": "12165 Alta Carmel Ct", "address3": None, "address2": "", "display_address": ["12165 Alta Carmel Ct", "San Diego, CA 92128"], "country": "US", "cross_streets": "Avenida Venusto"}}, {"is_claimed": True, "url": "https://www.yelp.com/biz/coneys-poway-2?adjust_creative=QSYD1kvff-x88DS1Yn86cA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_lookup&utm_source=QSYD1kvff-x88DS1Yn86cA", "categories": [{"title": "Pizza", "alias": "pizza"}], "review_count": 277, "display_phone": "(858) 513-3000", "phone": "+18585133000", "alias": "coneys-poway-2", "transactions": ["delivery", "pickup"], "rating": 4.5, "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/Fkhv5E4KbeAjD-qWVMt1lw/o.jpg", "price": "$", "hours": [{"is_open_now": True, "open": [{"is_overnight": False, "day": 2, "start": "1100", "end": "2000"}, {"is_overnight": False, "day": 3, "start": "1100", "end": "2000"}, {"is_overnight": False, "day": 4, "start": "1100", "end": "2000"}, {"is_overnight": False, "day": 5, "start": "1600", "end": "2000"}, {"is_overnight": False, "day": 6, "start": "1600", "end": "2000"}], "hours_type": "REGULAR"}], "id": "ephBummaBhrMVBV-MpZqPw", "coordinates": {"latitude": 32.9506142708867, "longitude": -117.06613723194}, "name": "Coney's", "photos": ["https://s3-media3.fl.yelpcdn.com/bphoto/Fkhv5E4KbeAjD-qWVMt1lw/o.jpg", "https://s3-media1.fl.yelpcdn.com/bphoto/bs_66toSbU5-uPbG-R6wkQ/o.jpg", "https://s3-media2.fl.yelpcdn.com/bphoto/PuiAmC9o-pXHVdTiC6o_fg/o.jpg"], "is_closed": False, "location": {"zip_code": "92064", "city": "Poway", "state": "CA", "address1": "12233 Poway Rd", "address3": "", "address2": "", "display_address": ["12233 Poway Rd", "Poway, CA 92064"], "country": "US", "cross_streets": "Oak Knoll Rd & Pomerado Rd"}}, {"is_claimed": True, "url": "https://www.yelp.com/biz/flippin-pizza-san-diego-2?adjust_creative=QSYD1kvff-x88DS1Yn86cA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_lookup&utm_source=QSYD1kvff-x88DS1Yn86cA", "categories": [{"title": "Pizza", "alias": "pizza"}], "review_count": 108, "display_phone": "(858) 521-8433", "phone": "+18585218433", "alias": "flippin-pizza-san-diego-2", "transactions": [], "rating": 4.0, "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/ttSUjAlAvcV3-Nu-ErChog/o.jpg", "price": "$", "hours": [{"is_open_now": True, "open": [{"is_overnight": False, "day": 0, "start": "1100", "end": "2100"}, {"is_overnight": False, "day": 1, "start": "1100", "end": "2100"}, {"is_overnight": False, "day": 2, "start": "1100", "end": "2100"}, {"is_overnight": False, "day": 3, "start": "1100", "end": "2100"}, {"is_overnight": False, "day": 4, "start": "1100", "end": "2130"}, {"is_overnight": False, "day": 5, "start": "1100", "end": "2130"}, {"is_overnight": False, "day": 6, "start": "1100", "end": "2100"}], "hours_type": "REGULAR"}], "id": "F6DmIqq_sT0aN109TC8aVQ", "coordinates": {"latitude": 32.98233, "longitude": -117.07531}, "name": "Flippin' Pizza", "photos": ["https://s3-media2.fl.yelpcdn.com/bphoto/ttSUjAlAvcV3-Nu-ErChog/o.jpg", "https://s3-media4.fl.yelpcdn.com/bphoto/yMjUtm7cotA0sg-WYThr8A/o.jpg", "https://s3-media3.fl.yelpcdn.com/bphoto/eC2DUj5ZrGa7uYDNjlb8qw/o.jpg"], "is_closed": False, "location": {"zip_code": "92128", "city": "San Diego", "state": "CA", "address1": "11975 Carmel Mountain Rd", "address3": "", "address2": "Ste 605", "display_address": ["11975 Carmel Mountain Rd", "Ste 605", "San Diego, CA 92128"], "country": "US", "cross_streets": ""}}]}
    return JsonResponse(result, content_type="application/json")