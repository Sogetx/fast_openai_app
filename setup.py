from setuptools import setup, find_packages

setup(
    name='fast_openai_app',
    version='0.1',
    packages=find_packages(where='app'),
    install_requires=[
        'fastapi==0.68.0',
        'uvicorn==0.27.0',
        'openai',
        'pydantic'
    ],
    entry_points={
        'console_scripts': [
            'start_app = app.main:app'
        ]
    }
)
