from django.shortcuts import render
from rest_framework import viewsets
from .models import users, authority, department, section, subSection, machine, machineStatus, machineType, status, jobType, Type, complaintStatus, complaint, Action
from .serializers import userSerializer, departmentSerializer, authoritySerializer, sectionSerializer, subsectionSerializer, machineSerializer, machineStatusSerializer, machineTypeSerializer, statusSerializer, jobTypeSerializer, typeSerializer, complaintStatusSerializer, complaintSerializer, actionSerializer
import json
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import action
# Create your views here.


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class userViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = users.objects.all()
    serializer_class = userSerializer


class departmentViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = department.objects.all()
    serializer_class = departmentSerializer


class authorityViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = authority.objects.all()
    serializer_class = authoritySerializer


class sectionViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = section.objects.all()
    serializer_class = sectionSerializer


class subSectionViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = subSection.objects.all()
    serializer_class = subsectionSerializer


class machineViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = machine.objects.all()
    serializer_class = machineSerializer


class machineTypeViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = machineType.objects.all()
    serializer_class = machineTypeSerializer


class statusViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = status.objects.all()
    serializer_class = statusSerializer


class machineStatusViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = machineStatus.objects.all()
    serializer_class = machineStatusSerializer


class jobTypeViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = jobType.objects.all()
    serializer_class = jobTypeSerializer


class typeViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Type.objects.all()
    serializer_class = typeSerializer


class complaintStatusViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = complaintStatus.objects.all()
    serializer_class = complaintStatusSerializer


class complaintViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = complaint.objects.all()
    serializer_class = complaintSerializer


class actionViews(viewsets.ModelViewSet):
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Action.objects.all()
    serializer_class = actionSerializer
    
    
    

@csrf_exempt
def machineData(request):
    if request.method == 'POST':
        machineID = request.POST.get("machine")
        print(machineID)
        machType = machine.objects.get(id=str(machineID))
        if machType:
            machType = machineType.objects.get(id=str(machType))
            objects = machType.sections.all()
            sections = []
            for o in objects:
                sections.append(str(o))

            objects = machType.subsections.all()
            subsections = []
            for o in objects:
                subsections.append(str(o))

            res = {
                "machineType": machType.name,
                "sections": sections,
                "subsections": subsections
            }

            return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            return HttpResponse("No Machine")
    else:
        return HttpResponse("Hello")

