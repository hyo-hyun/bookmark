#뷰를 만들었으면 어떤 주소를 사용해 이 뷰를 호출할 수 있도록 연결해야 함. 즉. 어떤 주소를 입력했을 때 해당 페이지를 보여주고 싶은 가를 설정하는 것.


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('bookmark/', include('bookmark.urls')),
    path('admin/', admin.site.urls),
]
