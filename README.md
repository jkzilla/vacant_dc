# Vacant DC

Vacant DC shows vacant retail locations across Washington, D.C.

Detailed documentation is in the "docs" directory.

## Quick start


1. Add "vacant-dc.apps.VacantDc2Config" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
	    'vacant-dc.apps.VacantDc2Config',,
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^vacant-dc/', include('vacant-dc.urls')),

3. Run `python manage.py migrate` to create the Vacant DC models.

4. Start the development server

To run this application from your local machine:

```
python manage.py runserver
```
5. Visit http://127.0.0.1:8000/admin/
   (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/vacant-dc/index.html to visit the map.


## Notes

Access the database:

```
psql vacant_dc
```

User:
vacant_dc_user

Password:
