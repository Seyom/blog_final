from django.contrib import admin
from django.urls import path, include
import wordcount.urls
import blog.urls
import account.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', blog.views.list, name='list'),
    path('blog/', include(blog.urls)),
    path('wordcount/', include(wordcount.urls)),
    path('account/', include(account.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)