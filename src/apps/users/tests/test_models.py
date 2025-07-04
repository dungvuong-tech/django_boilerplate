import pytest
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = "testuser@example.com"
    password = "testpassword"


@pytest.mark.django_db
def test_create_user():
    user = UserFactory()
    assert user.email == "testuser@example.com"
    assert user.check_password("testpassword")
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_superuser():
    user = User.objects.create_superuser(
        email="superuser@example.com", password="superpassword"
    )
    assert user.email == "superuser@example.com"
    assert user.check_password("superpassword")
    assert user.is_staff
    assert user.is_superuser
