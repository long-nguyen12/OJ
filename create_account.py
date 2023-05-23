#use python manage.py shell

from judge.models import *
from django.contrib.auth.models import User
from openpyxl import load_workbook
import os
wb = load_workbook(filename='testht.xlsx', read_only=True)
ws = wb['Sheet2']
for row in ws.rows:
    password = row[-1].value
    username = row[-2].value
    email = username + "@gmail.com"
    user = User.objects.create_user(username, email, password)
    
    profile = Profile(user=user, language=Language.get_python3())
    profile.save()

# password = "Hdu123456"
# username = "Hdu123456"
# email = "Hdu123456@gmail.com"
# user = User.objects.create_user(username, email, password)
# user.last_name = "HDU"
# user.first_name = "Hdu123456"
# user.save()
# profile = Profile(user=user, language=Language.get_python3())
# profile.save()

