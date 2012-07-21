from django.contrib import admin
from open.models import Source, Article,Product,Category,City

class SourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_', 'scraper')
    list_display_links = ('name',)
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'source', 'url_','description','thumbnail')
    list_display_links = ('title',)
    raw_id_fields = ('checker_runtime',)
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'source', 'url_','meta','time','price','year')
    list_filter = ('source','time','year')
    #list_display = ('id', 'title', 'prod_website','time','price')
    list_display_links = ('title',)
    raw_id_fields = ('checker_runtime',)
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','source', 'slug', 'url_','parent')
    list_filter = ('parent','source')
    #list_display = ('id', 'title', 'prod_website','time','price')
    list_display_links = ('name',)
    raw_id_fields = ('checker_runtime',)
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True
    
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','prod_website', 'slug', 'url_','parent')
    list_filter = ('parent','source')
    #list_display = ('id', 'title', 'prod_website','time','price')
    list_display_links = ('name',)
    raw_id_fields = ('checker_runtime',)
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True

admin.site.register(Source, SourceAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(City,CategoryAdmin)
