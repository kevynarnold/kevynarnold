from setuptools import setup, find_packages

setup(
    name='ipfs_processor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow', 'pyyaml', 'piexif'
    ],
    entry_points={
        'console_scripts': [
            'ipfs_processor=ipfs_processor.main:main'
        ]
    },
    author='Your Name',
    description='A package to process images and save metadata',
    keywords='IPFS, image processing, metadata',
)
