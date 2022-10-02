import pytest


@pytest.mark.parametrize("username,password",
                         [("selenium", "webdriver"),
                          ("python", "pytest"),
                          ("java", "jar")

                          ])
def test_parameter(username, password, welcome):
    print(f'\n{username},{password}')
