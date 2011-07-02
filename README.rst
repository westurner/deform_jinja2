deform_mako
===========

This is a Mako port of the Chameleon templates included in Deform.

To run the `deformdemo <http://deformdemo.repoze.org>`_ application using the
``deform_mako`` renderer:

- Create a virtualenv::

    $ virtualenv2.6 --no-site-packages env

  Heretofore, the ``env`` directory created above will be referred to as
  $VENV

- Clone the deformdemo GitHub repository::

    $ git clone git://github.com/Pylons/deformdemo.git

- cd to the deformdemo checkout and ``setup.py develop`` it into your
  virtualenv

    $ cd deformdemo
    $ $VENV/bin/python setup.py develop

- Use the deform_mako ``demo.ini`` file to run a demo app server via ``paster
  serve``:

    $ $VENV/bin/paster demo.ini

- The demo app will be running on port 8521.  See the ``README.rst`` in the
  deformdemo checkout for instructions about how to run the selenium tests.
