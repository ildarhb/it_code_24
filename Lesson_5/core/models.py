from django.db import models

class Category(models.Model):
    title = models.CharField(verbose_name='Наименования категории', max_length=150)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=250)
    body = models.TextField()
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    likes = models.PositiveIntegerField(verbose_name='Лайки', 
                                        blank=True, 
                                        default=0)
    date = models.DateField(verbose_name='Дата', blank=True)
    photo = models.ImageField(blank=True)
    category = models.ForeignKey(Category,
                             on_delete=models.CASCADE,
                             related_name='comments')
    
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
    on_moderation = models.BooleanField(verbose_name='На модерации',
                                        default=True,)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
    
    def __str__(self):
        return f'Коммент {self.name} на {self.post}'

