[![build-test](https://github.com/darkwizard242/ansible-role-vscode/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-vscode/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-vscode/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-vscode/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/46026?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/46026?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/46026?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-vscode&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-vscode) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-vscode&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-vscode) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-vscode&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-vscode) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-vscode&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-vscode) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-vscode?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-vscode?color=orange&style=flat-square)

# Ansible Role: vscode

Role to install (_by default_) [Visual Studio Code](https://code.visualstudio.com/docs) on **Debian/Ubuntu** family and **EL** family systems. Visual Studio Code is a lightweight but powerful source code editor

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
vscode_app_name: code
vscode_desired_state: present
vscode_repo_desired_state: present

# For Debian/Ubuntu Family
vscode_debian_pre_reqs:
  - apt-transport-https
  - curl
  - ca-certificates
  - lsb-release
  - gnupg
vscode_debian_pre_reqs_desired_state: present
vscode_debian_gpg_key: https://packages.microsoft.com/keys/microsoft.asc
vscode_debian_repo: "deb [arch={{ ansible_architecture }}] https://packages.microsoft.com/repos/{{ vscode_app_name }} stable main"
vscode_debian_repo_when_x86_64: "deb [arch=amd64] https://packages.microsoft.com/repos/{{ vscode_app_name }} stable main"
vscode_debian_repo_filename: vscode

# For EL Family
vscode_el_gpg_key: https://packages.microsoft.com/keys/microsoft.asc
vscode_el_repo_name: code
vscode_el_repo_description: Visual Studio Code
vscode_el_repo: https://packages.microsoft.com/yumrepos/vscode
vscode_el_repo_filename: vscode
vscode_el_repo_gpgcheck: yes
vscode_el_repo_enabled: yes
```

### Variables table:

Variable                             | Description
------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
vscode_app_name                      | Name of Visual Studio Code package i.e. `code`
vscode_desired_state                 | State of the vscode_app_name package (i.e. `code` package itself.). Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
vscode_repo_desired_state            | `present` indicates creating the repository file if it doesn't exist on Debian or EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **code** pacakge).
vscode_debian_pre_reqs               | Package required by Visual Studio Code on Debain based systems.
vscode_debian_pre_reqs_desired_state | State of the vscode_pre_reqs_debian_desired_state packages. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
vscode_debian_gpg_key                | Visual Studio Code GPG required on Debian based systems.
vscode_debian_repo                   | Repository URL for Debian based systems. Utilized facts such as `ansible_architecture`.
vscode_debian_repo_when_x86_64       | This variable is used only against systems that are x86_64 type as the architecture is overridden to `arch=amd64` as per Visual Studio Code's Installation steps.
vscode_debian_repo_filename          | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems. Defaults to `vscode`.
vscode_el_gpg_key                    | Visual Studio Code GPG required on EL based systems.
vscode_el_repo_name                  | Repository name for Visual Studio Code on EL based systems.
vscode_el_repo_description           | Description to be added in EL based repository file for Visual Studio Code.
vscode_el_repo                       | Repository `baseurl` for Visual Studio Code on EL based systems.
vscode_el_repo_filename              | Name of the repository file that will be stored at `/etc/yum/sources.list.d/` on EL based systems. Defaults to `vscode`.
vscode_el_repo_gpgcheck              | Boolean for whether to perform gpg check against Visual Studio Code on EL based systems.
vscode_el_repo_enabled               | Boolean for whether to set Visual Studio Code repo as 'enabled' on EL based systems.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **vscode**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.vscode
```

For customizing behavior of role (i.e. installation of latest **vscode**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.vscode
  vars:
    vscode_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **vscode**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.vscode
  vars:
    vscode_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-vscode/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev).
