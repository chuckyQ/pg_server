from django.db import models

# Create your models here.
class SafetyLimits(models.Model):

	program = models.CharField(max_length=50)
	upper_limit_v = models.FloatField()
	lower_limit_v = models.FloatField()

	