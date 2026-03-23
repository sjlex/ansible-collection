mise
=========

An Ansible role to install and configure mise.

Requirements
------------

None

Role Variables
--------------

`mise_package_version`: Package version

`mise_package_url`: Package URL

`mise_package_checksum`: Package Checksum

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.mise, mise_package_version: '2026.3.13' }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
