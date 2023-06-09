"""TaskQueue service.

make test T=test_services/test_task_queue.py
"""
import pytest
from flask import Flask
from google.appengine.api.taskqueue import Queue, Task
from . import TestServices


class TestTaskQueue(TestServices):
    """Test GAE TaskQueue service."""

    def setUp(self):
        """Queue with one Task."""
        super().setUp()
        self.queue = Queue('default')
        self.queue.add(Task('xxx', url='/'))

    def test_queue(self):
        """Check for number of tasks in queue."""
        self.tester.assert_tasks_num(1)
        tasks = self.tester.gae_tasks(queue_name='default', flush_queue=False)

        assert len(tasks) == 1
        self.tester.assert_tasks_num(1)

        tasks = self.tester.gae_tasks(queue_name='default', flush_queue=True)
        assert len(tasks) == 1
        self.tester.assert_tasks_num(0)

        with pytest.raises(AssertionError) as err:
            self.tester.assert_tasks_num(1)
        assert 'task count: 0' in str(err.value)

    def test_dict(self):
        """Get queue content as dict."""
        data = self.tester.gae_tasks_dict()
        assert len(data) == 1
        assert 'task1' in data

    def test_dump(self):
        """Dump queue content."""
        self.tester.gae_queue_dump()
        self.tester.gae_queue_dump(fields=['name', 'url'])

    def test_flask_execute(self):
        """Execute queue in fask app context."""
        app = Flask(__name__)
        app.config['TESTING'] = True

        @app.route('/', methods=['POST'])
        def root_page():
            """Flask view."""
            return 'OK'

        client = app.test_client()

        data = self.tester.gae_tasks_dict()
        assert len(data) == 1
        task = data[list(data.keys())[0]]

        self.tester.gae_task_flask_execute(task, client, is_delete=False, is_debug_print=True)
        data = self.tester.gae_tasks_dict()
        assert len(data) == 1

        self.tester.gae_task_flask_execute(task, client, is_debug_print=True)
        data = self.tester.gae_tasks_dict()
        assert not data

        self.queue.add(Task('xxx', url='/'))

        self.tester.gae_queue_flask_execute(client)
        data = self.tester.gae_tasks_dict()
        assert not data
