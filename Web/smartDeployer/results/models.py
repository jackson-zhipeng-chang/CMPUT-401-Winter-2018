from django.db import models

# Create your models here.

class WorkloadA(models.Model):
    workload = models.IntegerField()
    latency = models.FloatField()

    def __str__(self):
        return self.workload

class WorkloadB(models.Model):
    workload = models.IntegerField()
    latency = models.FloatField()

class WorkloadC(models.Model):
    workload = models.IntegerField()
    latency = models.FloatField()

class WorkloadD(models.Model):
    workload = models.IntegerField()
    latency = models.FloatField()

class Experiments(models.Model):
    cpu = models.IntegerField()
    mem = models.IntegerField()
    io = models.IntegerField()
