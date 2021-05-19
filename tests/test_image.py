import unittest

from pycolor import image


class MyTestCase(unittest.TestCase):
    def test_get_img(self):
        """> validate image file."""
        result = image.get("/test_files/test.jpg")
        self.assertIn("/test_files/test.jpg", result)

    def test_get_image_dir(self):
        """> validate image directory."""
        result = image.get("/test_files")
        self.assertEqual(result.endswith(".jpg", ".png"), True)

    def test_get_image_fail(self):
        """> Validate image. (fail)"""
        with self.assertRaises(SystemExit):
            image.get("/test_files/test_fail.jpg")

    def test_get_img_dir_fail(self):
        """> Validate image directory. (fail)"""
        with self.assertRaises(SystemExit):
            image.get('tests')


if __name__ == '__main__':
    unittest.main()
