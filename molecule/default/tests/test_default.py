import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ntp_is_installed(host):
    p = host.package('ntp')

    assert p.is_installed


def test_ntp_is_running_and_enabled(host):
    s = host.service('ntpd')

    assert s.is_running
    assert s.is_enabled
