from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name= "Author")
    title = models.CharField(max_length = 50, verbose_name= "Title")
    content = RichTextField()
    createdDate = models.DateTimeField(auto_now_add = True, verbose_name = "Created Date")
    articleImage = models.FileField(blank = True, null = True, verbose_name = "Image")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createdDate']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Comment", related_name = "comments")
    commentAuthor = models.CharField(max_length = 50, verbose_name = "Name")
    commentContent = models.CharField(max_length = 200, verbose_name = "Comment")
    commentDate = models.DateTimeField(auto_now_add = True, verbose_name = "Comment Date")

    def __str__(self):
        return self.commentContent
    
    class Meta:
        ordering = ['-commentDate']