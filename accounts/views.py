from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import Http404, HttpResponseRedirect
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView

from .serializers import CustomRegisterSerializer, CustomUserDetailSerializer, UserInfoEmailSerializer
from .models import User

# ============= EMAIL =============
class ConfirmEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        # A React Router Route will handle the failure scenario
        return HttpResponseRedirect('http://localhost:3000/signup/success') # 인증성공

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                # A React Router Route will handle the failure scenario
                return HttpResponseRedirect('/') # 인증실패
        return email_confirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs

# ============= Registeration =============
class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

# ============= User Detail =============
class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailSerializer

class UserInfoEmailView(APIView): # 이메일로 유저 정보 불러오기
    def get_object(self, email):
        print(email)
        try:
            return User.objects.filter(email__icontains=email)[0]
        except User.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        print(request)
        user = self.get_object(email)
        serializer = UserInfoEmailSerializer(user)
        return Response(serializer.data)