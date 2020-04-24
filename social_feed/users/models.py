from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextField, ImageField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    bio = TextField("Enter your Bio", blank=True, max_length=500)
    profile_picture = ImageField("Upload your profile picture", upload_to="media", blank=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
