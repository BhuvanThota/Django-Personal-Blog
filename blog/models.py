from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length = 100)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_adr = models.EmailField(null = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class All_Posts(models.Model):
    title = models.CharField(max_length = 200)
    excerpt = models.CharField(max_length = 500)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(default="",blank= True, null=False, unique= True, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null = True)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to="images", default="images/coding.jpg")


    def __str__(self):
        return f"{self.title} {self.author}"
    

    class Meta:
        verbose_name_plural = "All_Posts"


class Comment(models.Model):
    username = models.CharField(max_length=100)
    user_email = models.EmailField()
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(5)], default = 5)
    post = models.ForeignKey(All_Posts, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.username