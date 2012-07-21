from celery.task import task

from dynamic_scraper.utils.task_utils import TaskUtils
from open.models import Source, Product
#from open_news.models import Article,

@task()
def run_spiders():
    t = TaskUtils()
    t.run_spiders(Source, 'scraper', 'scraper_runtime', 'product_spider')
    
#@task()
def run_checkers():
    t = TaskUtils()
    t.run_checkers(Product, 'source__scraper', 'checker_runtime', 'product_checker')



#this is for test purpose 
from celerytest.models import Counter   
@task()
def add(x):
    if Counter.objects.count()==0:
        counter= Counter()
        counter.seq=1
    else:
        counter=Counter.objects.filter(id=1)[0]
        counter.seq+=x
    counter.save()
    return counter.seq
