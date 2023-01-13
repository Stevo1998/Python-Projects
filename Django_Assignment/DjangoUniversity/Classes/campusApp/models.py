from django.db import models

# Create your models here.


# Creating model of Campuses
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default=None, blank=True, null=True)

    # Creates model manager
    objects = models.manager

    # Function displays the object output values in the form of a string
    def __str__(self):
        return self.campus_name  # Returns the input value of the campus name to display on the browser as the title

    # Removes added 's' that Django adds to the model name on the browser display
    class Meta:
        verbose_name_plural = "University Campus"

