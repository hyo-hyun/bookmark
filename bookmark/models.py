from django.db import models

#models.Model 을 상속받는 Bookmark 클래스를 만듦.
#클래스 안에 site_name과 url 이라는 두 개의 필드를 만듦.
#데이터베이스에 이 두가지의 정보를 저장하려고 만듦.
#이 정보가 기록되는 테이블의 이름은 bookmark
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    def __str__(self):
        #객체를 출력할 때 나타날 값
        return "이름 : "+self.site_name + " , 주소:" + self.url
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])  #reverse 메서드는 URL 패턴의 이름과 추가 인자를 전달받아 URL를 생성하는 메서드

#_(언더바)가 앞뒤로 두 개씩 붙어있는 함수들을 매직 메서드라고 함. 클래스의 object를 출력할 때 나타날 내용을 결정하는 메서드
#북마크 모델에 __str__ 메서드를 추가, __str__메서드는 항상 문자열을 반환해야함

from django.urls import reverse