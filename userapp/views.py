#import json
#from pickle import NONE
from django.shortcuts import redirect
from django.http import JsonResponse
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import pandas as pd


#from . import EmailService,SendSMS
#import bcrypt
#import uuid,os
from django.shortcuts import render
#from .models import Employee,AllCities,AllInstitute
# Create your views here.
from sqlalchemy import create_engine
import schedule
import time
from userapp.models import LiveQuotes, User, NonAgro
import re

import numpy as np



def trendline(index,data, order=1):
     coeffs = np.polyfit(index, list(data), order)
     slope = coeffs[-2]
     return float(slope)

# index=[1,2,3,4]
# List=[1043,6582,5452,7571]
# resultent=trendline(index,List)
# print(resultent)  


def algo(request):
 
      data= LiveQuotes.objects.filter(pname='Jeera')
      dataoi=data.values_list('oi')
      datasp=data.values_list('spot_price')
      
      c= 1
      q=[]
      idx=[]
      print (dataoi)
      print(datasp)
      for i in dataoi:
        idx.append(c)
        c+=1
      
      oi =trendline(idx, dataoi)
      sp=trendline(idx, datasp)

      print(oi)
      print(sp)
      if(oi>=0):
        oi_trend=1
      else:
         oi_trend=0

      if(sp>=0):
        sp_trend=1
      else:
         sp_trend=0
      
      if(oi_trend==1 and sp_trend==0):
        print("increase in weakness")

      elif(oi_trend==1 and sp_trend==1):
        print("strong increase")
      
      elif(oi_trend==0 and sp_trend==1):
         print("short covering")
      
      else:
          print("long unbinding")

      return HttpResponse("trend detection algorithm")

      #return render(request,"table.html" ,  {'data': datab})


        

def Login(request):
   # try:
    #    result = request.session['ADMIN']
     #   return render(request,'Login.html')

        # return redirect("admin-dashboard")
    #except Exception as e:
        # print("Err",e)
        # return redirect("admin-dashboard")

        return HttpResponse("helllooo")


def display ():
   URL = "https://ncdex.com/market-watch/live_quotes"
   r = requests.get(URL)
   soup = BeautifulSoup(r.content, 'html5lib')

   table = soup.find('table')
   tr=table.find_all('tr')

   print("test1")

   c=0

   for i in tr:
      c=c+1

      if(c>2):
         td=i.find_all('td')


         pname=td[0].text.strip()
         expdate=td[1].text
         open=float(re.sub("[^0-9]", "", td[1].text))
         li=td[3].find_all('li')
         low=float(re.sub("[^0-9]", "", li[0].text))
         ltp=float(re.sub("[^0-9]", "", li[1].text))
         high=float(re.sub("[^0-9]", "", li[2].text))
         close=float(re.sub("[^0-9]", "", td[4].text))
         change=float(td[5].text.replace(',', ''))
         change_per=float(td[6].text.replace(',', ''))
         avtp=float(re.sub("[^0-9]", "", td[7].text))
         spot_price=float(re.sub("[^0-9]", "", td[1].text))
         sp_dt=td[9].text
         best_buy=float(re.sub("[^0-9]", "", td[10].text))
         best_sell=float(re.sub("[^0-9]", "", td[11].text))
         oi=int(td[12].text.replace(',', ''))
         graph=td[13].text


         data=LiveQuotes.objects.create(pname=pname, expiry_date=expdate, open=open, low=low,ltp=ltp,high=high,close=close, change=change, change_percentage=change_per, avtp=avtp,spot_price=spot_price, sp_date_time=sp_dt, best_buy=best_buy,best_sell=best_sell,oi=oi, graph=graph )
         data.save()

   print("append")


def non_agro():


   URL = "https://www.mcxdata.in/"
   r = requests.get(URL)
   soup = BeautifulSoup(r.content, 'html5lib')

   table = soup.find('table')
   tr=table.find_all('tr')

   c=0
   for i in tr:

      if(c!=0 and c!=6 and c!=14):
         td=i.find_all('td')
         print(i.text)
         commodity=td[0].text.strip()
         price=float(re.sub("[^0-9]", "", td[1].text))
         change=float(td[2].text.replace(',', ''))
         change_per=float(td[3].text.replace(',', ''))
         open=float(re.sub("[^0-9]", "", td[4].text))
         high=float(re.sub("[^0-9]", "", td[5].text))
         low=float(re.sub("[^0-9]", "", td[6].text))
         time=td[7].text

         data=NonAgro.objects.create(commodity=commodity, price=price, change=change, change_per=change_per, open=open, high=high, low=low, time=time)
         data.save()

      c+=1
         


def home(request):
 

   print("append")
   non_agro()
   return HttpResponse("jejjfiji")
   # schedule.every(1).minutes.do(display)
   # while True:
   #    schedule.run_pending()
   #    time.sleep(1)


def non_agrolist(request):
   datab= NonAgro.objects.all().order_by('-id_na')[:10]

   return render(request,"table2.html" ,  {'data': datab})



def live_quotes(request):
      datab= LiveQuotes.objects.all().order_by('-idlive_quotes')[:10]

      return render(request,"table.html" ,  {'data': datab})


# Create your views here.
