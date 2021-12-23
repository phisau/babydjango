import datetime
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """Different categories are e.g. diaper change, breast feeding"""

    category_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now)

    def was_published_recently(self):
        return self.pub_date >= timezone.now - datetime.timedelta(days=1)

    def __str__(self):
        return self.category_text


class Event(models.Model):
    """A single event of an action"""

    event_text = models.ForeignKey(Category, on_delete=models.CASCADE)
    shit = models.BooleanField("Contains shit", default=False)
    mood = models.IntegerField(default=0)
    fee = models.IntegerField(default=0)
    good_day = models.BooleanField("Had a good day?", default=False)

    time_from = models.DateTimeField("Time started", default=timezone.now)
    time_to = models.DateTimeField("Time ended", default=timezone.now)

    def within_24h(self):
        if self.time_from >= timezone.now - datetime.timedelta(days=1):
            return self.time_from.isoformat()

    def shit_show(self):
        return self.shit
    def from_show(self):
        #return self.time_from.isoformat()
        return self.time_from.strftime("%m/%d %H:%M:%S")
    def to_show(self):
        return self.time_to.strftime("%m/%d %H:%M:%S")
    def __str__(self):
        return self.time_from.isoformat()
