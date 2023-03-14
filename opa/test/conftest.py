import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        type=str,
        action="store",
        help="url of the main service",
    )


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")
