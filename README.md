<h3 id="ansible-collection" align="center">
  <br>
    <img src="assets/logo.png" alt="Ansible Collection Logo" width="160">
  <br>
  Ansible Collection
  <br>
</h3>

##

<div align="center">
  <p>A personal collection of Ansible roles.</p>
</div>

<p align="center">
  <a href="https://github.com/sjlex/ansible-collection/releases/latest"><img alt="Version" src="https://img.shields.io/github/v/release/sjlex/ansible-collection?labelColor=black&color=black"></a>&nbsp;
  <a href="https://github.com/sjlex/ansible-collection/blob/main/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/sjlex/ansible-collection?labelColor=black&color=black"></a>&nbsp;
</p>

## Table of contents

- [Ansible Collection](#ansible-collection)
  - [Table of contents](#table-of-contents)
  - [Getting started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Development](#development)
    - [Dev-Container](#dev-container)
      - [Build](#build-the-docker-image)
      - [Run](#run-the-docker-container)
    - [Install dependencies](#install-dependencies)
    - [Testing](#testing)
      - [Run all tests](#run-tests-for-all-roles)
      - [Run tests for a specific role](#run-tests-for-a-specific-role)
      - [Run tests manually](#run-tests-manually)
      - [Login](#login)
    - [Linting](#linting)
    - [Clear All](#clear-all)
  - [License](#license)
  - [Third-Party Assets](#third-party-assets)

## Getting started

### Prerequisites

Supported Operating Systems:

| Platform | Versions                   |
| -------- |----------------------------|
| Debian   | Bookworm - 12, Trixie - 13 |

### Installation

- requirements.yml

  ```yml
  collections:
    - name: sjlex.collection
      source: https://github.com/sjlex/ansible-collection
      type: git
    ```

## Usage

- Playbooks:

  ```yml
  roles:
    - role: sjlex.collection.fish
  ```

- Roles:

  ```yml
  tasks:
    - name: "Install package"
      ansible.builtin.include_role:
        name: "sjlex.collection.fish"
      vars:
        fisher_plugins:
          - sjlex/plain-prompt
          - jethrokuan/z
          - jethrokuan/fzf
  ```

## Development

### Dev-Container

#### Build the Docker image:

```shell
./bin/task docker:build
```

#### Run the Docker container:

```shell
./bin/task docker:run
```

### Install dependencies:

```shell
task dependencies:dev:install
```

### Testing

#### Run tests for all roles:

```shell
task test:all
```

#### Run tests for a specific role:

```shell
task test:role -- fish
```

or:

```shell
cd roles/fish
```

```shell
molecule test --all
```

#### Run tests manually:

```shell
cd roles/fish
```

```shell
molecule create &&
molecule converge &&
molecule verify &&
molecule idempotence &&
molecule destroy
```

#### Login

```shell
molecule list
```

```shell
molecule login --host role-fish_debian13_
```

### Linting

```shell
task lint
```

```shell
task lint:fix
```

### Clear All

- Cache and Python environment cleanup:

```shell
task clear
```

## License

[MIT License](LICENSE)

## Third-Party Assets

This project may include or reference third-party assets under their own licenses. Any such assets are used in accordance with their licensing terms.

- [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
  - Source: [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono)
  - License: [SIL Open Font License 1.1](https://fonts.google.com/specimen/JetBrains+Mono/license)
