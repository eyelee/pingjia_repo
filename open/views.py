from models import Category
from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponse
from django.utils import simplejson

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