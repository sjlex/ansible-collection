tmux
=========

An Ansible role to install and configure tmux.

Requirements
------------

None

Role Variables
--------------

`tmux_version`: Tmux version

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.tmux, tmux_version: '3.3a' }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>
