"""GAE services."""
from .. import TestCase


class TestServices(TestCase):
    """Test GAE services."""

    def setUp(self):
        """Create tester instance."""
        super().setUp()

        from test_helper_gae3 import TestGae3

        self.tester = TestGae3()
        self.tester.set_up(None)

    def tearDown(self):
        """Deactivate tester."""
        self.tester.tear_down()
        super().tearDown()
