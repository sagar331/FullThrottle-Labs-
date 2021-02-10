from django.db import models
class Member(models.Model):
    id_name = models.CharField(max_length=30,null=False,blank=True)
    real_name = models.CharField(max_length=100,null=True,blank=True)
    tz = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.id_name
class ActivityPeriod(models.Model):
    memer = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='member')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.memer.real_name