from django.test import TestCase

from jesFinance.apps import jesFinanceConfig


class AppConfigTest(TestCase):
    def test(self):
        self.assertEqual(jesFinanceConfig.name, 'jesFinance')
