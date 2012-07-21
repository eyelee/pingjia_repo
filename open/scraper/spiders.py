from dynamic_scraper.spiders.django_spider import DjangoSpider
from open.models import Source, Article, ArticleItem,Product,ProductItem,Category,CategoryItem
from open.models import City, CityItem

class ArticleSpider(DjangoSpider):
    
    name = 'article_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Source, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Article
        self.scraped_obj_item_class = ArticleItem
        super(ArticleSpider, self).__init__(self, *args, **kwargs)

        
class ProductSpider(DjangoSpider):
    
    name = 'product_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Source, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Product
        self.scraped_obj_item_class = ProductItem
        super(ProductSpider, self).__init__(self, *args, **kwargs)
        
class CategorySpider(DjangoSpider):
    
    name = 'category_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Source, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Category
        self.scraped_obj_item_class = CategoryItem
        super(CategorySpider, self).__init__(self, *args, **kwargs)

class CitySpider(DjangoSpider):
    
    name = 'city_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Source, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = City
        self.scraped_obj_item_class = CityItem
        super(CitySpider, self).__init__(self, *args, **kwargs)
        
        

        