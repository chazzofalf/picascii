from setuptools import setup

setup(
    name='picascii',
    version='0.1.0',    
    description='Turn pictures into colored dot text files!',
    url='https://github.com/chazzofalf/picascii',
    author='Charles Timothy Montgomery',
    author_email='charles.montgomery@charter.net',
    license='MIT',
    packages=['picascii'],
    install_requires=['Pillow'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: MIT',  
        'Operating System :: Cross-Platform',                
        'Programming Language :: Python :: 3.12',
    ],
)