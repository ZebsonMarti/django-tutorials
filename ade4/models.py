from django.db import models

# Create your models here.


def display_date(date):
    return date.strftime('%d-%m-%Y')


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

    def __str__(self):
        return self.raw_address.upper()

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Constants(TimestampMixin):
    title = models.CharField(max_length=100, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f'{self.title.upper()}: {self.amount}'

    class Meta:
        verbose_name = 'Constants'
        verbose_name_plural = 'Constants'


class Meeting(TimestampMixin):
    date = models.DateField(verbose_name='Date', unique=True)
    address = models.ForeignKey(to=Address, default='', on_delete=models.SET_DEFAULT)
    # hosts = models.ManyToManyField(to='Member', related_name='hosted_meetings', through='Hosts')

    class Meta:
        verbose_name = 'Meeting'
        ordering = ['-date']

    def __str__(self):
        return display_date(self.date)


class Member(TimestampMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(verbose_name='Full Name', max_length=100)
    register_date = models.ForeignKey(to=Meeting, to_field='date', null=True, on_delete=models.SET_NULL)
    address = models.ForeignKey(to=Address, on_delete=models.SET_NULL, null=True, blank=True, to_field='raw_address')
    skills = models.ManyToManyField(to=Skill)

    def __str__(self):
        return self.email

    def member_skills(self):
        s = [skill.title for skill in self.skills.all()] if self.id else []
        return '/'.join(s) if s else ''

    def reg_date(self):
        return display_date(self.register_date.date)


class ReceptionRound(TimestampMixin):
    start_date = models.ForeignKey(to=Meeting, to_field='date', null=False, blank=False, on_delete=models.CASCADE, related_name='start_reception_round')
    end_date = models.ForeignKey(to=Meeting, to_field='date', null=True, blank=True, on_delete=models.SET_NULL, related_name='end_reception_round')

    def __str__(self):
        return f"START: {self.start}-END: {self.end}"

    @property
    def start(self):
        return display_date(self.start_date.date) if self.start_date else '-'

    @property
    def end(self):
        return display_date(self.end_date.date) if self.end_date else '-'

    class Meta:
        verbose_name = 'Reception Round'
        verbose_name_plural = 'Reception Rounds'
        ordering = ['-start_date__date']
