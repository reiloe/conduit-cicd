# init_superuser.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conduit.settings")
django.setup()

from django.contrib.auth import get_user_model

print(">>> init_superuser.py running")

name = os.environ.get("DJANGO_SU_NAME")
email = os.environ.get("DJANGO_SU_EMAIL")
password = os.environ.get("DJANGO_SU_PASSWORD")

print(">>> DEBUG ENV:", name, email, password)

User = get_user_model()

if not User.objects.filter(username=name).exists():
    user = User.objects.create_superuser(username=name, email=email, password=password or "changeme123")
    print("✅ Superuser created:", name)
else:
    print("ℹ️ Superuser already exists:", name)