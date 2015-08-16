from django.contrib.auth.models import User
from django.db import models
from skills.models import Skill


MONDAY = 'Mon'
TUESDAY = 'Tue'
WEDNESDAY = 'Wed'
THURSDAY = 'Thu'
FRIDAY = 'Fri'
SATURDAY = 'Sat'
SUNDAY = 'Sun'

WEEKDAYS = (
    (MONDAY, 'Monday'),
    (TUESDAY, 'Tuesday'),
    (WEDNESDAY, 'Wednesday'),
    (THURSDAY, 'Thursday'),
    (FRIDAY, 'Friday'),
    (SATURDAY, 'Saturday'),
    (SUNDAY, 'Sunday'),
)

class ScheduledSkill(models.Model):

    # Foreign keys
    skill = models.ForeignKey(Skill, verbose_name='scheduled')
    user = models.ForeignKey(User, verbose_name='scheduled_skills')

class TrainingTime(models.Model):

    # Foreign keys
    scheduled_skill = models.ForeignKey(ScheduledSkill)

    # Another fields
    day = models.CharField(max_length=3, choices=WEEKDAYS)
    from_time = models.TimeField()
    to_time = models.TimeField()


