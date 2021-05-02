from setuptools import setup, find_packages

setup(
    name='Entipy',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'attrs==20.3.0',
        'cycler==0.10.0',
        'greenlet==1.0.0',
        'iniconfig==1.1.1',
        'kiwisolver==1.3.1',
        'matplotlib==3.4.1',
        'numpy==1.20.2',
        'packaging==20.9',
        'pandas==1.2.4',
        'pillow==8.2.0',
        'pluggy==0.13.1',
        'py==1.10.0',
        'pyparsing==2.4.7',
        'pytest==6.2.3',
        'python-dateutil==2.8.1',
        'pytz==2021.1',
        'six==1.15.0',
        'sqlalchemy==1.4.12',
        'toml==0.10.2'
    ]
)
