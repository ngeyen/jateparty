from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Active"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    address = models.TextField()
    items = models.CharField(max_length=700, )
    content = models.TextField()
    date = models.DateField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='party_posts')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    @property
    def tools(self):
        items = self.items.split(',')
        tools = [i.strip().capitalize() for i in items]
        return tools


class Attendance(models.Model):
    photo = models.ImageField(upload_to='attendance', null=True, blank=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='attendance')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
