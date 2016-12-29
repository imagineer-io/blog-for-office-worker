from django.db import models

class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMENT,
    )

    hashtag = models.ManyToManyField(HashTag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        related_name="article_comments",
        on_delete=models.CASCADE
    )
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return "{}에 댓글: {}".format(self.article.title, self.content)

# class ArticleHasHashTag(models.Model):
#     article = models.ForeignKey(Article)
#     hashtag = models.ForeignKey(HashTag)
