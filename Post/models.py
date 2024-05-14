import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save, post_delete
from notification.models import Notification


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='media/', blank=True)
    legende = models.CharField(max_length=10000 ,blank=True)
    date_publication = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    post_type=models.CharField(max_length=10000 ,blank=True)
    def get_absolute_url(self):
        return reverse("details-du-post", args=[str(self.id)])


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")

    @staticmethod
    def user_liked_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender_user = like.user
        notification = Notification(post=post, sender=sender_user, recipient=post.user, notification_type=1)
        notification.save()

    @staticmethod
    def user_unliked_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender_user = like.user
        Notification.objects.filter(post=post, sender=sender_user, notification_type=1).delete()


post_save.connect(Likes.user_liked_post, sender=Likes)
post_delete.connect(Likes.user_unliked_post, sender=Likes)


class Evenement(Post):
    date_evenement = models.DateField()

class Recommandation(Post):
    texte = models.TextField(blank=True)


class EvenClub(Evenement):
    prixC = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)

    nom = models.CharField(max_length=100 ,blank=True)
    domaine = models.CharField(max_length=100, blank=True)
 

class EvenSocial(Evenement):
    prixS = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)

    nom = models.CharField(max_length=100 ,blank=True)
    theme = models.CharField(max_length=100 ,blank=True)


class Stage(Post):
    localisation = models.CharField(max_length=200 ,blank=True)
    societe = models.CharField(max_length=200)
    duree = models.IntegerField()
    sujet = models.CharField(max_length=200)
    specialite = models.CharField(max_length=200)


class Logement(Post):
    localisation = models.CharField(max_length=200 ,blank=True)
    prix = models.IntegerField()
    contact_info = models.CharField(max_length=100 ,blank=True)


class Transport(Post):
    destination = models.CharField(max_length=200)
    type_transport = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200 ,blank=True)
