eza
=========

An Ansible role to install and configure eza (a modern replacement for ls).

Requirements
------------

None

Role Variables
--------------

`eza_key_id`: The identifier of the key

`eza_key_url`: The URL to retrieve gpg key

`eza_key_path`: The keyring path (default: /etc/apt/keyrings/gierens.gpg)

`eza_repo_url`: A source string for the repository

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.eza }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
