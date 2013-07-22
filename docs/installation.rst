Installation
============

To install Django Object Permissions, simply pull it from PyPI:

::

  pip install django-object-permissions

If you want to have the latest version, you can clone git repository:

::

  git clone git://git.osuosl.org/gitolite/django/django_object_permissions

Then you'd have to manually install it:

::

  python setup.py install


Configuration
=============

1. Add ``object_permissions`` to your project's ``INSTALLED_APPS`` setting.
2. Add ``object_permissions.backend.ObjectPermBackend`` to your project's
   ``AUTHENTICATION_BACKENDS``.
3. Synchronize your database: ``./manage.py sync``

Testing
=======

The unittests provided by Object Permissions requires ``TESTING`` to be set to
``True`` in ``settings.py``. This setting instructs Object Permissions to
create a set of test tables needed for unittests.
