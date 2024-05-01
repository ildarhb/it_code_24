from django.db import models

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=250)
    body = models.TextField()
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи' 

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
    
    def __str__(self):
        return f'Коммент {self.name} на {self.post}'

