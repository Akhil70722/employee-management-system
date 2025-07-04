# """
# URL configuration for config project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# # from django.contrib import admin
# # from django.urls import path

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# # ]


from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Employee Management System API")

urlpatterns = [
    path('', home),  # Root path: http://127.0.0.1:8000/
    
    # Admin panel
    path('admin/', admin.site.urls),
    
    # All API endpoints grouped under /api/
    path('api/', include('employees.urls')),  # /api/employees/
    
    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh
    
    # DRF's browsable API login/logout
    path('api-auth/', include('rest_framework.urls')),
]
