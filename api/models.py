from django.db import models


class Salary(models.Model):
    name = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    salary = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "salaries"
        verbose_name = "salary"
        verbose_name_plural = "salaries"

    def __str__(self):
        return self.name
