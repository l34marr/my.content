# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from my.content.interfaces import IFolklore
from my.content.testing import MY_CONTENT_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class FolkloreIntegrationTest(unittest.TestCase):

    layer = MY_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Folklore')
        schema = fti.lookupSchema()
        self.assertEqual(IFolklore, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Folklore')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Folklore')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IFolklore.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Folklore',
            id='Folklore',
        )
        self.assertTrue(IFolklore.providedBy(obj))
