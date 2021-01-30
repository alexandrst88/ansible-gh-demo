import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_is_goss_installed(host):
    package_goss = host.file("/usr/local/bin/goss").exists
    assert package_goss

def test_run_goss_binary(host):
    hello_world_ran = host.run("/usr/local/bin/goss")
    assert 'goss - Quick and Easy server validation' in hello_world_ran.stdout
