from setuptools import setup

from __version__ import __version__

setup(
    name="pytest-twilio-conversations-client-mock",
    description="",
    long_description="",
    author="",
    license="MIT license",
    author_email="",
    url="",
    version=__version__,
    classifiers=[],
    install_requires=[
        "twilio==7.12.0",  # TODO mock depends on TwilioRestException
    ],
)
