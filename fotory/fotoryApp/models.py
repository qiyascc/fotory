from django.db import models

class Album(models.Model):
    ALBUM_TYPES = [('education', 'Education')]
    album_type = models.CharField(max_length=50, choices=ALBUM_TYPES)
    name = models.CharField(max_length=100)
    date_range = models.CharField(max_length=50)
    group_name = models.CharField(max_length=100)

    def album_types_name_groupname(self):
        return f"{self.get_album_type_display()}_{self.name}_{self.group_name}"

    def __str__(self):
        return self.album_types_name_groupname()



class Person(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile_photo = models.ImageField(upload_to='profiles/')
    
    def __str__(self):
        return f"{self.name}_{self.album.group_name}_{self.album.name}"

class Photo(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')
    