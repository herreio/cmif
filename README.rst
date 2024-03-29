.. role:: shell(code)
   :language: shell

cmif
====

Synopsis
--------

``cmif`` is a Python package for creating and retrieving data in `CMI format <https://github.com/TEI-Correspondence-SIG/CMIF>`_. It has been developed as part of the `Dikon project <https://dikon.izea.uni-halle.de/>`_ (2019–2020) at the `Interdisciplinary Centre for European Enlightenment Studies <https://www.izea.uni-halle.de/>`_.

Installation
------------

You can install this package via `PyPI <https://pypi.org/project/cmif/>`_:

.. code-block:: shell

    pip install cmif

... or by cloning the repository:

.. code-block:: shell

    git clone https://github.com/herreio/cmif.git --recurse-submodules
    cd cmif
    # create and activate virutalenv
    utils/setup
    source env/bin/activate

Documentation
-------------

The documentation can be found on `Read the Docs <https://cmif.readthedocs.io/>`_.

To build the documentation from the files found at docs:

.. code-block:: shell

    cd docs
    make html


Test
----

In case you cloned the repository, you can run a unittest:

.. code-block:: shell

    python -m unittest test.creation


See Also
--------

The Python command line interface `csv2cmi <https://github.com/saw-leipzig/csv2cmi>`_, written by `K. Rettinghaus <https://github.com/rettinghaus>`_, allows to create files in CMI format from CSV input.
