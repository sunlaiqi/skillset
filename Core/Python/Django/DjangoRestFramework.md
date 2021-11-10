


# Backend Refactor: add rest api to Django like-minded 

1. Create a new app for rest api:

```bash
$./manager.py startapp restapis
```
Install the needed packages.
```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

2. Add 'rest_framework' to your INSTALLED_APPS setting.

```py
INSTALLED_APPS = (
    ...
    'rest_framework',
)
```


If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root `urls.py` file.

```py
urlpatterns = [
    ...
    url(r'^api-auth/', include(‘rest_framework.urls’, namespace=‘rest_framework’))
]
```

Any global settings for a REST framework API are kept in a single configuration dictionary named `REST_FRAMEWORK`. Start off by adding the following to your `settings.py` module:

```py
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
```

3. serializers.py

Create serializers.py in restapis app, and add following codes.

```py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from groups.models import Group, Activity

# To get current User model
User = get_user_model()

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = ('url', 'username', 'email', 'is_staff', 'password')
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    organizer = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Group
        fields = ('name', 'photo', 'organizer', 'description', 'id')
        # fields = '__all__'

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.SlugRelatedField(read_only=True, slug_field='id')
    class Meta:
        model = Activity
        fields = ‘__all__'
```

4. Add viewsets 

In `views.py` under restapis, add viewsets for the serializers. 

Django Filter Backend:
http://www.django-rest-framework.org/api-guide/filtering/#api-guide

In order to filter out the returned data (e.g. activities by group), we need to setup a filter backend.

First, install Django-filter:
```bash
$ pip install django-filter
```
You should now either add the filter backend to your settings:
```py
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
```
Or add the filter backend to an individual View or ViewSet.
```py
from django_filters.rest_framework import DjangoFilterBackend
class UserListView(generics.ListAPIView):
    ...
    filter_backends = (DjangoFilterBackend,)
```

If all you need is simple equality-based filtering, you can set a `filter_fields` attribute on the view, or viewset, listing the set of fields you wish to filter against.
```py
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category', 'in_stock')
```

This will automatically create a `FilterSet` class for the given fields, and will allow you to make requests such as:
http://example.com/api/products?category=clothing&in_stock=True

Therefore, here are the snippets for our viewsets. (don’t forget to add ‘django-filter’ into INSTALLED_APP in setting file)
```py
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth import get_user_model
from groups.models import Group, Activity
from .serializers import UserSerializer, GroupSerializer, ActivitySerializer

# To get the current user model
User = get_user_model()

# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields =  ('group', 'name', ‘venue')
```

5. urls.py 

Create urls.py file under restapis app and add following snippet.

```py
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, ActivityViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
```

You can now open the API in your browser at http://127.0.0.1:8000/restapis/, and view your new APIs. If you use the login control in the top right corner you'll also be able to add, create and delete users from the system.

6. Configure cors on Django to allow client access

otherwise, you will get the following error when accessing api in client:
Failed to load http://192.168.3.2:8000/restapis/groups/: No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://localhost:8080' is therefore not allowed access.

This is a CORS issue. We need to enable Django to support CORS. In fact, it is to enable CORS in order to allow all the CORS.

Configuration

Configure the middleware's behaviour in your Django settings. You must add the hosts that are allowed to do cross-site requests to CORS_ORIGIN_WHITELIST, or set CORS_ORIGIN_ALLOW_ALL to True to allow all hosts.

Set in django setting:
```py
CORS_ORIGIN_ALLOW_ALL = True
```

Refer to :
https://github.com/ottoyiu/django-cors-headers/

Install django-cors-headers from pip:
```bash
$ pip install django-cors-headers
```
and then add it to the installed apps:
```py
INSTALLED_APPS = (
    ...
    'corsheaders',
    ...
)
```

You will also need to add a middleware class to listen in on responses:
```py
MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```

CorsMiddleware should be placed as high as possible, especially before any middleware that can generate responses such as Django's CommonMiddleware or Whitenoise's WhiteNoiseMiddleware. If it is not before, it will not be able to add the CORS headers to these responses.

Also if you are using CORS_REPLACE_HTTPS_REFERER it should be placed before Django's CsrfViewMiddleware.

7. Enable Django Rest Authentication

Use django-rest-auth
http://django-rest-auth.readthedocs.io/en/latest/installation.html#social-authentication-optional

Installation
```bash
$ pip install django-rest-auth
```

Add rest_auth app to INSTALLED_APPS in your django `settings.py`:
```py
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'rest_auth'
)
```

This project depends on django-rest-framework library, so install it if you haven’t done yet. Make sure also you have installed rest_framework and rest_framework.authtoken apps

Add rest_auth urls:
```py
urlpatterns = [
    ...,
    url(r'^rest-auth/', include('rest_auth.urls'))
]
```

Migrate your database
```bash
$ python manage.py migrate
```

Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, groups, profiles, sessions, social_django, thumbnail
Running migrations:
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK

You’re good to go now!

**Login:**

Now change app Loginvue file as: (it uses ‘key’ instead of ‘token’)
```js
    methods: {
      login: function () {
        // let self = this;
        axios.post('http://127.0.0.1:8000/rest-auth/login/', {
          username: this.username,
          password: this.password
        })
          .then((response) => {
            console.log('The user name is: ');
            console.log(this.username);
            console.log('The password is : ');
            console.log(this.password);
            console.log(response.data.key);
            this.$store.dispatch('SET_TOKEN', response.data.key);
            this.$f7.dialog.alert('The user logged in!');
            this.$f7router.navigate('/groups/');
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    }
```

Changed the user to test222, we got different token. More importantly, we don’t need to write a code to generate the token.

**Registration**

If you want to enable standard registration process you will need to install django-allauth by using (don’t forget [with_social]).
```bash
$ pip install django-rest-auth[with_social].
```

Add django.contrib.sites, allauth, allauth.account and rest_auth.registration apps to INSTALLED_APPS in your django settings.py:
```py
# Add SITE_ID = 1 to your django settings.py
INSTALLED_APPS = (
    ...,
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
)

SITE_ID = 1
```

Add rest_auth.registration urls:
```py
urlpatterns = [
    ...,
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
```

Don’t forget to sync your database:
```bash
$ ./manager.py migrate
```
Operations to perform:
  Apply all migrations: account, admin, auth, authtoken, contenttypes, groups, profiles, sessions, sites, social_django, thumbnail
Running migrations:
  Applying account.0001_initial... OK
  Applying account.0002_email_max_length... OK
  Applying sites.0001_initial... OK
  Applying sites.0002_alter_domain_unique... OK

Please see the following link for user registration and how to use django-rest-framework-jwt with django-rest-auth to expire the token. (the default django token will never change).
https://michaelwashburnjr.com/django-user-authentication/#

Changed my Signup.vue as follow:
```js
    methods: {
      login: function () {
        axios.post('http://127.0.0.1:8000/rest-auth/registration/', {
          username: 'test8888',
          password1: 'test1234',
          password2: 'test1234',
          email: 'test8888@test.com'
        })
          .then( (response) => {
            console.log(response.data.key);
            this.$store.dispatch('SET_TOKEN', response.data.key);
          })
          .catch(function (error) {
          console.log(error);
          });
      }
    }
```

It succeeded!


Also noticed, that in admin, a model named ‘Email addresses’ was created under Accounts app. (just one record created for test8888).
A new model named ‘Tokens’ was created under “Auth Token” app. All the tokens are in there.

But when I used postman to test the registration. I got the following error:
"detail": "CSRF Failed: CSRF token missing or incorrect."

# HTTP 403 Forbidden when get /rest-auth/user

Why are you getting this error?

As you have not defined the AUTHENTICATION_CLASSES in your settings, DRF uses the following default authentication classes.
```py
'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication'
)
```

Now, SessionAuthentication enforces the use of CSRF Token. If you don't pass a valid CSRF token, then 403 error is raised.
If you're using an AJAX style API with SessionAuthentication, you'll need to make sure you include a valid CSRF token for any "unsafe" HTTP method calls, such as PUT, PATCH, POST or DELETE requests.

What you need to do then?

Since you are using TokenAuthentication, you need to explicitly define it in the 
https://stackoverflow.com/questions/32602027/django-drf-403-forbidden-csrf-token-missing-or-incorrect

Solution: 

Add TokenAuthentication framework into the REST settings.py
```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
```

So my setting.py for django rest framework will looks like so:
```py
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
CORS_ORIGIN_ALLOW_ALL = True
SITE_ID = 1
```








