from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, Http404
from .serializers import *
from .models import *
from .filter import *
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
@csrf_exempt
def TBGRApi(request, tbgrno=0):
    if request.method == 'GET':
        tbgrs = TBGR.objects.all()
        tbgrs_serializer = TBGRSerializer(tbgrs, many=True)
        return JsonResponse(tbgrs_serializer.data, safe=False)

    elif request.method == 'POST':
        tbgr_data = JSONParser().parse(request)
        tbgr_serializer = TBGRSerializer(data=tbgr_data)
        if tbgr_serializer.is_valid():
            tbgr_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        tbgr_data = JSONParser().parse(request)
        tbgr = TBGR.objects.get(tbgrno=tbgr_data['tbgrno'])
        tbgr_serializer = TBGRSerializer(tbgr, data=tbgr_data)
        if tbgr_serializer.is_valid():
            tbgr_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        tbgr = TBGR.objects.get(tbgrno=tbgrno)
        tbgr.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def BoardApi(request):
    if request.method=='GET':
        boards = Board.objects.all()
        boards_serializer = BoardSerializer(boards, many=True)
        return JsonResponse(boards_serializer.data, safe=False)

@csrf_exempt
def VillageApi(request, villageid=0):
    if request.method == 'GET':
        villages = Village.objects.all()
        villages_serializer = VillageSerializer(villages, many=True)
        return JsonResponse(villages_serializer.data, safe=False)

    elif request.method == 'POST':
        village_data = JSONParser().parse(request)
        village_serializer = VillageSerializer(data=village_data)
        if village_serializer.is_valid():
            village_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        village_data = JSONParser().parse(request)
        village = Village.objects.get(villageid=village_data['villageid'])
        village_serializer = VillageSerializer(village, data=village_data)
        if village_serializer.is_valid():
            village_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        village = Village.objects.get(villageid=villageid)
        village.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt

def SlipApi(request, lotno=0):
    if request.method == 'GET':
        slips = Slip.objects.all()
        slips_serializer = SlipSerializer(slips, many=True)
        return JsonResponse(slips_serializer.data, safe=False)

    elif request.method == 'POST':
        slip_data = JSONParser().parse(request)
        slip_serializer = SlipSerializer(data=slip_data)
        if slip_serializer.is_valid():
            slip_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    # elif request.method == 'POST':
    #     slip_data = JSONParser().parse(request)
    #     slips = Slip.objects.all()
    #     if slip_data['lotno']:
    #         slips = slips.filter(lotno=slip_data['lotno'])
    #     if slip_data['tbgrno']:
    #         slips = slips.filter(tbgrno=slip_data['tbgrno'])
    #     if slip_data['grade']:
    #         slips = slips.filter(grade=slip_data['grade'])
    #     slips_serializer = SlipSerializer(slips, many=True)
    #     return JsonResponse(slips_serializer.data, safe=False)

    elif request.method == 'PUT':
        slip_data = JSONParser().parse(request)
        slip = Slip.objects.get(lotno=slip_data['lotno'])
        slip_serializer = SlipSerializer(slip, data=slip_data)
        if slip_serializer.is_valid():
            slip_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        slip = Slip.objects.get(lotno=lotno)
        slip.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def GradeApi(request):
    if request.method == 'GET':
        grades = Grades.objects.all()
        grades_serializer = GradeSerializer(grades, many=True)
        return JsonResponse(grades_serializer.data, safe=False)

@csrf_exempt
def ContactApi(request, phone=0):
    if request.method == 'GET':
        contacts = Contacts.objects.all()
        contacts_serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(contacts_serializer.data, safe=False)

    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = ContactSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False, status=404)

    elif request.method == 'PUT':
        contact_data = JSONParser().parse(request)
        contact = Contacts.objects.get(phone=contact_data['phone'])
        contact_serializer = ContactSerializer(contact, data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        contact = Contacts.objects.get(phone=phone)
        contact.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
