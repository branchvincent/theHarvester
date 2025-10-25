import pytest


# def pytest_addoption(parser: pytest.Parser) -> None:
#     parser.addoption('--integration', action='store_true', default=False, help='Run integration tests')


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line('markers', 'integration: mark test as an integration test')
    # config.option.markexpr = 'integration' if config.option.integration else 'not integration'
    # if 'integration' not in config.option.markexpr:
    #     config.option.markexpr += f"{'and ' if config.option.markexpr else ''}not integration"
