"""GAE tester.

make test T=test_gae3.py
"""
from . import TestCase


class TestInitTestbed(TestCase):
    """Test GAE tester."""

    def test_init(self):
        """Activate and deacivate tester."""
        from test_helper_gae3 import TestGae3

        tester = TestGae3()
        assert tester.gae_testbed is None

        tester.set_up()
        assert tester.gae_testbed is not None

        tester.tear_down()
        assert tester.gae_testbed is None


class TestServices(TestCase):
    """Test GAE services."""

    def setUp(self):
        """Create tester instance."""
        super.setUp(self)

        from test_helper_gae3 import TestGae3

        self.tester = TestGae3()
        self.tester.set_up()

    def tearDown(self):
        """Deactivate tester."""
        self.tester.tear_down()
        super().tearDown()

    def test_check_db_tables(self):
        """Method check_db_tables."""
