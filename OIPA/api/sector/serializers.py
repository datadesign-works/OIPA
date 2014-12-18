from rest_framework import serializers
import iati
from api.serializers import DynamicFieldsModelSerializer


class SectorSerializer(DynamicFieldsModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='sector-detail')

    class Meta:
        model = iati.models.Sector
        fields = (
            'url',
            'code',
            'name',
            'description',
            'category',

            # Reverse linked data
            'activity_set',
            'activitysector_set',
        )