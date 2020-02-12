#admin.py
#모델을 관리자 페이지에 등록해 관리할 수 있도록 하는 역할
#관리자 페이지에서 보이는 내용의 변경, 기능 추가 등을 할 수 있도록 코드를 입력하는 파일
from django.contrib import admin

from .models import Bookmark
#models.py에서 Bookmark 라는 모델을 불러오겠다 라는 의미

admin.site.register(Bookmark)
#등록하여 관리자 페이지에서 해당 모델을 관리 할 수 있도록 함.
