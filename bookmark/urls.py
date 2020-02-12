from django.urls import path
from .views import BookmarkListView,BookmarkCreateView,BookmarkDetailView,BookmarkUpdateView,BookmarkDeleteView


urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    #앞쪽인 int는 타입, 즉 컨버터 뒤쪽은 컨버터를 통해 반환받은 값 혹은 패턴에 일치하는 값의 변수명
]
#BookmarkListView 라는 뷰를 호출하겠다는 의미
#함수 형 뷰라면 뷰 이름만 써주면 되지만 클래스 형 뷰일 경우 뒤에 .as_view() 를 붙여줘야 정상적으로 동작함.