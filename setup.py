from setuptools import setup

def main():
    setup(name='tripsmodule',
          version='1.0.0',
          description='Python TripsModule',
          long_description='surgically removed from bioagents',
          author='Benjamin Gyori',
          author_email='benjamin_gyori@hms.harvard.edu',
          url='http://github.com/mrmechko/bioagents',
          packages=['tripsmodule'],
          #install_requires=['pysb', 'objectpath', 'rdflib',
          #                  'functools32', 'requests', 'lxml',
          #                  'pandas', 'suds'],
          #include_package_data=True,
          keywords=['nlp'],
          classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.5',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            'Topic :: Scientific/Engineering :: Chemistry',
            'Topic :: Scientific/Engineering :: Mathematics',
            ],
          )
if __name__ == '__main__':
    main()
