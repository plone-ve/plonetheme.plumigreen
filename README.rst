=====================
plonetheme.plumigreen
=====================


This plone theme, is an installable `Diazo`_ theme for `Plone`_ 4 developed 
by `Rok Garbas`_.

.. contents::

Introduction
============

The ``plonetheme.plumigreen`` package uses the *theming & packaging* features
available in `plone.app.theming`_ for intent to be similar to `plumi.skin`_ package in 
*Plone 4*. Its ment to be its replacement.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest versión (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/garbas/plonetheme.plumigreen/raw/master/plonetheme/plumigreen/static/preview.png


Features
========

- It's an installable Plone Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- It's have support for clean uninstallation.
- Also it's a simple Diazo package (Zip file).


Installation
============


Zip file
--------

Using .zip as an end user
^^^^^^^^^^^^^^^^^^^^^^^^^

If you are an end user, you might enjoy installation via zip file import.

1. Download a `zip file <https://github.com/garbas/plonetheme.plumigreen/raw/master/plumigreen.zip>`_.
2. Import the theme from the Diazo theme control panel.


Using .zip as a developer
^^^^^^^^^^^^^^^^^^^^^^^^^

If you are a developer, you might enjoy installation via zip file import.

::

    % git clone git://github.com/garbas/plonetheme.plumigreen.git
    % cd plonetheme.plumigreen
    % git archive --format=zip --prefix=plumigreen/ HEAD:plonetheme/plumigreen/static/ > plumigreen.zip

Import created zip file via ``@@theming-controlpanel`` -> ``Import theme`` tab.


Enabling the theme
^^^^^^^^^^^^^^^^^^

Select and enable the theme from the Diazo control panel. That's it!


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``plonetheme.plumigreen`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.plumigreen


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.plumigreen',
    ],


Contribute
==========

:Source Code: https://github.com/garbas/plonetheme.plumigreen
:Issues Tracker: https://github.com/garbas/plonetheme.plumigreen/issues
:Licence: http://www.opensource.org/licenses/bsd-license.php
:Download: https://github.com/garbas/plonetheme.plumigreen/archive/master.zip


License
=======

The project is licensed under the BSD.

Credits
-------

- `Rok Garbas`_, initial implementation
- `Plumi developers`_, idea that this theme is based uppon


Contributors
------------

- Leonardo J. Caballero G. (leonardocaballero at gmail dot com).

.. _`Plone`: http://plone.org
.. _`Diazo`: http://diazo.org
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`plumi.skin`: https://github.com/plumi/plumi.skin/
.. _`Rok Garbas`: https://www.garbas.si/
.. _`Plumi developers`: https://plumi.org/blog/
