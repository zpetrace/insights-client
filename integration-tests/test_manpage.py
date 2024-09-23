"""
:casecomponent: insights-client
:requirement: RHSS-291297
:subsystemteam: sst_csi_client_tools
:caseautomation: Automated
:upstream: Yes
"""

import gzip
import pytest


@pytest.mark.parametrize(
    "option",
    [
        "--checkin",
        "--compliance",
        "--conf",
        "--content-type",
        "--diagnosis",
        "--disable-schedule",
        "--display-name",
        "--enable-schedule",
        "--group",
        "--keep-archive",
        "--list-specs",
        "--logging-file",
        "--net-debug",
        "--no-upload",
        "--offline",
        "--output-dir",
        "--output-file",
        "--payload",
        "--quiet",
        "--register",
        "--retry",
        "--show-results",
        "--silent",
        "--status",
        "--test-connection",
        "--unregister",
        "--validate",
        "--verbose",
        "--version",
    ],
)
def test_manpage(option):
    """
    :id: bd8dbda3-930e-4081-b318-1e88b25e26ef
    :title: Test manual page entries for insights-client
    :description:
        This test verifies that the insights-client manual page includes
        all the specified options.
    :reference:
    :tier: Tier 1
    :steps:
        1. Open the manual page
        2. Verify that the specified options are present
    :expectedresults:
        1. Manual page is opened successfully
        2. All od the options are found in the manual page
    """
    file = "/usr/share/man/man8/insights-client.8.gz"
    opened_file = gzip.open(file, "rt")
    content = opened_file.read()
    assert option in content, f"Option {option} is not present"
