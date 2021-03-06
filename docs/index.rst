.. _index:

Yet Another Time Series Model (YATSM)
=====================================

About
-----

Yet Another Timeseries Model (YATSM) is a Python package for utilizing a
collection of timeseries algorithms and methods designed to monitor the land
surface using remotely sensed imagery.

YATSM can be thought of as three components:

1. A library of functions and other objects useful for performing time series
   analysis, including various statistics and input/output helpers.
2. Time series analysis algorithm implementations
3. The command line interface (CLI) provides a set of programs that facilitate
   the running of time series algorithms on "time series stacks" and the
   analysis of the results.

User Guide
----------

To get started with YATSM, please follow this user guide:

.. toctree::
   :maxdepth: 1

   guide/install
   guide/example
   guide/dataset
   guide/exploration
   guide/model_specification
   guide/models/models
   guide/configuration
   guide/batch_interface
   guide/map_static
   guide/map_changes
   guide/classification
   guide/phenology
   guide/developer/custom_timeseries_algorithms.rst


Command Line Interface Utilities
--------------------------------

The Command Line Interface (CLI) for YATSM is built using
`click <http://click.pocoo.org/>`__ and is accessed using the ``yatsm``
command. Documentation about the CLI is available below:

.. toctree::
   :maxdepth: 2

   cli/scripts

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

References
----------

.. bibliography:: static/index_refs.bib
   :style: unsrt
   :cited:
