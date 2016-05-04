from django.conf.urls import url
from snippets import views
from version1.views import index, streamgraph, radialboxplot, linegraph, overview, scatterplot

urlpatterns = [
    #url(r'version1/$', index),
    url(r'version1/scatterplot', scatterplot),
    url(r'version1/streamgraph', streamgraph),
    url(r'version1/radialboxplot', radialboxplot),
    url(r'version1/linegraph', linegraph),
    url(r'version1/overview', overview),
    url(r'version1/home', index),
    url(r'version1/', index),

]


