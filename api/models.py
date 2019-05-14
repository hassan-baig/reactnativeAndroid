from django.db import models

# Create your models here.


class department(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class authority(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class users(models.Model):
    name = models.CharField(max_length=255)
    userID = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    authority = models.ForeignKey(authority, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name


class section(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class subSection(models.Model):
    name = models.CharField(max_length=255)
    section = models.ForeignKey(section, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name


class machineType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    NoOfMachine = models.IntegerField()
    sections = models.ManyToManyField(section)
    subsections = models.ManyToManyField(subSection)
    objects = models.Manager()

    def __str__(self):
        return self.name


class status(models.Model):
    name = models.CharField(max_length=255, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class machine(models.Model):
    machineType = models.ForeignKey(machineType, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk)


class machineStatus(models.Model):
    status = models.ForeignKey(status, on_delete=models.CASCADE)
    MachineID = models.ForeignKey(machine, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.status


class jobType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class complaintStatus(models.Model):
    name = models.CharField(max_length=255, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class complaint(models.Model):
    machinetype = models.ForeignKey(machineType, on_delete=models.CASCADE)
    machineID = models.ForeignKey(machine, on_delete=models.CASCADE)
    section = models.ForeignKey(section, on_delete=models.CASCADE)
    subsection = models.ForeignKey(subSection, on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)
    shift = models.CharField(max_length=5)
    problem = models.TextField()
    breakDownTime = models.TimeField(auto_now_add=True)
    Reporter = models.ForeignKey(users, on_delete=models.CASCADE)
    jobtype = models.ForeignKey(jobType, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    status = models.ForeignKey(complaintStatus, on_delete=models.CASCADE)
    objects = models.Manager()


class Action(models.Model):
    RefNo = models.ForeignKey(complaint, on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)
    shift = models.CharField(max_length=5)
    actionTaken = models.TextField()
    remarks = models.TextField()
    startTime = models.TimeField()
    handoverTime = models.TimeField()
    Attendee = models.ForeignKey(users, on_delete=models.CASCADE)
    status = models.ForeignKey(complaintStatus, on_delete=models.CASCADE)
    objects = models.Manager()
