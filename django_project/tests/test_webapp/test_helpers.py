import pytest
import os
import sys


# from django.contrib.auth.models import User
from webapp.models import Users


@pytest.mark.django_db
def test_users_create(Users):
    Users.objects.create_user('sajjad', 'zaidi', 'sajjad@we-over-i.com')
    assert Users.objects.count() == 1
