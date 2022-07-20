from django.contrib.auth.models import AbstractUser


class ApplicationUsers(AbstractUser):

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'ApplicationUser'
        verbose_name_plural = 'ApplicationUsers'
