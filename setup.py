from setuptools import setup

setup(name='ctkapi',
      version='1.0',
      description='Spend SDK for third party integration',
      url='https://github.com/SpendSystem/SDK-Python.git',
      author='spend',
      author_email='support@ax.net',
      license='MIT',
      packages=['ctkapi'],
      install_requires=[
          'requests',
           "pyyaml",
           
      ],
      zip_safe=False)
