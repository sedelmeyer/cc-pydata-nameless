import logging
from unittest import TestCase

from cc_pydata_nameless.cli import main


def test_main():
    main([])


class TestNullHandler(TestCase):
    """Test default logger is initialized with module"""

    def test_default_logging_handler(self):
        """Ensure only one handler is initialized by default"""
        logger = logging.getLogger('cc_pydata_nameless')
        self.assertEqual(len(logger.handlers), 1)

    def test_logging_nullhandler(self):
        """Ensure logging.nullHandler is initialized with module"""
        logger = logging.getLogger('cc_pydata_nameless')
        self.assertIsInstance(logger.handlers[0], logging.NullHandler)
