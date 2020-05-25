
from django.contrib import admin
from django.urls import path,include
import wordcount.urls
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wordcount/',include(wordcount.urls)),

    path('',list, name="list"),
    path('blog/<int:blog_id>',detail, name = "detail"),
    path('blog/new',new, name = "new"),
    path('blog/create',create, name = "create"),
    path('blog/edit/<int:blog_id>',edit, name = "edit"),
    path('blog/update/<int:blog_id>',update, name = "update"),
    path('blog/delete/<int:blog_id>',delete, name = "delete")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
