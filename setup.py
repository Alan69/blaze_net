from setuptools import setup, find_packages

setup(
    name='blaze-net',
    version='1.0.1',
    author='McLovinAlan69',
    author_email='gameg1676@gmail.com',
    description='A Python web framework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Alan69/blaze_net',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
    ],
    install_requires=[
        'werkzeug',
        'jinja2',
        'sqlalchemy',
    ],
)
