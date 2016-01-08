from setuptools import setup

setup(name='prova',
      version='0.1',
      description='prova',
      url='http://github.com/adriaalcala/prova',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['prova'],
      dependency_links=['https://github.com/jkbr/httpie/tarball/master'],
      install_requires=[
          'httpie',
      ],
      zip_safe=False)
