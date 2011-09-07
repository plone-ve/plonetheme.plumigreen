=====================
plonetheme.plumigreen
=====================

Installable theme for `Plone`_ (using `plone.app.theming`_).

:Source: https://github.com/garbas/plonetheme.plumigreen
:Issues: https://github.com/garbas/plonetheme.plumigreen/issues
:Licence: http://www.opensource.org/licenses/bsd-license.php
:Download: http://github.com/downloads/garbas/plonetheme.plumigreen/plumigreen-latest.zip

This theme is intent to be similar to `plumi.skin`_. Its ment to be its
replacement.


.. contents::


Installation
============

Using buildout
--------------

Add ``plonetheme.plumigreen`` to eggs section of your zope client.::

    [instance]
    ...
    eggs =
        ...
        plonetheme.plumigreen


Using .zip
----------

::

    % git clone git://github.com/garbas/plonetheme.plumigreen.git
    % cd plonetheme.plumigreen
    % git archive --format=zip --prefix=plumigreen/ HEAD:plonetheme/plumigreen/static/ > plumigreen.zip

Import created zip file via ``@@theming-controlpanel`` -> ``Import theme`` tab.



Activating theme
----------------

Browse to ``http://yoursite/Plone/@@theming-controlpanel`` click on ``Enable
theme`` check box and select ``plonetheme.plumigreen`` from
dropdown.


Credits
=======

    * `Rok Garbas`_, initial implementation
    * `Plumi developers`_, idea that this theme is based uppon


Changelog
=========

0.1 - 2011-09-07
----------------

    * initial implementation of theme with Diazo_ rules.
      [garbas]


.. _`Rok Garbas`: http://www.garbas.si
.. _`Plumi developers`: http://blog.plumi.org

.. _`Plone`: http://plone.org
.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Diazo': http://diazo.org
