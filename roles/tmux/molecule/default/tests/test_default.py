import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        tmux -V
        """,
    )

    assert cmd.rc == 0
    assert cmd.stdout.startswith("tmux")


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "trixie", "tmux", "3.6a"),
        ("debian", "bookworm", "tmux", "3.6a"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename

    if host_os == os_name and os_codename == host_os_codename:
        cmd = host.run_test("tmux -V")

        assert cmd.rc == 0
        assert cmd.stdout.startswith(f"tmux {package_version}\n")
