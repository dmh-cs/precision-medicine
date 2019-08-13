from setuptools import setup

setup(
  name='precision_medicine',
  version='0.0.1',
  install_requires=['lxml'],
  extras_require={
    'dev': [
      'pylint',
      'ipdb',
      'pip',
      'pip-tools'
    ]
  }
)
