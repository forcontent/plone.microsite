# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.microsite.interfaces import IMicrosite
from zope.interface import implementer


@implementer(IMicrosite)
class Microsite(Container):
    """ A microsite. """
