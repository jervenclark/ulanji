import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ulanji-jervenclark", # Replace with your own username
    version="0.0.1",
    author="Jerven Clark Chua",
    author_email="jervenclark@gmail.com",
    description="Distraction free markdown editor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jervenclark/ulanji",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
