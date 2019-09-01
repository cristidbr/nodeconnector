from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='nodeconnector',
      version='1.0.0',
      description='Python connector module for Node.JS applications',
      url='https://github.com/cristidbr/nodeconnector',
      author='Cristian Dobre',
      author_email='cristian.dobre@hbfsrobotics.com',
      license='MIT',
      packages=['nodeconnector'],
      install_requires=[
          'pyzmq',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)