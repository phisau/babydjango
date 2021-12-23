=========
Babystats
=========

Babystats is a Django app to conduct web-based statistics around a baby. For each task (e.g. diaper change, breast feeding), visitors can track the time and other properties.

Detailed documentatino is in the "docs" directory.

Quick start
===========


1. Add "babystats" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'babystats',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('babystats/', include('babystats.urls')),

3. Run ``python manage.py migrate`` to create the babystats models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a your different tasks (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/babystats/dashboard to start your tasks.
