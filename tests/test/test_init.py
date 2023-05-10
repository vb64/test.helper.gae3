"""GAE tester.

make test T=test_init.py
"""
from . import TestCase


class TestInitTestbed(TestCase):
    """Test GAE tester."""

    def test_init(self):
        """Activate and deacivate tester."""
        from test_helper_gae3 import TestGae3

        tester = TestGae3()
        assert tester.gae_testbed is None

        tester.set_up(None)
        assert tester.gae_testbed is not None

        tester.tear_down()
        assert tester.gae_testbed is None
