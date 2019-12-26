from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('master/<int:id>', views.master, name='master'),
]
