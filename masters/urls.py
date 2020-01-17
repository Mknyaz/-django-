from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('master/<int:pk>', views.master, name='master'),
    # path('master-list/', views.master_list, name='master_list'),
]
