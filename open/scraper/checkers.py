from dynamic_scraper.spiders.django_checker import DjangoChecker
from open.models import Article,Product


class ArticleChecker(DjangoChecker):
    
    name = 'article_checker'
    
    def __init__(self, *args, **kwargs):
        self._set_ref_object(Article, **kwargs)
        self.scraper = self.ref_object.news_website.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.checker_runtime
        super(ArticleChecker, self).__init__(self, *args, **kwargs)
        
class ProductChecker(DjangoChecker):
    
    name = 'product_checker'
    
    def __init__(self, *args, **kwargs):
        self._set_ref_object(Product, **kwargs)
        self.scraper = self.ref_object.prod_website.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.checker_runtime
        super(ProductChecker, self).__init__(self, *args, **kwargs)
        
class CategoryChecker(DjangoChecker):
    
    name = 'category_checker'
    
    def __init__(self, *args, **kwargs):
        self._set_ref_object(Category, **kwargs)
        self.scraper = self.ref_object.prod_website.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.checker_runtime
        super(ProductChecker, self).__init__(self, *args, **kwargs)
        
class CityChecker(DjangoChecker):
    
    name = 'city_checker'
    
    def __init__(self, *args, **kwargs):
        self._set_ref_object(City, **kwargs)
        self.scraper = self.ref_object.prod_website.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.checker_runtime
        super(CityChecker, self).__init__(self, *args, **kwargs)
        
        