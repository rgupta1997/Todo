from rest_framework import serializers
from todoo.models import *

class TodooSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    types=(( 'created','Created'),('inprogress','inprogress'),('done','Done'))
    desc=serializers.CharField(max_length=500)
    title=serializers.CharField(max_length=200)
    status=serializers.CharField(max_length=100)
    

    def create(self,validated_data):
        return Todoo.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.desc=validated_data.get('desc',instance.desc)
        instance.title=validated_data.get('title',instance.title)
        instance.status=validated_data.get('status',instance.status)
        instance.save()
        return instance

