# ecommerce-with-django-and-vue

- pip installs done
    - `django`
    - `django-cors-headers`
    - `django-rest-framework` - for API
    - `django-cors-headers` - for security
    - `djoser` - for authentication, create user ,login, token for auth, etc...
    - `pillow` - for image upload, resize, etc...
    - `stripe` - for payment

- `django-admin startproject djackets_django .` - create project

- `settings.py` is the main settings file for the project
- `urls.py` is the main urls file for the project
- `wsgi.py` is the main wsgi file for the project
- `asgi.py` is the main asgi file for the project
- `manage.py` is the main manage file for the project

## step 2

- add the following to `settings.py` file installed apps part

```
'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
```
- under that add the following

```
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]
```

- add this before common middleware

```
'corsheaders.middleware.CorsMiddleware',
```

- go to url and remove the comment and add the following

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('djoser.urls')),
    path('api/v1',include('djoser.urls.authtoken')),
]

```

- do `py manage.py makemigrations` - to create migrations - this will create a db.sqlite3 file
- then do `py manage.py migrate` - to migrate the migrations to the db
- create superuser by doing `py manage.py createsuperuser`
- add name, email and password

- do `py manage.py runserver` - to run the server
- since we dont have any url '/' it will show an error, so we will got to /admin and login with the superuser credentials

- under users we can see the superuser we created

# lets start VUE

- to start vue we have to install cli globally by doing `npm install -g @vue/cli`
- create a new vue project by doing `vue create djackets_vue` - this will create a new folder djackets_vue with all the files  and folders needed for vue project and will ask you to select the features you want to use for the project  - we will select the following
    - Babel for transpiling JS code to ES5 syntax for older browsers support (default) 
    - Router for SPA routing (default) 
    - Vuex for state management (default) 
    - CSS Pre-processors - SASS/SCSS (with dart-sass)
    - choose vue version
    - Note: press space to select features, then enter to confirm your choices

- after the project is created, now install `npm install axios` - for api calls and `npm install bulma` - for css framework

- lets explore the djackets_vue folder
    - `node_modules` - all the packages installed
    - `public` - all the public files like index.html and favicon
    - `src` - all the source files like main.js, App.vue, etc... 
    - router folder - all the routes
    - store folder - all the vuex files like state, mutations, actions, etc...
    - views folder - all the views like home.vue, about.vue, etc...
    - main.js - main js file for the project 
    - components folder - all the components like navbar.vue, footer.vue, etc... 
    - `package.json` - all the packages installed
    - `package-lock.json` - all the packages installed
    - `README.md` - readme file
    - `babel.config.js` - babel config file
    - `vue.config.js` - vue config file

- lets start the project by doing `npm run serve` - this will start the project and open the browser with the url `http://localhost:8080/` 
- we need to include font awesome icons,so the cdn if cloudflare is `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css` - add this to the index.html file in the public folder

- lets setup base template, go to app.vue file in the src folder and remove everything inside style and template tags and add the following

```
add `@import '../node_modules/bulma';` to the style tag
```

```

- app.vue file  - this is the base template for the project
- home.vue file - this is the home page for the project
- about.vue file - this is the about page for the project

- lets create an app for the project, go to the terminal and do `py manage.py startapp product` - this will create a jackets folder with all the files and folders needed for the app

- add category model in the models.py file

- then go to settings.py file and add the product app to the installed apps

- then do `py manage.py makemigrations` - to create migrations called 0001_initial.py in the migrations folder in the product folder 
- then do `py manage.py migrate` - to migrate the migrations to the db

- lets add product model in the models.py file and then do `py manage.py makemigrations` - to create migrations called 0002_product.py in the migrations folder in the product folder

- then do `py manage.py migrate` - to migrate the migrations to the db

- we also need to fix the uploads folder, so go to settings.py file and add the following

```
MEDIA_URL = '/media/'
MEDIA_ROOT=BASE_DIR / 'media/'
```

- now go to urls.py file and add the following

```
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
so that we can access the media folder from the browser by going to `http://localhost:8000/media/` 

- lets create a serializer.py file in the product folder so that we can serialize the data from the db to json format

- lets go to views.py file to create the views for the product app

- also create a urls.py file in the product folder so that we can create the urls for the product app
- and import this urls.py file in the main urls.py file

- at this stage if we go to `http://127.0.0.1:8000/api/v1/latest-products/` we get empty array, so lets add some data to the db

- go to admin.py file in product and register the models so that we can add data from the admin panel 
```
from .models import Category, Product 
admin.site.register(Category)
admin.site.register(Product)
```

now go to `http://127.0.0.1:8000/admin/` and login with the superuser credentials, you will see the category and product models in the admin panel and you can add data to the db from there 

- add two categoried and one product for each category

- lets go to Homeview.vue file

- axios is a promise based HTTP client for the browser and node.js. It basically makes it easy to make HTTP requests to fetch or save data. It can be used in plain JavaScript or with a library such as Vue or React. It supports the Promise API that is native to JavaScript ES6. It also supports an async / await syntax for cleaner asynchronous code. It can be used in plain JavaScript or with a library such as Vue or React. It supports the Promise API that is native to JavaScript ES6. It also supports an async / await syntax for cleaner asynchronous code. it is more like a fetch api but it is more powerful and easier to use.
- so in homeview.vue file we are using axios to fetch the data from the api and then we are using v-for to loop through the data and display it in the template.we pass it method

- now we need to add the base url to the axios, so go to main.js file and add the following
```
axios.defaults.baseURL="http://127.0.0.1:8000"
createApp(App).use(store).use(router,axios ).mount('#app')
```

- go to views.py file and add the following
```
ProductDetail class - this will return the product detail page
``` 

- now go to urls.py file and add the following
```
path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),

```

- create a new Product.vue file in the views folder

- now go to index.js file in router and do 