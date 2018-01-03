# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from my.content.testing import MY_CONTENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that my.content is properly installed."""

    layer = MY_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if my.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'my.content'))

    def test_browserlayer(self):
        """Test that IMyContentLayer is registered."""
        from my.content.interfaces import (
            IMyContentLayer)
        from plone.browserlayer import utils
        self.assertIn(IMyContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MY_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['my.content'])

    def test_product_uninstalled(self):
        """Test if my.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'my.content'))

    def test_browserlayer_removed(self):
        """Test that IMyContentLayer is removed."""
        from my.content.interfaces import \
            IMyContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMyContentLayer, utils.registered_layers())
