# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.app.layout.viewlets.common import LogoViewlet
from plone.formwidget.namedfile.converter import b64encode_file
from plone.namedfile.browser import Download
from plone.registry import Record
from plone.registry import field
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


class LocalRegistrySetter(BrowserView):
    """ Utility view to set metadata in the local registry,
        we need to work in a subrequest to get the local registry.
    """

    def __call__(self):
        """ Save metadata on local registry """
        registry = getUtility(IRegistry)
        logo_key = 'plone.microsite.logo'
        logo = getattr(self.context, 'microsite_logo', False)

        if registry != self.context['local_registry']:
            return

        if logo:
            logo_b64 = b64encode_file(logo.filename, logo.data)
            if logo_key not in registry.records:
                registry.records[logo_key] = Record(
                    field.TextLine(title=u"Micro Site Logo"), u"")
        else:
            logo_b64 = u""

        site_logo = registry.records[logo_key]
        setattr(site_logo, 'value', logo_b64.decode('utf-8'))


class MicroSiteLogo(Download):
    """ """

    def __init__(self, context, request):
        super(MicroSiteLogo, self).__init__(context, request)
        self.filename = None
        self.data = None
        registry = getUtility(IRegistry)

        if registry != self.context['local_registry']:
            return

        logo = getattr(registry, 'microsite_logo', False)

        if logo:
            self.data = logo
            self.filename = logo.filename

    def _getFile(self):
        return self.data


class MicrositeLogoViewlet(LogoViewlet):
    """ Override Plone logo viewlet """
    index = ViewPageTemplateFile("templates/logo.pt")

    def update(self):
        super(MicrositeLogoViewlet, self).update()
        self.isMicrosite = False
        self.hasMicrositeLogo = False

        microsite = self.get_microsite_root
        self.portal_root_url = api.portal.get().absolute_url()

        if microsite:
            self.isMicrosite = True
            self.microsite_title = microsite.title_or_id()
            self.microsite_url = microsite.absolute_url()

            if getattr(microsite, 'microsite_logo', False):
                self.hasMicrositeLogo = True
                self.microsite_logo = self.get_microsite_logo(self.microsite_url)

    @property
    def get_microsite_root(self):
        microsite_type = u'plone.microsite'
        context = self.context

        if microsite_type in context.portal_type:
            return context
        else:
            for item in context.aq_chain:
                if microsite_type in getattr(item, 'portal_type', ''):
                    return item

    def get_microsite_logo(self, site_url):
        return '%s/@@microsite-logo/micrositelogo' % (site_url)