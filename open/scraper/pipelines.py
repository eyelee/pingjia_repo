from django.db.utils import IntegrityError
from scrapy import log
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime
from open.models import ArticleItem

class DjangoWriterPipeline(object):
    
    def process_item(self, item, spider):
        try:
            #spider.log("item class is: %s" % item)
            #if (item == ArticleItem):
                #item['news_website'] = spider.ref_object
            #else:
            item['source'] = spider.ref_object
            
            checker_rt = SchedulerRuntime(runtime_type='C')
            checker_rt.save()
            item['checker_runtime'] = checker_rt
            
            item.save()
            spider.action_successful = True
            spider.log("Item saved.", log.INFO)
            
                
        except IntegrityError, e:
            spider.log(str(e), log.ERROR)
            raise DropItem("Missing attribute.")
                
        return item