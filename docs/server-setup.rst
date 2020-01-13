Server Setup
========================


Provisioning
------------------------

The server provisioning is managed using `Salt Stack <http://saltstack.com/>`_. The base
states are managed in a `common repo <https://github.com/caktus/margarita>`_ and additional
states specific to this project are contained within the ``conf`` directory at the root
of the repository.

For more information see the doc:`provisioning guide </provisioning>`.


Layout
------------------------

Below is the server layout created by this provisioning process::

    /code
    /var/www/rapidpro_community_portal/
        log/
        public/
            static/
            media/
        ssl/

``code`` contains the source code of the project.
``log`` stores the Nginx, uWSGI and other logs used by the project.
``public`` holds the static resources (css/js) for the project and the uploaded user media.
``public/static/`` and ``public/media/`` map to the ``STATIC_ROOT`` and ``MEDIA_ROOT`` settings.

