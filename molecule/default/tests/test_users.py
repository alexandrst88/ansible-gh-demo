import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_is_users_exists(host):
    assert host.user("security_audit").exists is True
    assert host.group("security_audit").exists is True
