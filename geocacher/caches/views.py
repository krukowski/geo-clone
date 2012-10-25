from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from caches.models import Cache, Log, CacheForm, LogForm
from django.contrib.auth.decorators import login_required

@login_required
def add_cache(request):
    if request.method == 'POST':
        form = CacheForm(request.POST)
        cache = form.save(commit=False)
        cache.created_by = request.user
    return render(request, 'caches/create.html', {'form':CacheForm()})

