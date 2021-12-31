import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PACKAGE = 'code'
PACKAGE_BINARY = '/usr/bin/code'
REPO_DEBIAN_FILE = '/etc/apt/sources.list.d/vscode.list'
REPO_EL_FILE = '/etc/yum.repos.d/vscode.repo'


def test_vscode_package_installed(host):
    """
    Tests if vscode package is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_vscode_binary_exists(host):
    """
    Tests if vscode binary exists.
    """
    host.file(PACKAGE_BINARY).exists


def test_vscode_binary_isfile(host):
    """
    Tests if vscode binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_vscode_binary_which(host):
    """
    Tests the output to confirm vscode's binary location.
    """
    assert host.check_output('which code') == PACKAGE_BINARY


def test_vscode_repofile_exists(host):
    """
    Tests if vscode repo file exists.
    """
    assert host.file(REPO_DEBIAN_FILE).exists or \
        host.file(REPO_EL_FILE).exists


def test_vscode_repofile_isfile(host):
    """
    Tests if vscode repo file is file type.
    """
    assert host.file(REPO_DEBIAN_FILE).is_file or \
        host.file(REPO_EL_FILE).is_file
