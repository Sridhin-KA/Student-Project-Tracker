from django.db import models

class Batch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        related_name="students"
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    title = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return f"{self.student.name} - {self.title}"