Post.objects.first()
Post.objects.last()
Post.objects.count()
Post.objects.order_by('title')
Post.objects.order_by('-title')
Post.objects.filter(title__contains='т')
Post.objects.filter(title__icontains='т')
Post.objects.filter(title__exact='Третья')
Post.objects.filter(title__iexact='Третья')
Post.objects.filter(likes__gt=5)
Post.objects.filter(likes__lte=5)
Post.objects.get(id=1)
Post.objects.filter(id=3).exists()
Post.objects.filter(likes__gt=3, title__contains='т')
Post.objects.create(title='test_title', body='text', status='Draft', date='2024-05-05')
Post.objects.create(title='test2_title', body='text', status='Published', likes=13, date='2024-05-05')
post = Post.objects.get(id=1)
Comment.objects.create(post=post, name='test_name', email='test@test.com', body='text text')
Comment.objects.filter(id__gt=2).update(on_moderation=False)
Comment.objects.filter(id__gt=2).delete()
Post.objects.values('title', 'status')
Post.objects.values_list('title', flat=True)
Post.objects.dates('date', 'day')
Comment.objects.exclude(name__contains='2')
Comment.objects.exclude(name__contains='2').reverse()