from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import feedparser
import pandas as pd


# -----------User_Authentication-----------------



@csrf_exempt
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            context["error"] = "Provide valid credentials !!!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url="/login/")
def dashboard(request):
    context={'message':'you have been logged successfully'}
    return render(request, "auth/dashboard.html", context)

@login_required(login_url="/login/")
def processRSS(request):
    button = request.POST.get('ProcessRSS')
    feeds = feedparser.parse('http://www.iangels.com/feed/')
    # print(feeds.keys())
    # print(feeds['feed']['title'])
    # print(feeds['entries'][1]['title'])
    print(feeds.items())
    tit = []
    for index, item in enumerate(feeds.entries):
        if index >= 0:
            # print(item.title)
            tit.append(item.title)
    # print(tit)

    lnk = []
    for index, item in enumerate(feeds.entries):
        if index >= 0:
            # print(item.link)
            lnk.append(item.link)

    pDate = []
    for index, item in enumerate(feeds.entries):
        if index >= 0:
            # print(item.published)
            pDate.append(item.published)

    des = []
    for index, item in enumerate(feeds.entries):
        if index >= 0:
            # print(item.description)
            # des.append(item.description)
            soup = BeautifulSoup(item.description)
            texts = soup.find(text=True)
            print(texts)
            b = ''.join(texts)
            # print(b)
            des.append(b)
            print(len(des))
    #
    # print(len(des))
    # print(len(tit))
    # print(len(lnk))
    # print(len(pDate))
    data = {"Title": tit, 'Link': lnk, 'Publish_date': pDate, 'Description': des}
    df = pd.DataFrame(data)
    html = df.to_html()
    # print(df)
    df.to_csv("iangles.csv", index=False)


    file = open("iangles.csv", 'r+')
    fread = file.readlines()

    fnl_feed = []
    for i in fread:
        if "tracked" in i:
            fnl_feed.append(i)

    file2 = open("Fnl_feeds.csv", 'w+')
    file2.writelines(fnl_feed)
    DataFrame = pd.read_csv('iangles.csv')
    return HttpResponse(html)

    # results = pd.DataFrame()
    #
    # response = HttpResponse(content_type='iangles.csv')
    # response['Content-Disposition'] = 'attachment; filename=filename.csv'
    #
    # Response = results.to_csv(path_or_buf=response, sep=';', float_format='%.2f', index=False, decimal=",")
    # return HttpResponse()

def classifier(request):
    return render(request,'classifier.html')

def classifyRSS(request):
    n = request.POST.get('classifierName')
    file = open("iangles.csv", 'r+')
    fread = file.readlines()
    n = input()
    print(n)
    fnl_feed = []
    for i in fread:
        if n in i:
            fnl_feed.append(i)
    data = {'Description': fnl_feed}
    df = pd.DataFrame(data)
    html = df.to_html()
    print(fnl_feed)
    print(len(fnl_feed))
    return HttpResponse(html)



