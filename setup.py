import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

requires = [
    'Kotti',
    'fanstatic'
    ]

setup(name='betahaus_net_site',
      version='0.1dev',
      description='betahaus_net_site',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Betahaus',
      author_email='robin@betahaus.net',
      url='http://www.betahaus.net',
      keywords='web pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      tests_require= requires,
      test_suite="betahaus_net_site",
      entry_points = """\
      [paste.app_factory]
      main = betahaus_net_site:main
      [fanstatic.libraries]
      betahaus_net_lib = betahaus_net_site:betahaus_net_lib
      """,
      message_extractors = { '.': [
          ('**.py',   'lingua_python', None ),
          ('**.pt',   'lingua_xml', None ),
          ]},
      )

