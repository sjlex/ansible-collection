docker
=========

An Ansible role to install and configure docker.

Requirements
------------

None

Role Variables
--------------

`docker_key_id`: The identifier of the key

`docker_key_url`: The URL to retrieve gpg key

`docker_key_path`: The keyring path (default: /etc/apt/keyrings/docker.asc)

`docker_repo_url`: A source string for the repository

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.docker, docker_repo_url: 'https://download.docker.com/linux/debian' }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
