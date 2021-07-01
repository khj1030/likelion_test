from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    writer= models.ForeignKey(User, on_delete=models.CASCADE, null=True) # on_delete : 삭제할 때 연결도 끊겠다는 의미

    likes = models.ManyToManyField(User, through='Like', through_fields=('blog','user'), related_name="likes") # through: ~를 통과한다. through_fields: ~를 통해서 통과하겠다.

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField(max_length=500)
    pub_date = models.DateTimeField("data published")
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) # 블로그 글 하나

#foreignKey:일대다 -> 좋아요는 다대다인데 왜 ForeignKey? => "라이크 입장에서는 유저와 일대다 관계를 형성하는 것"
class Like(models.Model): 
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
