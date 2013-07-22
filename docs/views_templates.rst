Views
=====

This app provides generic views and templates to quickly add permissions
editing for an object.

URLs
~~~~

* add user or group: ``<base>``
* edit user: ``<base>/user/<id>``
* edit group: ``<base>/group/<id>``

Views
~~~~~

Generic views for displaying and editing permissions object permissions.  These
views expect that you have already done permissions checking and loaded the
object prior to calling these views.

.. autofunction:: object_permissions.views.permissions.view_users

.. autofunction:: object_permissions.views.permissions.view_permissions

Example:

.. code-block:: python

    from object_permissions.views.permissions import view_users, view_permissions

    @login_required
    def view1(request, object_id):
        object = get_object_or_404(MyModel, id=object_id)
        return view_users(request, object)

    @login_required
    def view2(request, object_id):
        object = get_object_or_404(MyModel, id=object_id)
        return view_permissions(request, object)

Templates
=========

Templates
~~~~~~~~~

The templates render a list of Users and UserGroups for the object.  The list
uses AJAX to edit the list of Users and their permissions.  The views are
customizable if you need to add custom properties.

``permissions/users.html``
    The main template. Includes a list of users and javascript for editing
    them.

    Blocks:

    * ``head``: for additional javascript or css tags,
    * ``table_headers``: headers for additional columns in the table.

``permissions/user_row.html``
    Renders a single user row.

    Blocks:

    * ``table_cells``: additional table cells to add to the row.

``permissions/group_row.html``
    Renders a single UserGroup row.

    Blocks:

    * ``table_cells``: additional table cells to add to the row.

``permissions/form.html``
    Form that is used for editing permissions.  This form will render widgets
    for selecting a User or UserGroup if neither is provided.

Form classes
~~~~~~~~~~~~

.. autoclass:: object_permissions.views.permissions.ObjectPermissionForm

.. autoclass:: object_permissions.views.permissions.ObjectPermissionFormNewUsers
