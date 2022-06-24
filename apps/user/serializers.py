from rest_framework import serializers

from apps.user.models import User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'email', 'mobile_number', 'password')

    def create(self, validated_data):
        username = validated_data.get('username')
        name = validated_data.get('name')
        email = validated_data.get('email')
        mobile_number = validated_data.get('mobile_number')
        password = validated_data.get('password')
        user = User(username=username, email=email, name=name, mobile_number=mobile_number)
        user.set_password(password)
        user.save()
        return user
        return super().create(validated_data)


class UserViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class SingleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')


class UserTypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'user_type']


class UserDepartmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'department']


attrition_fields = ['name', 'email', 'department', 'effective_resignation_date', 'attrition_type',
                    'reason_for_separation', 'last_day_of_work', 'date_of_hire', 'resignation_letter',
                    'rehire_eligibility']


class UserAttritionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = attrition_fields


class UserAttritionHRSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'email', 'department', 'bamboo_hr_active_status', 'nearest_payroll_salary_or_CA_on_hold', 'clearance_and_exit_interview']


class UserAttritionICTSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'email', 'department', 'deactivate_door_badge', 'deactivate_biometric_access', 'deactivate_ev_mail', 'deactivate_pc_login',
                  'deactivate_client_tools_and_emails', 'company_assets_returned']
