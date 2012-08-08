#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from models import Category,Product
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponse
from django.utils import simplejson
from django.shortcuts import render_to_response
from function import Average,Normalprice
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def ajax_match(request):
    success = False
    to_return = {'msg':u'No POST data sent.' }
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('kw'):
            kw = post['kw']
            categories=Category.objects.filter(name__icontains=kw)[0:10]
            values=[]
            for item in categories:
                values.append(item.name)
            to_return["values"]=values
            success=True
        else:
            to_return['msg'] = u"Requires keywords"
    serialized = simplejson.dumps(to_return)
    if success == True:
        return HttpResponse(serialized, mimetype="application/json")
    else:
        return HttpResponseServerError(serialized, mimetype="application/json")
    
def search(request):
    if request.method=="GET":
        get=request.GET.copy()
        if get.has_key("kw"):
            kw=get['kw'].strip()
            if kw:
                kws=re.split(r'\s+',kw)
                #kws=re.split(r'[^\w\x80-\xff]+',kw)
                kws=list(set(kws))
                if kws.count(''):
                    kws.remove('')
                    #return HttpResponse(kws)
                if kws:
                    products=Product.objects.all()
                    #products.query.group_by = ['time']  
                    for item in kws:
                        products=products.filter(title__contains=item)
                    #products=products.exclude(time="车商店铺")
                         
                    products=products.order_by('-time')[0:50]  
                    products_dict=[]
                    for item in products: 
                        product=model_to_dict(item)
                        products_dict.append(product)
                    products=products_dict
                    excerpt_products= products[0:5]
                    #return HttpResponse(products)
                    if len(products):
                        return render_to_response("search.html",locals())
                    else:
                        return render_to_response("nothingfound.html",locals())      
                else:
                    return render_to_response("nothingfound.html",locals())
            else:
                return HttpResponseRedirect('/')
            
        
