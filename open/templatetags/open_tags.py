#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import re
from django import template
from open.function import Average,Normalprice,Normdistribution
register = template.Library()

@register.inclusion_tag("includes/svgrect.html", takes_context=True)
def showrect(context):
    """
    show svg rect diagram.
    """
    #context["products"] = BlogPostForm()
    data=[{'time':'2003','price':'6800'},
          {'time':'2004','price':'7800'},
          {'time':'2005','price':'8800'},
          {'time':'2006','price':'9800'},
          {'time':'2007','price':'10800'},
          {'time':'2008','price':'12600'}
         ]
    price=[]
    for item in data: 
        price.append(int(item['price']))
    maxprice=max(price)
    svgheight=200
    svgwidth=378
    time_relative=15
    price_relative=-5
    rectwidth=40
    x_relative=18 
    k=float(svgheight*0.9)/float(maxprice)
    rect_x_position=29
    time_x_position=34
    price_x_position=31
    for item in data:
        item['rectheight']=k*float(item['price'])
        item['rect_y_position']=svgheight-item['rectheight']
        item['time_y_position']=item['rect_y_position']+time_relative
        item['price_y_position']=item['rect_y_position']+price_relative
        item['rect_x_position']=rect_x_position
        item['time_x_position']=time_x_position
        item['price_x_position']=price_x_position
        rect_x_position+=rectwidth+x_relative
        time_x_position+=rectwidth+x_relative
        price_x_position+=rectwidth+x_relative
    result={}
    result['svgwidth']=svgwidth
    result['svgheight']=svgheight
    result['rectwidth']=rectwidth
    result['data']=data
    return result

@register.inclusion_tag("includes/svgcircle.html", takes_context=True)
def showcircle(context):
    dateformat='%Y年%m月%d日'
    data=context['products']
    product={}
    products=[]
    for item in data:
        product={}
        if not re.search('^\d+月\d+日$',item['time']):
            continue
        product['time']=time.strftime('%Y',time.gmtime())+'年'+item['time']
        if item['price'] is None:
            continue
        if Normalprice(item['price']) is None:
            continue
        product['price']=Normalprice(item['price'])
        products.append(product)
    data=products
    svgheight=280
    svgwidth=378
    maxprice_height=250
    first_x_position=20
    last_x_position=358
    first_y_position=10
    price=[]
    date=[]
    for item in data: 
        price.append(float(item['price']))
        timestamp=time.mktime(time.strptime(item['time'],dateformat))
        date.append(timestamp)
    maxprice=max(price)
    maxdate=max(date)
    mindate=min(date)
    kx=float(last_x_position-first_x_position)/float(maxdate-mindate)
    ky=float(maxprice_height)/float(maxprice)
    for key,item in enumerate(data):
        item['circle_x_position']=first_x_position+kx*(date[key]-mindate)
        item['circle_y_position']=first_y_position+ky*float(item['price'])
    length=len(data)
    center_point=int(length/2)
    if length<4:
        quater_point=0
        quater_to_point=length-1 
    else:
        quater_point=int(length/4)
        quater_to_point=int(0.75*length)
    average_line_x1=first_x_position+kx*(date[quater_point]-mindate)
    average_line_y1=first_y_position+ky*float(Average(price[:center_point]))
    average_line_x2=first_x_position+kx*(date[quater_to_point]-mindate)
    average_line_y2=first_y_position+ky*float(Average(price[center_point:]))
    k_average=(average_line_y2-average_line_y1)/(average_line_x2-average_line_x1)
    average_line_y1=average_line_y1-k_average*(average_line_x1-first_x_position)
    average_line_x1=first_x_position
    average_line_y2=average_line_y2+k_average*(last_x_position-average_line_x2)
    average_line_x2=last_x_position
    datepoints=[]
    for i in range(1,12,3):
        datepoint_x=first_x_position+kx*(i*(maxdate-mindate)/11)
        datepoint_str=time.strftime('%m/%d/%y',time.gmtime(i*(maxdate-mindate)/11+mindate))
        datepoint=dict(datepoint_x=datepoint_x,datepoint_str=datepoint_str)
        datepoints.append(datepoint)
    result={}
    result['svgwidth']=svgwidth
    result['svgheight']=svgheight
    result['datepoints']=datepoints
    result['data']=data
    result['average_line_x1']=average_line_x1
    result['average_line_x2']=average_line_x2
    result['average_line_y1']=average_line_y1
    result['average_line_y2']=average_line_y2
    return result

