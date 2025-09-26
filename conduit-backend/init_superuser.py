import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conduit.settings")
django.setup()

from django.contrib.auth import get_user_model

print(">>> init_superuser.py running")

name = os.environ.get("DJANGO_SU_NAME")
email = os.environ.get("DJANGO_SU_EMAIL")
password = os.environ.get("DJANGO_SU_PASSWORD")

User = get_user_model()

if not User.objects.filter(username=name).exists():
    User.objects.create_superuser(name, email, password)
    print("✅ Superuser created:", name)
else:
    print("ℹ️ Superuser already exists:", name)