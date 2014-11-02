from setuptools import setup, find_packages

setup(
    name='dantalian',
    version='0.7',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'dantalian = dantalian.main:main',
        ],
    },

    author='Allen Li',
    author_email='darkfeline@abagofapples.com',
    description='File tagging with hard links',
    license='MIT',
    url='http://darkfeline.github.io/dantalian/',
)
