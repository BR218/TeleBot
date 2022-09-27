from setuptools import setup, find_packages
from TeleBot import __version__
setup(
    name='TeleBot',
    version=__version__,
    description='A framework for telegram bot',
    url='https://github.com/BR218/TeleBot.git',
    author='Rudransh Jagannath',
    author_email='jrudransh@protonmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'python-telegram-bot~=13.14',
        'cryptography~=38.0.1',
        'jinja2~=3.1.2',
    ],
    classifiers=[
        'Development Status :: In Progress',
        'Intended Audience :: Python/Framework',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    entry_points={
        'console_scripts': ['telebot = TeleBot.main:command'],
    }
)
