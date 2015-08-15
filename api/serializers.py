from django.contrib.auth.models import User
from rest_framework import serializers
from builder.models import CharFieldTranslation, CharField, TextFieldTranslation, TextField, ImageFieldTranslation, \
    ImageField
from skills.models import Skill, SkillLevelTranslation, SkillLevel, CategoryTranslation, Category, ReferenceTranslation, \
    Reference, SkillTranslation

__author__ = 'cullycross'

# todo(CullyCross): make nice inheritance

class CharFieldTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharFieldTranslation
        fields = ('language', 'name', )


class CharFieldSerializer(serializers.ModelSerializer):
    translations = CharFieldTrSerializer()

    class Meta:
        model = CharField
        fields = ('translations', )


class TextFieldTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextFieldTranslation
        fields = ('language', 'name', )


class TextFieldSerializer(serializers.ModelSerializer):
    translations = TextFieldTrSerializer()

    class Meta:
        model = TextField
        fields = ('translations', )


class ImageFieldTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFieldTranslation
        fields = ('language', 'name', )


class ImageFieldSerializer(serializers.ModelSerializer):
    translations = ImageFieldTrSerializer()

    class Meta:
        model = ImageField
        fields = ('translations', )


class SkillLevelTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillLevelTranslation
        fields = ('language', 'name', 'description', )


class SkillLevelSerializer(serializers.ModelSerializer):
    translations = SkillLevelTrSerializer()

    class Meta:
        model = SkillLevel
        fields = ('translations', 'level', )


class CategoryTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTranslation
        fields = ('language', 'name', 'description', )


class CategorySerializer(serializers.ModelSerializer):
    translations = CategoryTrSerializer()

    class Meta:
        model = Category
        fields = ('translations', )


class ReferenceTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceTranslation
        fields = ('language', 'name', 'description', )


class ReferenceSerializer(serializers.ModelSerializer):
    translations = ReferenceTrSerializer()

    class Meta:
        model = Reference
        fields = ('translations', 'email')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )


class SkillTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTranslation
        fields = ('language', 'name', 'description', )


class SkillSerializer(serializers.ModelSerializer):
    translations = SkillTrSerializer()
    parent_skills = serializers.PrimaryKeyRelatedField(many=True)
    owner = UserSerializer()
    contributors = UserSerializer(many=True)

    class Meta:
        model = Skill
        fields = ('context', 'parent_skills', 'owner', 'contributors', 'translations', )




