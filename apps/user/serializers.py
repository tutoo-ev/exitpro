from rest_framework import serializers

from apps.user.models import User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'mobile_number', 'password', 'user_type')

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
    is_superuser = serializers.CharField(read_only=True)
    user_type = serializers.CharField(read_only=True)
    effective_resignation_date = serializers.CharField(read_only=True)
    attrition_type = serializers.CharField(read_only=True)
    reason_for_separation = serializers.CharField(read_only=True)
    last_day_of_work = serializers.CharField(read_only=True)
    date_of_hire = serializers.CharField(read_only=True)
    resignation_letter = serializers.CharField(read_only=True)
    rehire_eligibility = serializers.CharField(read_only=True)
    bamboo_hr_active_status = serializers.CharField(read_only=True)
    nearest_payroll_salary_or_CA_on_hold = serializers.CharField(read_only=True)
    clearance_and_exit_interview = serializers.CharField(read_only=True)
    deactivate_door_badge = serializers.CharField(read_only=True)
    deactivate_biometric_access = serializers.CharField(read_only=True)
    deactivate_ev_mail = serializers.CharField(read_only=True)
    deactivate_pc_login = serializers.CharField(read_only=True)
    deactivate_client_tools_and_emails = serializers.CharField(read_only=True)
    company_assets_returned = serializers.CharField(read_only=True)
    remove_from_evox_roster = serializers.CharField(read_only=True)
    department = serializers.CharField(read_only=True)

    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')


class UserTypeUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'user_type']


class UserDepartmentUpdateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'department']


attrition_fields = ['name', 'email', 'department', 'effective_resignation_date', 'attrition_type',
                    'reason_for_separation', 'last_day_of_work', 'date_of_hire', 'resignation_letter',
                    'rehire_eligibility']


class UserAttritionDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    department = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = attrition_fields


class UserAttritionHRSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    department = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'department', 'bamboo_hr_active_status', 'nearest_payroll_salary_or_CA_on_hold',
                  'clearance_and_exit_interview']


class UserAttritionICTSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    department = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'department', 'deactivate_door_badge', 'deactivate_biometric_access',
                  'deactivate_ev_mail', 'deactivate_pc_login', 'deactivate_client_tools_and_emails',
                  'company_assets_returned']
