from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="florican",
    version="0.1.0",
    description=(
        "A tool for monitoring over SSH and getting notified on your favorite channels! "
        "It runs every 5 minutes and notifies if something goes wrong!"
    ),
    license="MIT",
    long_description=long_description,
    author="Kundan Singh (@ksh7)",
    long_description_content_type="text/markdown",
    url="https://github.com/ksh7/florican/",
    packages=["florican", "florican.notifiers"],
    scripts=["scripts/florican"],
    install_requires=[
        "huey==2.4.2",
        "PyYAML==6.0",
        "tinydb==4.7",
        "typing_extensions==4.1.1",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Huey",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: System :: Monitoring",
    ],
)
