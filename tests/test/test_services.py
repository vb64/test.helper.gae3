"""GAE tester services.

make test T=test_services.py
"""
from . import TestCase


class TestServices(TestCase):
    """Test GAE services."""

    def setUp(self):
        """Create tester instance."""
        super().setUp()

        from test_helper_gae3 import TestGae3

        self.tester = TestGae3()
        self.tester.set_up()

    def tearDown(self):
        """Deactivate tester."""
        self.tester.tear_down()
        super().tearDown()

    def test_check_db_tables(self):
        """Method check_db_tables."""
