# -*- coding: utf-8 -*-
from plone.supermodel import model
from zope.interface import Interface


class IMicrositeLayer(Interface):
    """Marker interface that defines a browser layer."""


class IMicrosite(model.Schema):
    """A microsite."""
