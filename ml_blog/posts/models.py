from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    media = RichTextUploadingField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def comments(self):
        return Comment.objects.filter(post=self)

    def __str__(self):
        return self.content


class Comment(models.Model):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    author = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.text}'
