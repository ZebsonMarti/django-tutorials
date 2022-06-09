from django.db import models

# Create your models here.


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Skill(TimestampMixin):
    title = models.CharField(verbose_name='Skill', max_length=100, unique=True)

    def __str__(self):
        return self.title.upper()


class Address(TimestampMixin):
    raw_address = models.CharField(max_length=100, unique=True, null=False, blank=False)


class Constants(TimestampMixin):
    title = models.CharField(max_length=100, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)