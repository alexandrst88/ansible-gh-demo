import os
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_is_os_packages_installed(host):
    packages = ["python3-pip", "jq", "unzip"]
    for p in packages:
        p_os = host.package(p)
        assert p_os.is_installed


