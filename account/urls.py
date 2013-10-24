from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^login/$', 'account.views.auth_login', name="auth_login"),
    url(r'^logout/$', 'account.views.auth_logout', name="auth_logout"),
    url(r'^gastropin/$', 'account.views.gastropin', name='gastropin'),
    url(r'^wlan_presence/$', 'account.views.wlan_presence', name='wlan_presence'),
    url(r'^rfid/$', 'account.views.rfid', name='rfid'),
    url(r'^groups/(?P<group_name>[^/]+)/', 'account.views.groups_list'),
)