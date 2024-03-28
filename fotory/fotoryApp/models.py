from django.db import models

class Album(models.Model):
    ALBUM_TYPES = [
        ('education', 'Education'),
    ]

    album_type = models.CharField(max_length=50, choices=ALBUM_TYPES)
    name = models.CharField(max_length=100)
    date_range = models.CharField(max_length=50)
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_album_type_display()} - {self.name} - {self.group_name}"
    

class Person(models.Model):
    album = models.ForeignKey(Album, related_name='persons', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return f"{self.name} - {self.album.name}"

class Photo(models.Model):
    person = models.ForeignKey(Person, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')

    class Meta:
        verbose_name = 'Personal Photo'
        verbose_name_plural = 'Personal Photos'

    def __str__(self):
        return f"Photo of {self.person.name}"

class GroupPhoto(models.Model):
    album = models.ForeignKey(Album, related_name='group_photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='group_photos/')

    class Meta:
        verbose_name = 'Public Photo'
        verbose_name_plural = 'Public Photos'

    def __str__(self):
        return f"{self.album.name} Group Photo"

class JointPhoto(models.Model):
    album = models.ForeignKey(Album, related_name='joint_photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='joint_photos/')
    people = models.ManyToManyField(Person, related_name='joint_photos')

    def __str__(self):
        people_names = ', '.join(person.name for person in self.people.all())
        return f"{self.album.name} - {people_names}"
