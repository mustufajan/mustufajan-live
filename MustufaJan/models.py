from django.db import models

# Create your models here.
class Profile(models.Model):
    tag = models.CharField(max_length=500, blank=True, default='SW')
    profession = models.CharField(max_length=500)
    headline = models.CharField(max_length=500)
    highlights = models.ManyToManyField('Highlight', related_name="relevant_role", blank=True)

    def __str__(self):
        return f"{self.profession}"

class Highlight(models.Model):
    category_choices = [
        ('Education', 'Education'),
        ('Work', 'Work'),
    ]

    profile = models.ManyToManyField('Profile', related_name="relevant_highlights")

    position = models.CharField(max_length=500, blank=True)
    institution = models.CharField(max_length=500)
    institution_description = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=500, blank=True)
    logo_path = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=10000)
    start_date=models.DateField(blank=True, null=True)
    end_date=models.DateField()
    category = models.CharField(
        max_length= 20,
        choices= category_choices,
        default= 'Work')

    def __str__(self):
        return f"{self.position} at {self.institution} {self.profile.all()}"

class Project(models.Model):

    heading = models.CharField(max_length=500, blank=True)
    git_link = models.CharField(max_length=500, blank=True)
    preview = models.CharField(max_length=500, blank=True)
    logo_path = models.CharField(max_length=500, blank=True)
    icon_path = models.CharField(max_length=500, blank=True)
    tech_stack = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return f"{self.heading} using {self.tech_stack}"

class Feature(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    Project =  models.ForeignKey("Project", on_delete=models.CASCADE, related_name="features")

    def __str__(self):
        return f"{self.name} feature in {self.Project}"

class Skill(models.Model):

    name = models.CharField(max_length=500, blank=True)
    level = models.DecimalField(max_digits=2, decimal_places=1, default=3.5)
    years = models.DecimalField(max_digits=2, decimal_places=1, default=1)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "years": self.years
        }
    
    def __str__(self):
        return f"{self.name} with {self.years} years of experience at level {self.level}"

    