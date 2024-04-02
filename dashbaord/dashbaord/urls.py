from django.contrib import admin
from django.urls import path, include  # Make sure to import include
from django.conf.urls.static import static  # Import static
from django.conf import settings  # Import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/', include('teacher.urls')),  # Add this line
    path('student/', include('student.urls')),  # Add this line

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
