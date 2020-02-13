
from django.views.generic.list import ListView
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark
#북마크 앱은 전형적인 뷰들이 필요하기 때문에 클래스 형 뷰가 적절함.
#BookmarkListView 라는 이름으로 클래스 형 뷰를 만듦. ListView 를 상속해 사용


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    #fields 변수는 어떤 필드들을 입력받을 것인지 설정하는 부분
    success_url = reverse_lazy('list')
    #success_url은 글쓰기를 완료하고 이동할 페이지
    template_name_suffix = '_create'
    #template_name_suffix 는 사용할 템플릿의 접미사만  변경하는 설정값
    #기본으로 설정되어 있는 템플릿 이름들은 모델명_xxx 형태 입니다.
    #CreateView 와 UpdateView는 form 이 접미사 인데 이걸 변경해서 bookmark_create 라는 이름의 템플릿 파일을 사용하도록 설정한 것

from django.views.generic.detail import DetailView

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'      #bookmark_update.html 이 템플릿이 된다

class BookmarkDeleteView(DeleteView):
    model= Bookmark
    success_url = reverse_lazy('list')

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6