@register.inclusion_tag("includes/svgpath.html", takes_context=True)
def showpath(context):
    data=[{'time':'2005/7/10','price':'6800'},
          {'time':'2005/7/15','price':'6800'},
          {'time':'2005/8/5','price':'7600'},
          {'time':'2005/8/10','price':'7800'},
          {'time':'2005/8/13','price':'7900'},
          {'time':'2005/9/10','price':'8900'},
          {'time':'2005/9/13','price':'7800'},
          {'time':'2005/9/23','price':'6800'},
          {'time':'2005/10/12','price':'7800'},
          {'time':'2005/10/16','price':'7500'},
          {'time':'2005/11/20','price':'8800'},
          {'time':'2005/11/20','price':'8800'},
          {'time':'2005/12/17','price':'9800'},
          {'time':'2006/1/19','price':'10800'},
          {'time':'2006/1/20','price':'12600'},
          {'time':'2006/1/28','price':'9800'},
          {'time':'2006/2/14','price':'8900'},
          {'time':'2006/2/17','price':'8800'},
          {'time':'2006/3/11','price':'9200'},
          {'time':'2006/3/17','price':'9200'},
          {'time':'2006/3/21','price':'9200'},
         ]
    price=[]
    price_infos=[]
    svgheight=200
    svgwidth=378
    maxheight=180
    first_x_position=25
    last_x_position=340
    center_x_position=189
    for item in data:
        price.append(int(item['price']))
    #unique_price=list(set(price))
    #unique_price.sort()
    #for item in unique_price:
        #pricenum=price.count(item)
        #price_info=dict(price=item,pricenum=pricenum)
        #price_infos.append(price_info)
    average_price=Average(price)
    min_price=min(price)
    points=[]
    for point_x in range(center_x_position,last_x_position,16):
        point_y=Normdistribution(point_x ,u=center_x_position)
        point=dict(point_x=point_x,point_y=point_y)
        points.append(point)
    for point_x in range(first_x_position,center_x_position,16):
        point_y=Normdistribution(point_x ,u=center_x_position)
        point=dict(point_x=point_x,point_y=point_y)
        points.append(point)
    points.sort()
    for point in points:
        point['tag']='L'
    points[0]['tag']='M'
    result={}
    result['svgwidth']=svgwidth
    result['svgheight']=svgheight
    result['points']=points
    return result

@register.simple_tag
def price_range(datalist):
    if not datalist:
        return
    price=[]
    for item in datalist:
        if item['price'] is None:
            continue
        if Normalprice(item['price']) is None:
            continue
        price.append(Normalprice(item['price']))
    if price:
        average_price=Average(price)
        if len(price)<2:
            max_price=price[0]
            min_price=price[0]
        elif len(price)<5:
            price.append(average_price)
            price.sort()
            center=price.index(average_price)
            min_price=price[center-1]
            max_price=price[center+1]
        elif len(price)>4:
            price.append(average_price)
            price.sort()
            center=price.index(average_price)
            min_price=price[center-2]
            max_price=price[center+2]
        return '￥'+str(min_price)+'-￥'+str(max_price)
            
@register.simple_tag
def show_normalprice(price):
    if price is None:
        return
    if Normalprice(price) is None:
        return
    return Normalprice(price) 

@register.simple_tag
def average_price(datalist):
    if not datalist:
        return
    price=[]
    for item in datalist:
        if item['price'] is None:
            continue
        if Normalprice(item['price']) is None:
            continue
        price.append(Normalprice(item['price']))
    if price:
        average_price=Average(price)
        return average_price