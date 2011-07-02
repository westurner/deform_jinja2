import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.txt')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except:
    README = ''
    CHANGES = ''

requires = ['deform']

setupkw = dict(
    name='deform_mako',
    version='0.0.0',
    description='Mako templates for Deform widgets',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        ],
    keywords='web forms form generation schema validation',
    author="Somebody",
    author_email="somebody@example.com",
    url="http://example.com",
    license="some license",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points = """\
    [paste.app_factory]
    demo = deformdemo.app:run
    """,
    )

setup(**setupkw)
