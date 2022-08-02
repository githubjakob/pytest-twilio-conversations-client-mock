from setuptools import setup

setup(
    name="pytest-twilio-conversations-client-mock",
    description="",
    long_description="",
    author="Jakob",
    license="GPL-3.0-or-later",
    author_email="hello@jakobzanker.de",
    url="https://github.com/githubjakob/pytest-twilio-conversations-client-mock",
    version="0.0.2",
    classifiers=[],
    packages=["twilio_conversations_mock"],
    install_requires=[
        "twilio==7.12.0",  # TODO mock depends on TwilioRestException
    ],
)
