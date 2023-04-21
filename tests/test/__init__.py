"""Root class for testing."""
import os
import unittest


class TestCase(unittest.TestCase):
    """Inherit unittest."""

    proj_dir = os.path.join('tests', 'gae')
