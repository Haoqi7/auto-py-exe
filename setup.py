from io import open
from setuptools import setup
from auto_py_to_exe import __version__ as version

setup(
    name='auto-py-exe',
    version=version,
    url='https://github.com/Haoqi7/auto-py-exe',
    license='MIT',
    author='Brent Vollebregt',
    author_email='brent@nitratine.net',
    description='Converts .py to .exe using a simple graphical interface.',
    long_description=''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type='text/markdown',
    keywords=['gui', 'executable'],
    packages=['auto_py_exe'],
    include_package_data=True,
    install_requires=['Eel==0.14.0', 'pyinstaller>=4.6'],
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'autopyexe=auto_py_exe.__main__:run',
            'auto-py-exe=auto_py_exe.__main__:run'
        ],
    },
)
