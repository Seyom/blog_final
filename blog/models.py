from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    img = models.ImageField(upload_to="blog/") #media/파일이름 저장되게 세팅.파이에서 했는데 미디어/블로그/파일이름 으로 저장되게 한거


# 제목을 오브젝트 123이 아닌 제목으로 보이게 해주는
    def __str__(self):
        return self.title
# 내용을 100자만 보여주는
    def summary(self):
        return self.body[:100]


