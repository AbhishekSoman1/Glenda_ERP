from django.db import models

from register_app.models import CustomUser
from django.conf import settings


# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title  # Returns the title for clarity

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        ordering = ['title']  # Optional: orders the menus by title

class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, related_name='submenus', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url_name = models.CharField(max_length=255)  # Used for URL reversing

    def __str__(self):
        return self.title  # Returns the title for clarity

    class Meta:
        verbose_name = "SubMenu"
        verbose_name_plural = "SubMenus"
        ordering = ['title']  # Optional: orders the submenus by title

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.content}"


class Event(models.Model):
    title = models.CharField(max_length=100,null=True)
    start = models.DateTimeField(null=True)

    def __str__(self):
        return self.title