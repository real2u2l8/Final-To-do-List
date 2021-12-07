DJANGO_SECRET_KEY = 'django-insecure-q^=12425291'

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql', # 고정
        'NAME': 'Htodolist', # DB 이름
        'USER': 'admin', # 계정
        'PASSWORD': 'Ad12345678@@', # 암호
        'HOST': '52.79.235.242', # IP
        'PORT': '3306'
    }
}