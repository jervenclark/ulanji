import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "ulanji",
    version = "0.0.6",
    author = "Jerven Clark Chua",
    author_email = "jervenclark@gmail.com",
    description = "Distraction free markdown editor",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/jervenclark/ulanji",
    packages = setuptools.find_packages(),
    package_data = {
        'ulanji.gui': ['*.ui'],
        'ulanji.assets': ['*.html']
    },
    include_package_data = True,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    install_requires = [
        'markdown2==2.4.0',
        'PyQt5==5.15.0',
        'PyQtWebEngine==5.15.0',
        'QDarkStyle==2.8.1',
    ]
)
