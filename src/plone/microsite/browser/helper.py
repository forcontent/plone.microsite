# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.Five import BrowserView
from plone.memoize.view import memoize
from plone.memoize.view import memoize_contextless
from zope.interface import Interface
from zope.interface import implementer


class IHelperView(Interface):

    """ Microsite helpers."""

    def enabled():
        """ Validates if the viewlet should be enabled for this context. """

    def microsite_root():
        """ Return a Microsite Object """

    def microsite_logo(site_url):
        """ Return a Microsite Logo Url """


@implementer(IHelperView)
class HelperView(BrowserView):

    def __init__(self, context, request):
        self.context = aq_inner(context)
        self.request = request

    @memoize_contextless
    def microsite_root(self):
        microsite_type = u'plone.microsite'
        context = self.context

        if microsite_type in context.portal_type:
            return context
        else:
            for item in context.aq_chain:
                if microsite_type in getattr(item, 'portal_type', ''):
                    return item

    @memoize_contextless
    def microsite_logo(self, site_url):
        return '%s/@@microsite-logo/micrositelogo' % (site_url)

    @memoize
    def enabled(self):
        if self.microsite_root():
            return True
