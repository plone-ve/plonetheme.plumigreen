from setuptools import setup
from setuptools import find_packages


version = '0.1'
name='plonetheme.plumigreen'


setup(
    name=name,
    version=version,
    description='Plumi Green, is an installable Diazo theme for Plone 4',
    long_description=open("README.rst").read() + "\n" +
                     open(os.path.join("docs", "CHANGES.rst")).read(),
    # Get more strings from
    # https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='web zope plone diazo theme plonetheme plumigreen cms',
    author='Rok Garbas',
    author_email='rok@garbas.si',
    maintainer='Leonardo Caballero',
    maintainer_email='leonardocaballero@gmail.com',
    url='https://github.com/garbas/'+name,
    license='BSD',
    packages=find_packages(),
    namespace_packages=['plonetheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.theming',
        'plone.app.themingplugins',
        ],
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
        """,
    )
