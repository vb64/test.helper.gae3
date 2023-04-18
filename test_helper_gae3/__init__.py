"""Test helper for GAE Python3 app.

https://cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/testbed/Testbed
"""
from google.appengine.ext import testbed


class TestGae3:
    """Mixing class for GAE testbed use."""

    gae_testbed = None

    def set_up(self):
        """Activate GAE testbed."""
        self.gae_testbed = testbed.Testbed()
        self.gae_testbed.activate()
        # self.gae_testbed.setup_env()
        self.gae_testbed.init_datastore_v3_stub()
        self.gae_testbed.init_memcache_stub()

    def tear_down(self):
        """Deactivate GAE testbed."""
        self.gae_testbed.deactivate()
        self.gae_testbed = None

    def check_db_tables(self, db_state):
        """Check record count in the given GAE ndb Model.

        db_state must be defined as follows:

        db_state = [
          (ModelName, record_count),
        ]
        """
        for table, count in db_state:
            i = len(table.query().fetch(300, keys_only=True))
            assert i == count, "{} items: {} must be {}".format(
              table._get_kind(),  # pylint: disable=protected-access
              i,
              count
            )
