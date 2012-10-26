from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from caches.models import Cache, Log, CacheForm, LogForm
from django.contrib.auth.decorators import login_required
from simplejson import dumps
import math

@login_required
def add_cache(request):
    message = ''
    if request.method == 'POST':
        form = CacheForm(request.POST)
        try:
            cache = form.save(commit=False)
        
            cache.created_by = request.user
            cache.save()
            return HttpResponseRedirect('cache/'+str(cache.pk))
        except ValueError, e:
            message = 'Invalid entry.'
    return render(request, 'caches/create.html', {'form':CacheForm(), 'message':message})

def home(request):
    return render(request, 'caches/index.html')

def cache_list(request):
    return render(request, 'caches/cache_list.html')

def cache_ajax(request):
    # This is certainly not scalable the way it is.
    caches = list(Cache.objects.all())
    print len(caches)
    if "radius" in request.GET.keys():
        radius = request.GET.get("radius")
        lat = request.GET.get("lat")
        lon = request.GET.get("long")
        try:
            radius = float(radius)
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            radius = lat = lon = None
        if radius:
            caches = filter(lambda c: distance([c.lat, c.lon],[lat,lon]) <= radius,
                            caches)
    print len(caches)
    for c in caches:
        print c.size
    acceptable_sizes = []
    for s in ["small","medium","large"]:
        if request.GET.get(s):
            acceptable_sizes += [str.upper(s[0])]
    print acceptable_sizes
    caches = filter(lambda c: c.size in acceptable_sizes, caches)
    caches = map(lambda c: {'name':c.title, 'pk':c.pk, 'user':c.created_by.username, 
                            'size':c.size, 'lat':c.lat, 'long':c.lon}, caches)

    return HttpResponse(dumps({'caches':caches}))

def distance(origin, destination):
    # from http://www.platoscave.net/blog/2009/oct/5/calculate-distance-latitude-longitude-python/
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 3963 # miles

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def view_cache(request, id):
    cache = Cache.objects.get(pk=id)
    return render(request, 'caches/view_cache.html', {'cache':cache})
