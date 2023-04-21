"""Datastore service.

make test T=test_services/test_datastore.py
"""
import pytest
from google.appengine.ext import ndb
from . import TestServices


class ModelTest(ndb.Model):
    """Model for tests."""

    name = ndb.StringProperty(default='')


class TestDatastore(TestServices):
    """Test GAE Datastore service."""

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
