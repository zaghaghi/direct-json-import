from genericpath import exists
from os.path import join
from os import makedirs
from distutils.core import setup
from distutils.command.install import install


class InstallEx(install):
    def initialize_options(self):
        install.initialize_options(self)
        self.build_scripts = None

    def finalize_options(self):
        install.finalize_options(self)

    def run(self):
        ret = install.run(self)
        output_filename = join(self.install_libbase, 'direct_json_import.pth')
        input_filename = 'src/direct_json_import.pth'
        print('install path file from', input_filename, ' to', output_filename)
        with open(output_filename, 'w') as output, open(input_filename, 'r') as input:
            output.write(input.read())
        return ret

setup(
    name='direct-json-import',
    version='0.0.1',
    description='A pakacge to helps you import json files directly',
    keywords='python json direct import',
    author='Hamed Zaghaghi',
    author_email='hamed.zaghaghi@gmail.com',
    url='https://github.com/zaghaghi/direct-json-import',
    license='Apache Software License (Apache 2.0 license)',
    setup_requires=['wheel'],
    cmdclass={
        'install': InstallEx,
    },
    packages=[
        'direct_json_import',
    ],
    package_dir={
        '': 'src',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
