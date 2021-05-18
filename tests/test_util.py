"""Test utils function"""
import unittest
import os

from pycolor import utils

# import colors.
COLORS = utils.read_file_json("test_files/test_file.json")


class TestUtil(unittest.TestCase):
    """Test the until functions."""

    def test_read_file(self):
        """> Read colors from a file."""
        result = utils.read_file("test_files/test_file")
        self.assertEqual(result[0], "/home/trkhanh/Pictures/Wallpapers/1.jpg")
