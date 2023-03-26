from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password, username, **kwargs):
        if not email:
            raise ValueError('이메일 정보가 없습니다.')

        user = self.model(
            email=email,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, username=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
            username=username,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser