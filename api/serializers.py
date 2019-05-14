from rest_framework import serializers
from .models import users, authority, department, section, subSection, machine, machineStatus, machineType, status, jobType, Type, complaintStatus, complaint, Action


class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users
        fields = ('id', 'name', 'userID', 'password',
                  'department', 'authority')


class departmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = department
        fields = ('id', 'name')


class authoritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = authority
        fields = ('id', 'name')


class sectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = section
        fields = ('id', 'name')


class subsectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = subSection
        fields = ('id', 'name', 'section')


class machineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = machine
        fields = ('id', 'machineType')


class machineTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = machineType
        fields = ('id', 'name', 'NoOfMachine', 'sections', 'subsections')


class statusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = status
        fields = ('id', 'name')


class machineStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = machineStatus
        fields = ('id', 'status', 'MachineID')


class jobTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = jobType
        fields = ('id', 'name')


class typeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')


class complaintStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = complaintStatus
        fields = ('id', 'name')


class complaintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = complaint
        fields = ('id', 'machinetype', 'machineID',
                  'section', 'subsection', 'Date', 'shift', 'problem', 'breakDownTime', 'Reporter', 'jobtype', 'type', 'status')


class actionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ('RefNo', 'Date', 'shift', 'actionTaken',
                  'remarks', 'startTime', 'handoverTime', 'Attendee', 'status')
