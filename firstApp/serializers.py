from rest_framework import serializers
from .models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id', 'first_name', 'last_name', 'email', 'address', 'phone_number' ]

class StudentSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        ('male', 'male'),	
        ('female', 'female'),
    )
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    phone_number = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)



    def validate(self, attrs):
        #extra validation
        return super().validate(attrs)
    
    def create(self, validated_data):
        #do any custom logic here
        student = Student.objects.create(**validated_data)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name' , instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
        # return super().update(instance, validated_data)