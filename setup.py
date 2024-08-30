from setuptools import setup

setup(
    name='rvm',
    version="0.0.1",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sword4869/RobustVideoMatting",
    install_requires=[
        'torch',
        'torchvision',
        'tqdm',
        'av>=11.0.0',
        'pims>=0.6.1'
    ],
    entry_points={
        'console_scripts': [
            'rvm = rvm.inference:main',
        ]
    }
)
