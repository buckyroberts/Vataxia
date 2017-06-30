from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls


urlpatterns = [

    # API (v1)
    url(r'^', include('v1.accounts.urls')),
    url(r'^', include('v1.credits.urls')),
    url(r'^', include('v1.posts.urls')),
    url(r'^', include('v1.private_messages.urls')),
    url(r'^', include('v1.replies.urls')),
    url(r'^', include('v1.user_roles.urls')),
    url(r'^', include('v1.votes.urls')),

    # Core
    url(r'^admin/', admin.site.urls),
    url(r'^', include_docs_urls(title='Vataxia')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
