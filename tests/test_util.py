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

    def test_read_file_start(self):
        """> Read colors from a file."""
        result = utils.read_file_json("test_files/test_file.json")
        self.assertEqual(result["colors"]["color0"], "#1F211E")

    def test_read_file_end(self):
        """> Read colors from a file."""
        result = utils.read_file_json("test_files/test_file.json")
        self.assertEqual(result["colors"]["color15"], "#F5F1F4")

    def test_read_wallpaper(self):
        """> Read wallpaper from json file."""
        result = utils.read_file_json("test_files/test_file.json")
        self.assertEqual(result["wallpaper"], "5.png")

    def test_save_file(self):
        """> Save colors to a file."""
        tmp_file = "/tmp/test_file"
        utils.save_file("Hello, world", tmp_file)
        result = os.path.isfile(tmp_file)
        self.assertTrue(result)
