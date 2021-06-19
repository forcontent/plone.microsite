# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory
import logging


_ = MessageFactory('plone.microsite')

PROJECTNAME = __name__
ADD_PERMISSION = 'plone.microsite: Add Microsite'
logger = logging.getLogger(PROJECTNAME)
