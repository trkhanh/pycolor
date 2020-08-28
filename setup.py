"""wal - setup.py"""
import sys
import setuptools

try:
    import cobot
except ImportError:
    print("error: cobot requires Python 3.5 or greater.")
    sys.exit(1)

LONG_DESC = open('README.md').read()
VERSION = cobot.__version__
DOWNLOAD = "https://github.com/trkhanh/cobot/archive/%s.tar.gz" % VERSION

setuptools.setup(
    name="cobot",
    version=VERSION,
    author="Tran Khanh",
    author_email="trkhanh8@gmail.com",
    description="Generate and change color-context-generator-base on the fly",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    keywords="wal colorscheme terminal-emulators changing-colorschemes",
    license="MIT",
    url="https://github.com/trkhanh/cobot",
    download_url=DOWNLOAD,
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["cobot"],
    entry_points={"console_scripts": ["wal=cobot.__main__:main"]},
    python_requires=">=3.5",
    test_suite="tests",
    include_package_data=True,
    zip_safe=False)
