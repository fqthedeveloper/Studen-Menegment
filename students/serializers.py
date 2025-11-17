from rest_framework import serializers
from .models import StudSelection

class StudSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudSelection
        fields = [
            'sel_SelectedIDKey',
            'sel_UserName',
            'sel_TableName'
        ]
