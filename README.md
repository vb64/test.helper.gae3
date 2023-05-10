# Class for autotests GoogleAppEngine Python3 app.

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/test.helper.gae3/pep257.yml?label=Pep257&style=plastic&branch=main)](https://github.com/vb64/test.helper.gae3/actions?query=workflow%3Apep257)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/test.helper.gae3/py3.yml?label=Python%203.7-3.10&style=plastic&branch=main)](https://github.com/vb64/test.helper.gae3/actions?query=workflow%3Apy3)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/abee606aca3047f9952c43196aa5d2b7)](https://app.codacy.com/gh/vb64/test.helper.gae3/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/abee606aca3047f9952c43196aa5d2b7)](https://app.codacy.com/gh/vb64/test.helper.gae3/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

## Install
```bash
pip install test-helper-gae3
```

## Usage in tests

```python
import unittest
from google.appengine.ext import ndb
from test_helper_gae3 import TestGae3


class ModelTest(ndb.Model):
    name = ndb.StringProperty(default='')


class TestCase(unittest.TestCase, TestGae3):

    def setUp(self):
        super().setUp()

        # For using queues names other then 'default', root_path dir must contain file
        # 'queue.yaml' (or 'queue.yml') with correct queues definition.
        # If root_path set to None, only 'default' queue is available.
        TestGae3.set_up(self, 'path/to/folder/with/queue.yaml')  # activate GAE testbed

    def tearDown(self):
        TestGae3.tear_down(self)  # deactivate GAE testbed
        super().tearDown()

    def test_record_count(self):
        self.check_db_tables([
          (ModelTest, 0),  # no records in ModelTest
        ])

        ModelTest().put()

        self.tester.check_db_tables([
          (ModelTest, 1),  # one record in ModelTest
        ])

```
