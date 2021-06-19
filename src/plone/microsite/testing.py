# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing.zope import WSGI_SERVER_FIXTURE


class IMicrositeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plone.microsite)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.microsite:default')


MICROSITE_FIXTURE = IMicrositeLayer()


MICROSITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MICROSITE_FIXTURE,),
    name='MicrositeLayer:IntegrationTesting',
)


MICROSITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MICROSITE_FIXTURE,),
    name='MicrositeLayer:FunctionalTesting',
)


MICROSITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MICROSITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name='MicrositeLayer:AcceptanceTesting',
)
