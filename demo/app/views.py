from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *

class Activity_PeriodViewSet(viewsets.ViewSet):        
    def list(self,request):
        activity_periodlist = ActivityPeriod.objects.all()
        member_list = []
        period_data_list=[]
        for activity_periodlists in activity_periodlist:
            member_list.append({
                'id':activity_periodlists.memer.id_name,
                'real_name':activity_periodlists.memer.real_name,
                'tx':activity_periodlists.memer.tz,
                'peridio_period':period_data_list
            })
            period_data_list.append({
                'start_time':activity_periodlists.start_time,
                'end_time':activity_periodlists.end_time
            })
        response_payload={
        'ok':True,
        'member':member_list
        }
        return Response(response_payload)
    def create(self,request):
        id=request.data.get('id')
        memer_id=Member.objects.get(id=id)
        activity_object= ActivityPeriod.objects.get(memer=memer_id)
        
        activity_object.memer=memer_id
        # activity_object.start_time = request.data.get('start_time')
        # activity_object.end_time = request.data.get('end_time')
        activity_object.save()
        return Response({'Create Data'})
