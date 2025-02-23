.. _ref_linux_docker:

Linux Docker container
======================

.. contents::
   :backlinks: none

.. _ref_running_linux_containers:

Docker for Linux containers
---------------------------

To run the Linux Docker container for the Geometry service, ensure that you follow
these steps when installing Docker:

.. tab-set::

    .. tab-item:: Linux machines

       If you are on a Linux machine, install `Docker for your distribution <https://docs.docker.com/engine/install/#server>`_

    .. tab-item:: Windows/MacOS machines

       #. Install `Docker Desktop for Windows <https://docs.docker.com/desktop/install/windows-install/>`_ or
          `Docker Desktop for MacOS <https://docs.docker.com/desktop/install/mac-install/>`_.

       #. **(On Windows)** When prompted for **Use WSL2 instead of Hyper-V (recommended)**, **clear** this checkbox.
          Hyper-V must be enabled to run Windows Docker containers, which you might be interested in doing in the future.

       #. Once the installation finishes, restart your machine and start Docker Desktop.

Now that your Docker engine supports running Linux Docker containers, you can build or install
the PyAnsys Geometry image.

Build or install the Geometry service image
-------------------------------------------

There are two options for installing the PyAnsys Geometry image:

* Downloading it from the :ref:`GitHub Container Registry <ref_linux_docker_ghcr>`.
* :ref:`Build the Geometry service Linux container <ref_linux_docker_fromscratch>`.

.. _ref_linux_docker_ghcr:

GitHub Container Registry
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This option is only available for users with write access to the repository or
   who are members of the Ansys organization.

Once Docker is installed on your machine, follow these steps to download the Linux Docker
container for the Geometry service and install this image.

#. Using your GitHub credentials, download the Docker image from the `PyAnsys Geometry repository <https://github.com/ansys/pyansys-geometry>`_
   on GitHub.

#. Use a GitHub personal access token with permission for reading packages to authorize Docker
   to access this repository. For more information, see `Managing your personal access tokens
   <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`_
   in the GitHub documentation.

#. Save the token to a file with this command:

   .. code-block:: bash

       echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX > GH_TOKEN.txt

#. Authorize Docker to access the repository and then run the commands for your OS. To see these commands, click the tab for your OS.

   .. tab-set::

       .. tab-item:: Linux/Mac

           .. code-block:: bash

               GH_USERNAME=<my-github-username>
               cat GH_TOKEN.txt | docker login ghcr.io -u $GH_USERNAME --password-stdin

       .. tab-item:: Powershell

           .. code-block:: pwsh

               $env:GH_USERNAME=<my-github-username>
               cat GH_TOKEN.txt | docker login ghcr.io -u $env:GH_USERNAME --password-stdin

       .. tab-item:: Windows CMD

           .. code-block:: bash

               SET GH_USERNAME=<my-github-username>
               type GH_TOKEN.txt | docker login ghcr.io -u %GH_USERNAME% --password-stdin


#. Pull the Geometry service locally using Docker with a command like this:

   .. code:: bash

      docker pull ghcr.io/ansys/geometry:linux-latest

.. _ref_linux_docker_fromscratch:

Build the Geometry service Linux container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Geometry service Docker containers can be easily built by following
these steps.

Inside the repository's ``docker`` folder, there are two ``Dockerfile`` files:

* ``Dockerfile.linux``: File for building the Linux-based Docker image.
* ``Dockerfile.windows``: File for building the Windows-based Docker image.

Depending on the characteristics of the Docker engine installed on your
machine, either one or the other has to be built.

This guide focuses on building the ``Dockerfile.linux`` image.

Prerequisites
~~~~~~~~~~~~~

* Ensure that Docker is installed on your machine.
  If you do not have Docker available, see
  :ref:`Docker for Linux containers <ref_running_linux_containers>`.

* Download the `latest Linux Dockerfile <https://github.com/ansys/pyansys-geometry/blob/main/docker/Dockerfile.linux>`_.

* Download the `latest release artifacts for the Linux
  Docker container (ZIP file) <https://github.com/ansys/pyansys-geometry/releases/latest/download/linux-binaries.zip>`_.

* Move this ZIP file to the location of the Linux Dockerfile previously downloaded.

Build the Docker image
~~~~~~~~~~~~~~~~~~~~~~

To build your image, follow these steps:

#. Navigate to the folder where the ZIP file and the Dockerfile are located.
#. Run this Docker command:

   .. code:: bash

      docker build -t ghcr.io/ansys/geometry:linux-latest -f Dockerfile.linux .

#. Check that the image has been created successfully. You should see an output similar
   to this one:

   .. code:: bash

      docker images

      >>> REPOSITORY                                               TAG                                IMAGE ID       CREATED          SIZE
      >>> ghcr.io/ansys/geometry                                   linux-******                       ............   X seconds ago    Y.ZZGB
      >>> ......                                                   ......                             ............   ..............   ......


.. START - Include the common text for launching the service from a Docker container

.. jinja:: linux_containers
   :file: getting_started/docker/common_docker.jinja
   :header_update_levels:

.. END - Include the common text for launching the service from a Docker container

.. button-ref:: index
    :ref-type: doc
    :color: primary
    :shadow:
    :expand:

    Go to Docker containers

.. button-ref:: ../index
    :ref-type: doc
    :color: primary
    :shadow:
    :expand:

    Go to Getting started
