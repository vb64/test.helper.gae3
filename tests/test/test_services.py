"""GAE tester services.

make test T=test_services.py
"""
import pytest
from google.appengine.ext import ndb
from . import TestCase


class ModelTest(ndb.Model):
    """Model for tests."""

    name = ndb.StringProperty(default='')


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
        self.tester.check_db_tables([
          (ModelTest, 0),
        ])

        ModelTest().put()

        self.tester.check_db_tables([
          (ModelTest, 1),
        ])

        with pytest.raises(AssertionError) as err:
            self.tester.check_db_tables([
              (ModelTest, 2),
            ])
        assert 'must be 2' in str(err.value)
