#from models import Product
#from django.db.models import Q
from django.shortcuts import render_to_response

def showsvg(maincate='',subcate='',time=''):
    
    # products=Product.objects.filter(Q(title__contains=maincate),Q(title__contains=subcate),meta__contains=time)
    
    #this is a static data collection for testing svg diagram
    data=[{'time':'2003','price':'6800'},
          {'time':'2004','price':'7800'},
          {'time':'2005','price':'8800'},
          #{'time':'2006','price':'9800'},
          #{'time':'2007','price':'10800'},
          {'time':'2008','price':'12600'}
         ]
     
    maxprice=0
    for item in data: 
        price=int(item['price'])
        if price>maxprice:
           maxprice=price
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
    return render_to_response('svg.html',locals())