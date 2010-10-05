from django.conf.urls.defaults import *

cluster = 'cluster/(?P<cluster_slug>\w+)'
instance = '/(?P<instance>[^/]+)'

urlpatterns = patterns('ganeti_webmgr.ganeti.views.general',
    # Example:
    # (r'^ganeti_webmgr/', include('ganeti_webmgr.foo.urls')),
    url(r'^$', 'index', name="cluster-overview"),
    #   Orphans
    url(r'^orphans/','orphans', name='instance-orphans'),
    # Authentication
    url(r'^accounts/login/?', 'login_view', name="login"),
    url(r'^accounts/logout/?', 'logout_view', name="logout"),
)

# Clusters
urlpatterns += patterns('ganeti_webmgr.ganeti.views.cluster',
    #   List
    url(r'^clusters/$', 'list', name="cluster-list"),
    #   Detail
    url(r'^%s/?$' % cluster, 'detail', name="cluster-detail"),
    url(r'^%s/users/?$' % cluster, 'cluster_users', name="cluster-users"),
    url(r'^%s/user/?$' % cluster, 'permissions', name="cluster-permissions"),
    url(r'^%s/user/quota/?$'% cluster, 'quota', name="cluster-quota"),
)

# Instances
prefix = '%s%s' %  (cluster, instance)
urlpatterns += patterns('ganeti_webmgr.ganeti.views.virtual_machines',
    #  List
    url(r'^vms/$', 'list', name="virtualmachine-list"),
    #  Detail
    url(r'^%s' % prefix, 'detail', name="instance-detail"),
    #  Create
    url(r'^create/$', 'create', name="instance-create"),
    url(r'^create/(?P<cluster_slug>\w+)$', 'create', name="instance-create"),
    #  Start, Stop, Reboot
    url(r'^%s/vnc/?$' % prefix, 'vnc', name="instance-vnc"),
    url(r'^%s/shutdown/?$' % prefix, 'shutdown', name="instance-shutdown"),
    url(r'^%s/startup/?$' % prefix, 'startup', name="instance-startup"),
    url(r'^%s/reboot/?$' % prefix, 'reboot', name="instance-reboot"),
)