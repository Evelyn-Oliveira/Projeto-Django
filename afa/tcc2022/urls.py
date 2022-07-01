from django.urls import path
from .views import index, logar, refreshbd, showdataform, showchoicejobs, sendresults, confirmchoices
from .views.getjobs import getjobs, getabstract, getsubarea
#from .views.showchoicejobs import deletetrabs
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
  path('',index,name='index'),
  path('login/',logar,name='login'),
  path('refreshbd/',refreshbd,name='refreshbd'),
  path('showdataform/',showdataform,name='showdataform'),
  path('showdataform/getjobs/<int:id>', getjobs, name='getjobs'),
  path('showdataform/getsubarea/<int:id>', getsubarea, name='getsubarea'),
  path('showdataform/getabstract/<int:id>', getabstract, name='getabstract'), 
  path('showchoicejobs/',showchoicejobs,name='showchoicejobs'),
  path('showchoicejobs/<int:id>',showchoicejobs, name='showchoicejobs'),
  path('sendresults/',sendresults,name='sendresults'),
  path('sendresults/<int:id>',sendresults, name='sendresults'),
  path('confirmchoices/',confirmchoices,name='confirmchoices'),
]

urlpatterns += staticfiles_urlpatterns()