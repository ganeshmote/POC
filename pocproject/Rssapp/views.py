import csv

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Provided_RssLinks, Rssfeedclassifieds, RssDatas, Provided_RssLink
from .serializers import RssTableSerializer, RssTableSerializer1




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
            context["error"] = "Provide valid credentials !!"
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


# @login_required(login_url="/login/")
def rssdata_view(request):
    object=RssDatas.objects.all()
    print(object)
    return HttpResponse(len(object))


def Rssfeedclassified_view(request):
    object=Rssfeedclassifieds.objects.all()
    # serializer=RssTableSerializer1(object,many=True)
    # print(serializer.data)
    return HttpResponse(len(object))

def rssdatadel_view(request):
    object=RssDatas.objects.all().delete()
    print(object)
    return HttpResponse('rssdatadel_view')


def Rssfeedclassifiedsel_view(request):
    object=Rssfeedclassifieds.objects.all().delete()
    print(object)

    return HttpResponse('rssdatadel_view')



def insertDB(request):

    csv_file = 'NEW RSS FEED URL.csv'
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader)
        for row in reader:
            try:
                p = Provided_RssLink(URL = row['URL'],Process_N_Y = row['Process_N_Y'])
                p.save()
            except:
                print("Cannot enter duplicate data")
    return HttpResponseRedirect(reverse('dashboard'))













    # context={'message':'you have been logged successfully'}
    # return render(request, "auth/dashboard.html", context)
# @login_required(login_url="/login/")
# def Rssprocess(request):
#     feeds = feedparser.parse('http://www.iangels.com/feed/')
#     tit = []
#     lnk = []
#     pDate = []
#     des = []
#     super_dict=[]
#     for index,item in enumerate(feeds.entries):
#         if index>=0:
#             data={}
#             tit.append(item.title)
#             lnk.append(item.link)
#             pDate.append(item.published)
#             soup = BeautifulSoup(item.description,features="html.parser")
#             texts = soup.find(text=True)
#             b = ''.join(texts)
#             des.append(b)
#             ########## "Optional part"###########
#             data = {"Title":item.title,'Link':item.link,'Publish_date':item.published,'Description':b}
#             super_dict.append(data)
#             ########## "Optional part"###########
#     data = {"Title":tit,'Link':lnk,'Publish_date':pDate,'Description':des}
#
#     df = pd.DataFrame(data)
#     df["classification"] = "other"
#
#     searchfor1=['fund','raised','funding round','investment','invested','investing','funds','invest','financing rounds']
#     df["classification"][df['Description'].str.contains('|'.join(searchfor1))]="fund"
#
#     searchfor2 = ['merger/s','M&A','acquisition/s ','acquire','acquiring','acquired','sold their company']
#     df["classification"][df['Description'].str.contains('|'.join(searchfor2))]="Merge & Aquistion"
#
#     delete=Rssfeedclassified.objects.all().delete()
#     df.to_csv("iangles.csv",index=False)
#     csv_file = 'iangles.csv'
#     with open(csv_file , encoding="utf8") as csvfile:
#         reader = csv.DictReader(csvfile)
#         print(reader)
#         for row in reader:
#             p = Rssfeedclassified(Title = row['Title'],Link=row['Link'],Description=row['Description'],Publish_date = row['Publish_date'],classification = row['classification'])
#             p.save()
#
#     context={'message':"Rss process and saved data successfully"}
#     return render(request, "auth/dashboard.html", context)







