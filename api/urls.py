from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('user', views.userViews)
router.register('department', views.departmentViews)
router.register('authority', views.authorityViews)
router.register('section', views.sectionViews)
router.register('subsection', views.subSectionViews)
router.register('machine', views.machineViews)
router.register('machinetype', views.machineTypeViews)
router.register('status', views.statusViews)
router.register('machinestatus', views.machineStatusViews)
router.register('jobtype', views.jobTypeViews)
router.register('type', views.typeViews)
router.register('complaintstatus', views.complaintStatusViews)
router.register('complaint', views.complaintViews)
router.register('action', views.actionViews)


urlpatterns = [
    path('api/', include(router.urls)),
]
