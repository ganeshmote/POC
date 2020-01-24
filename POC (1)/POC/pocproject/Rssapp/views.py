from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import *
from .forms import *
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import json
import os
import csv


# ------------User_Authentication-----------------
from .serializers import RssTableSerializer


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
    print(feeds.items())
    tit = []
    lnk = []
    pDate = []
    des = []
    for index, item in enumerate(feeds.entries):
        if index >= 0:
            # append RSS title to list
            tit.append(item.title)
            # append RSS link to list
            lnk.append(item.link)
            # append RSS published date to list
            pDate.append(item.published)
            # pre-process Rss text and then append to list
            soup = BeautifulSoup(item.description)
            texts = soup.find(text=True)
            print(texts)
            b = ''.join(texts)
            des.append(b)

    data = {"Title": tit, 'Link': lnk, 'Publish_date': pDate, 'Description': des}
    df = pd.DataFrame(data)
    df["classification"] = "other"

    searchfor1 = ['fund', 'raised', 'funding round', 'investment', 'invested', 'investing', 'funds', 'invest',
                  'financing rounds']
    df["classification"][df['Description'].str.contains('|'.join(searchfor1))] = "fund"

    searchfor2 = ['merger/s', 'M&A', 'acquisition/s ', 'acquire', 'acquiring', 'acquired', 'sold their company']
    df["classification"][df['Description'].str.contains('|'.join(searchfor2))] = "Merge & Aquistion"

    delete = Rssfeedclassified.objects.all().delete()
    df.to_csv("iangles.csv", index=False)
    csv_file = 'iangles.csv'
    with open(csv_file, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader)
        for row in reader:
            p = Rssfeedclassified(Title=row['Title'], Link=row['Link'], Description=row['Description'],
                                  Publish_date=row['Publish_date'], classification=row['classification'])
            p.save()

    context = {'message': "Rss process and saved data successfully"}
    return render(request, "auth/dashboard.html", context)
    # html = df.to_html()
    # data = json.dumps([data])
    # # serializer = RssTableSerializer(data=data)
    # # if serializer.is_valid():
    # #     serializer.save()
    # df.to_csv("iangles.csv", index=False)
    # return HttpResponse(html)

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

def getData(request):
    a = Rss_Table.objects.values('Title','Link','Publish_date')
    l = []
    for i in a:
        l.append(i)
    # data = {'Title':l}
    df = pd.DataFrame(l)
    html = df.to_html()
    paginator = Paginator(html, 5)
    pg1 = paginator.page(1)


@login_required(login_url="/logout/")
def index(request):
    rss_list = Rss_Table.objects.all()
    paginator = Paginator(rss_list, 10)  # Show 10 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Process_rss.html', {'page_obj': page_obj})


def my_view(request):
    a = Rss_Table.objects.all()
    for i in a:
        print(i)
        response = serializers.serialize("json", a)
        return HttpResponse(response,content_type='application/json')

def get_data(request):
    rss_list = Rss_Table.objects.all()

    paginator = Paginator(rss_list, 1)

    page = request.GET.get('page')
    Rss_Feeds = paginator.get_page(page)
    qs_json = serializers.serialize('json', Rss_Feeds)
    json_data = json.loads(qs_json)
    return HttpResponse(json_data)


def rss_details (request,id=None):
    context={}
    context['user']=get_object_or_404(Rss_Table,id=id)
    return render(request, 'details.html', context)


def insertDB(request):
    # twitters=twitter.objects.all().delete()
    csv_file = 'iangles.csv'
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader)
        for row in reader:
            p = Rss_Table(Title = row['Title'],Link=row['Link'],Publish_date = row['Publish_date'],Created_at = row['Created_at'])
            p.save()
    return HttpResponse('INserted to DB')

@login_required(login_url="/login/")
def Rss_feed_edit(request, id=None):
    user = get_object_or_404(Rss_Table, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            # return HttpResponse('Edited Successfully!!!')
            return HttpResponseRedirect(reverse('get_data'))
        else:
            return render(request, 'edit.html', {"user_form": user_form})
    else:
        user_form = UserForm(instance=user)
        return render(request, 'edit.html', {"user_form": user_form})



def back_to_feedlist(request):
    return HttpResponseRedirect(reverse('dashboard'))


def json_response(request):
    rss = Rssfeedclassified.objects.filter(Description__contains = 'raised').order_by('-Publish_date')
    rss_list = serializers.serialize('json',rss)
    return HttpResponse(rss_list,content_type="text/json-comment-filtered")


def dashboard1(request):
    object=RssData.objects.all()
    print(object)
    return HttpResponse(len(object))


