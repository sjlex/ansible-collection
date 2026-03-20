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

`docker_context_default`: Docker default context

`docker_context`: Docker context

    docker_context:
      - name: "remote"
        endpoint: "tcp://localhost:2375"

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - role: sjlex.docker
          vars:
            docker_context_default: "my-context"
            docker_context:
              - name: "remote"
                endpoint: "tcp://localhost:2375"
              - name: "my-context"
                endpoint: "unix:///var/run/docker.sock"

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
