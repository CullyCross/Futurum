from django.contrib.auth.models import User
from rest_framework import serializers
from builder.models import CharFieldTranslation, CharField, TextFieldTranslation, TextField, ImageFieldTranslation, \
    ImageField, AbstractTranslationFieldModel
from skills.models import Skill, SkillLevelTranslation, SkillLevel, CategoryTranslation, Category, ReferenceTranslation, \
    Reference, SkillTranslation, AbstractTranslationModel

__author__ = 'cullycross'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )

# todo(CullyCross): make nice inheritance

# Translation serializers

class CharFieldTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharFieldTranslation
        fields = ('language', 'name', )


class TextFieldTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextFieldTranslation
        fields = ('language', 'name', )


class ImageFieldTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFieldTranslation
        fields = ('language', 'name', )


class SkillLevelTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillLevelTranslation
        fields = ('language', 'name', 'description', )


class CategoryTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTranslation
        fields = ('language', 'name', 'description', )


class ReferenceTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceTranslation
        fields = ('language', 'name', 'description', )


class SkillTrSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTranslation
        fields = ('language', 'name', 'description', )

# Model serializers:

class CharFieldSerializer(serializers.ModelSerializer):
    translations = CharFieldTrSerializer()

    class Meta:
        model = CharField
        fields = ('translations', )


class TextFieldSerializer(serializers.ModelSerializer):
    translations = TextFieldTrSerializer()

    class Meta:
        model = TextField
        fields = ('translations', )


class ImageFieldSerializer(serializers.ModelSerializer):
    translations = ImageFieldTrSerializer()

    class Meta:
        model = ImageField
        fields = ('translations', )


class SkillLevelSerializer(serializers.ModelSerializer):
    translations = SkillLevelTrSerializer()
    text_fields = TextFieldSerializer()
    char_fields = CharFieldSerializer()
    image_fields = ImageFieldSerializer()

    class Meta:
        model = SkillLevel
        fields = ('translations', 'level', 'text_fields',
                  'char_fields', 'image_fields')


class CategorySerializer(serializers.ModelSerializer):
    translations = CategoryTrSerializer()

    class Meta:
        model = Category
        fields = ('translations', )


class ReferenceSerializer(serializers.ModelSerializer):
    translations = ReferenceTrSerializer()

    class Meta:
        model = Reference
        fields = ('translations', 'email')


class SkillSerializer(serializers.ModelSerializer):
    translations = SkillTrSerializer()
    parent_skills = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    owner = UserSerializer()
    contributors = UserSerializer(many=True)

    class Meta:
        model = Skill
        fields = ('context', 'parent_skills', 'owner', 'contributors', 'translations', )
