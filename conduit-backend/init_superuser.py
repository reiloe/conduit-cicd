import os
from django.contrib.auth import get_user_model

print("DEBUG: starting init_superuser.py")

name = os.environ.get("DJANGO_SU_NAME")
email = os.environ.get("DJANGO_SU_EMAIL")
password = os.environ.get("DJANGO_SU_PASSWORD")

print("DEBUG ENV:", name, email, password)

User = get_user_model()

try:
    qs = User.objects.filter(username=name)
    print("DEBUG: existing users with that name:", list(qs.values("username", "email")))

    if not qs.exists():
        User.objects.create_superuser(name, email, password)
        print("✅ Superuser created:", name)
    else:
        print("ℹ️ Superuser already exists:", name)
except Exception as e:
    print("❌ ERROR while creating superuser:", e)