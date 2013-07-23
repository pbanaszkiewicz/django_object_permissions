Signals
=======

Django includes a `signal dispatcher`_ which helps decoupled applications
get notified when actions occur elsewhere in the framework.  In a nutshell,
signals allow certain senders to notify a set of receivers that some action
has taken place.  They’re especially useful when many pieces of code may be
interested in the same events.

.. _signal dispatcher: http://docs.djangoproject.com/en/dev/topics/signals/

.. code-block:: python

    from object_permissions.signals import granted

    def my_receiver(sender, perm, obj,  **kwargs)
        """ simple signal receiver that doesn't actually do anything """
        pass

    # connect to all signals
    granted.connect(my_receiver)

    # connect filtering based on sender
    granted.connect(my_receiver, sender=MyModel)


Permissions signals
~~~~~~~~~~~~~~~~~~~

Signals are provided for both **grant** and **revoke** operations.  Each
permission that is granted or revoked is sent as a separate signal and only
sent when permissions actually change.  This includes methods such as
``user.set_perms()`` and ``user.revoke_all()`` which set multiple permissions
at the same time.

.. code-block:: python

    # signal sent
    user.grant('Foo', bar)

    # signal not sent, user was already granted Foo permission
    user.grant('Foo', bar)


.. function:: object_permissions.signals.granted(sender, perm, obj, **kwargs)

    Sent whenever **grant** operation is performed.

    :param sender: the model sending the signal
    :param perm: the permission that was granted
    :param obj: the model instance permission were granted to


.. function:: object_permissions.signals.revoked(sender, perm, obj, **kwargs)

    Sent whenever **revoke** operation is performed.  This include "bulk"
    operations like **revoke_all**.

    :param sender: the model sending the signal
    :param perm: the permission that was revoked
    :param obj: the model instance permission were revoked from


View signals
~~~~~~~~~~~~

.. versionadded:: 1.3

Object permissions provides a set of :doc:`views <views_templates>` for
editing groups and permissions.  It also provides high level signals issues
for adding or removing users, and editing user permissions.  These signals
differ from signals by including the user who is editing.  These signals are
also higher level and support the concept of permission based membership.

.. function:: object_permissions.signals.view_add_user(sender, editor, user, obj, **kwargs)

    Called whenever a **user** is added to an object as a member.  For objects
    with permission based membership this signal is sent when a **user** is
    granted it's initial permissions.

    :param sender: the model a user is being added to
    :param editor: the user who is adding the user
    :param user: the user or group who is being added
    :param obj: the object the user is being granted membership to

.. function:: object_permissions.signals.view_remove_user(sender, editor, user, obj, **kwargs)

    Called whenever a **user** has its membership revoked for an object.  For
    objects with permission based membership this signal is sent when
    a **user** has all of its permissions revoked.

    :param sender: the model a user is being removed from
    :param editor: the user who is removing the user
    :param user: the user or group who is being removed
    :param obj: the object membership is being revoked for

.. function:: object_permissions.signals.view_edit_user(sender, editor, user, obj, **kwargs)

    Sent whenever permissions are modified.  For permission based membership
    this signal is not sent if all permissions are revoked or a user is being
    added.

    :param sender: the model class of the object being edited
    :param editor: the user who is editing permissions
    :param user: the user or group whose permissions are being edited
    :param obj: the object permissions are being edited for
