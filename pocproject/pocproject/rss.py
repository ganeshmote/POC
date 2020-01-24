import csv
import datetime
from datetime import datetime
from bs4 import BeautifulSoup

import feedparser
import pandas as pd
from openpyxl import Workbook
from azureml import Workspace

# def classifier(row):
#         if df[df['Description'].str.contains('billion')]:
#             return "c1"
#
#         else:
#             return "c3"
#
#
# feeds = feedparser.parse('http://www.iangels.com/feed/')
# tit = []
# lnk = []
# pDate = []
# des = []
# for index,item in enumerate(feeds.entries):
#     if index>=0:
#         tit.append(item.title)
#         lnk.append(item.link)
#         pDate.append(item.published)
#         soup = BeautifulSoup(item.description)
#         texts = soup.find(text=True)
#         b = ''.join(texts)
#         des.append(b)
# data = {"Title":tit,'Link':lnk,'Publish_date':pDate,'Description':des}
# print(data)
# df = pd.DataFrame(data)
# df[df['Description'].str.contains('billion')]
# df["D"] = df.apply(classifier)
# print(df)

# print(df)
# df.to_csv("iangles.csv",index=False)



# ws = Workspace(
#     workspace_id='b0f1253516c642b988a3fd2441652f2e',
#     authorization_token='reW4VANmkB58LBp/+4voBHzzLRWsdTr5Iyfo8j6QPzCKbDPN6rUJ6wQdxhuv7MXfMO+VVZfeVfpkPXczUB7LNA==',
#     endpoint='https://studioapi.azureml.net'
# )
# experiment = ws.experiments['b0f1253516c642b988a3fd2441652f2e.f-id.65ab949133894a3e98d8607be6aa5287']
# ds = experiment.get_intermediate_dataset(
#     node_id='a6e02f5b-5d41-4f82-ba92-3fb08f5eade2-1452',
#     port_name='Results dataset',
#     data_type_id='GenericCSV'
# )
# frame = ds.to_dataframe()
#
# print(frame)

# import pandas as pd
# import csv
# from bs4 import BeautifulSoup
# import feedparser
# import os
# rss_feed_urls=['https://www.proactiveinvestors.co.uk/rss/sectorNews/60/rss.xml','https://mnacritique.mergersindia.com/category/m-and-a/feed/', 'https://www.blog.invesco.us.com/feed/']
# # feeds = feedparser.parse('http://www.iangels.com/feed/')
# tit = []
# lnk = []
# pDate = []
# des = []
# super_dict = []
# print(len(rss_feed_urls))
#
# for index,url in enumerate (rss_feed_urls):
#     feeds = feedparser.parse(url)
#
#     for index,item in enumerate(feeds.entries):
#         if index>=0:
#             tit.append(item.title)
#             lnk.append(item.link)
#             date=datetime.strptime(item.published[:-6], '%a, %d %b %Y %H:%M:%S')
#             pDate.append(date)
#             try:
#                 soup = BeautifulSoup(item.description,features="html.parser")
#                 texts = soup.find(text=True)
#                 b = ''.join(texts)
#                 des.append(b)
#             except:
#                 des.append(item.description)
#             data = {"Title":item.title,'Link':item.link,'Publish_date':item.published,'Description':texts}
#             super_dict.append(data)
# datas = {"Title":tit,'Link':lnk,'Publish_date':pDate,'Description':des}
# ########important########pd.concat([df1,df2]).drop_duplicates(keep=False)
# print(len(super_dict))
# df = pd.DataFrame(datas)
#
#
# if not os.path.isfile('filename1.csv'):
#    df.to_csv('filename1.csv', header='column_names')
# else: # else it exists so append without writing the header
#    df.to_csv('filename1.csv', mode='a', header=False)
# df1 = pd.DataFrame(datas)


from datetime import datetime
now = datetime.now()
print(now)
current_time = now.strftime("%H:%M:%S")
print(current_time)
