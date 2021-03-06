# -*- coding: utf-8 -*-
from collective.behavior.localregistry.behavior import ILocalRegistry
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.microsite import _
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IMicrositeLocalRegistry(model.Schema):
    """ Microsite Schema """

    microsite_logo = namedfile.NamedBlobImage(
        title=_(u'logo_field_title', default=u'Microsite Logo'),
        description=_(u'logo_field_description', default=u''),
        required=False,
    )

    directives.order_before(microsite_logo='ILocalDiazo.theme')


@implementer(IMicrositeLocalRegistry)
@adapter(ILocalRegistry)
class MicrositeLocalRegistry:

    def __init__(self, context):
        self.context = context
