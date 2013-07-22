Related models
==============

:doc:`Basic usage <usage>` of permissions methods focus on individual models.
A common security pattern is a hierarchy of objects that extend permissions
across multiple related models.  Permissions on a parent object may grant
inherent permissions on the children.  This is more efficient storage and cpu
usage than granting individual permissions on every child.

.. code-block:: python

    # example of a hierarchy of models.  Each model grants permissions over
    # models related through Foreign Keys

    class Parent(models.Model):
        """ can control children and toys """
        name = models.CharField(max_length=32)

    class Child(models.Model):
        """ can control toys """
        name = models.CharField(max_length=32)
        parent = models.ForeignKey(Parent, related_name="children")

    class Toy(models.Model):
        """ can only control itself """
        name = models.CharField(max_length=32)
        owner = models.ForeignKey(Child, related_name="toys")

The power of related model queries is that they are able to execute a single
query for what might otherwise be multiple queries.  For methods that return
querysets, such as ``get_objects`` and ``get_users``, this is important since
receiving a single query set allows you to iterate, sort, or paginate your
results easily.

.. versionadded:: 1.3


Related model queries
~~~~~~~~~~~~~~~~~~~~~

Related models are added as keyword arguments to most permissions methods.
Relationship paths are the same as django query paths.  They separate related
names by double underscores.

.. code-block:: python

    # the relationship path from Toy to Child is 'child'
    get_objects_any_perms(toy, perms=['play'], child=['EnterPlayroom'])

Join over intermediary tables
-----------------------------

Related query paths can follow relationships as far as they need to.
Intermediary that are joined over do not need to be registered with object
permissions.  If it is a valid django query path it should work.

.. code-block:: python

    # the relationship path from Toy to Parent is 'child__parent',
    # it spans two models
    get_objects_any_perms(toy, perms=['play'], child__parent=['Clean'])

Multiple related models
-----------------------

Multiple related model queries may be used at the same time.  This allows
permissions to be granted at multiple levels and checked at the same time.

.. code-block:: python

    # include multiple related models
    get_objects_any_perms(toy, perms=['play'], child=['EnterPlayroom'],
                          child__parent=['Clean'])


Limited functionality
~~~~~~~~~~~~~~~~~~~~~

For now, only ``get_objects`` supports related models.  Due to technical
hurdles implementations do not yet exist for other methods.  There are
partially functional implementations of the other methods, but they all have
their own quirks that haven't been worked out yet.

Parent ticket: `#2415 <https://code.osuosl.org/issues/2415>`_.

Tickets with important information: `#2457 <https://code.osuosl.org/issues/2457>`_, `#2481 <https://code.osuosl.org/issues/2481>`_.

Other related tickets: `#2463 <https://code.osuosl.org/issues/2463>`_, `#2469 <https://code.osuosl.org/issues/2469>`_, `#2475 <https://code.osuosl.org/issues/2475>`_, `#2487 <https://code.osuosl.org/issues/2487>`_, `#2493 <https://code.osuosl.org/issues/2493>`_, `#2499 <https://code.osuosl.org/issues/2499>`_.


Performance concerns
~~~~~~~~~~~~~~~~~~~~

Use related models with caution.  Queries generated with related models will
include **outer joins** and with some data sets they may perform poorly.  All
joins should be across indexed fields, but you must ensure that your indexes
are working sufficiently.
