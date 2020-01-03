from django.db import models
from django.contrib.auth.models import User
from PIL import Image

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to=user_directory_path)
    resume = models.FileField(upload_to=user_directory_path, blank=True)
    class_number = models.CharField(max_length=10)
    CAREER_PATH_CHOICES = [
        ('IT', 'IT'),
        ('FIN', 'Finance'),
        ('PHA', 'Pharmaceutical'),
        ('ACA', 'Academia'),
        ('OTH', 'Other')
    ]
    career_path = models.CharField(max_length=5,
                                   choices=CAREER_PATH_CHOICES)
    company = models.CharField(max_length=100, blank=True)
    employment_status = models.CharField(max_length=2,
                                         choices=(
                                             ('1', 'Looking for Jobs'),
                                             ('2', 'Looking for Candidates'),
                                             ('3', 'Both')
                                         )
                                         )
    start_time = models.CharField(max_length=2,
                                  choices=(
                                      ('1', 'In 2 weeks'),
                                      ('2', 'In a month'),
                                      ('3', 'In 3 months'),
                                      ('4', 'In 6 months')
                                  )
                                  )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save(**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)