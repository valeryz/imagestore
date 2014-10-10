#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ImagestoreApp(CMSApp):
    name = _("Imagestore App") # give your app a name, this is required
    urls = ["imagestore.imagestore_cms.urls"] # link your app to url configuration(s)

# valeryz: Disabling the app, using only as a plugin, apps make
# deployment a pain because of import time database access
# apphook_pool.register(ImagestoreApp) # register your app
