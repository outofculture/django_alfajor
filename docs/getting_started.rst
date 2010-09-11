Getting Started
===============

django_alfajor is a nose plugin to glue django and alfajor
together. Enabling tasty functional testing for Django.::

    pip install -e git+git://github.com/outofculture/django_alfajor.git#egg=django_alfajor

Unfortunately due to a bug/design choice in django-nose you must add a
``--`` in before you start adding the options you want passed through
to alfajor. To change this behavior so you can pass the options
straight to alfajor you can install Martin Chase's fork of
django-nose.::

    pip install -e git+git://github.com/outofculture/django-nose.git#egg=django-nose

You will also need `Selenium Server
<http://seleniumhq.org/download/>`_ which is in their Selenium RC
package. Put the jar file somewhere where you can find it.

