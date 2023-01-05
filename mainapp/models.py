from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import CustomUser as User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
	author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	title=models.CharField(max_length=100)
	slug=models.SlugField(unique=True)
	content=RichTextUploadingField()
	blog_img=models.ImageField(blank=True, null=True)
	date_posted=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=('-date_posted',)
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug=slugify(self.title)
		super(Blog, self).save(*args,**kwargs)

	def get_absolute_url(self, *args, **kwargs):
		from django.urls import reverse
		return reverse("_blog", args =[str(self.slug)])


class Newsletter(models.Model):
	email=models.EmailField(unique=True)

	def __str__(self):
		return self.email

class UpcomingEvent(models.Model):
	title=models.CharField(max_length=100)
	subtitle=models.CharField(max_length=100)
	details=RichTextUploadingField()
	image=models.ImageField(upload_to="UpcomingEvent")
	eventpast=models.BooleanField(default=False, null=True)
	date_posted=models.DateTimeField(auto_now_add=True, null=True)


	class Meta:
		ordering=('-date_posted',)

	def __str__(self):
		return self.title