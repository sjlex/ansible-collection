import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """
        mise --help
        """,
    )

    assert cmd.rc == 0


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "trixie", "mise", "2026.3.13"),
        ("debian", "bookworm", "mise", "2026.3.13"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename

    if host_os == os_name and os_codename == host_os_codename:
        cmd = host.run_test("mise --version")

        assert cmd.rc == 0
        assert package_version in cmd.stdout


def test_man_page_is_installed(host):
    man_page = host.file("/usr/local/share/man/man1/mise.1")

    assert man_page.exists
    assert man_page.is_file
    assert man_page.size > 0
