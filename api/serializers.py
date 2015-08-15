from rest_framework import serializers
from skills.models import Skill

__author__ = 'cullycross'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        # fields =


