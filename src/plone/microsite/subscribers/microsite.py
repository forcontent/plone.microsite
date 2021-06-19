# -*- coding: utf-8 -*-
from plone.microsite import ADD_PERMISSION
from plone.subrequest import subrequest


def change_add_permission(object, event):
    """Remove all roles from 'plone.microsite: Add Microsite' permission inside
    a Microsite. We do that to avoid having a Microsite inside a Microsite.
    """
    object.manage_permission(ADD_PERMISSION, roles=[])


def set_metadata(obj, event):
    """ Save metadata on local registry """
    # When using /_vh_ subpaths it is safer to use this approach
    base = '/'.join(obj.getPhysicalPath())
    metadata_setter = subrequest(base + '/@@microsite-metadata-setter')  # noqa
