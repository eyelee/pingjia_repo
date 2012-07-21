from celery import task
from models import Counter

#@task()
def add(x):
    if Counter.objects.count()==0:
        counter= Counter()
        counter.seq=1
    else:
        counter=Counter.objects.filter(id=1)[0]
        counter.seq+=x
    counter.save()
    return counter.seq

