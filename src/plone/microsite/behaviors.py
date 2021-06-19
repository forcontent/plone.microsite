# -*- coding: utf-8 -*-
from collective.behavior.localregistry.behavior import ILocalRegistry
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.microsite import _
from plone.namedfile import field as namedfile
from zope.interface import provider


@provider(IFormFieldProvider)
class IMicrositeLocalRegistry(ILocalRegistry):
    """ Microsite Schema """
    # model.fieldset('default', fields=['microsite_name'])

    microsite_logo = namedfile.NamedBlobImage(
        title=_(u'logo_field_title', default=u'Microsite Logo'),
        description=_(u'logo_field_description', default=u''),
        required=False,
    )

    directives.order_before(microsite_logo='ILocalDiazo.theme')
