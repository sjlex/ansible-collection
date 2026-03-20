# ansible-my-collection

> An Ansible Collection of roles.

## Supported Operating Systems

| Platform | Versions                   |
| -------- |----------------------------|
| Debian   | Bookworm - 12, Trixie - 13 |

## Install

- requirements.yml

  ```yml
  collections:
    - name: sjlex.collection
      source: https://github.com/sjlex/ansible-my-collection
      type: git
  ```

## Usage

```yml
roles:
  - role: sjlex.collection.fish
```

or

```yml
tasks:
  - name: "Install packages"
    ansible.builtin.include_role:
      name: "sjlex.collection.fish"
    vars:
      fisher_plugins:
        - sjlex/plain-prompt
        - jethrokuan/z
        - jethrokuan/fzf
```

## Development and Testing

### 1. Build Docker image and run dev-container:

```shell
./bin/task docker:build
./bin/task docker:run
```

### 2. Install dev dependencies

```shell
task dependencies:dev:install
```

### 3. Development

```shell
cd roles/fish
```

Run molecule test:

```shell
molecule test --all
```

or

```shell
molecule create &&
molecule converge &&
molecule idempotence &&
molecule verify &&
molecule destroy
```

#### 3.1 Login:

```shell
molecule login --host role-[name]_debian13_
molecule login --host role-nvim_debian12_
```

### 4. Testing

```shell
task test:all
```

or (specific role):

```shell
task test:role -- fish
```

### 5. Linting

```shell
task lint
task lint:fix
```

### 5. Clear cache and python env

```shell
task dependencies:clear
```

## License

[MIT](LICENSE)
