#!/usr/bin/env python

"""Tests for `crypto_currency_price` package."""

import pytest
from click.testing import CliRunner

from crypto_currency_price import __version__, cli, crypto_currency_price


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_version():
    """Test reading version and module name"""
    assert (
        crypto_currency_price.__name__
        == "crypto_currency_price.crypto_currency_price"
    )
    assert __version__
    assert isinstance(__version__, str)


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0, result
    assert "ccp converts prices" in result.output

    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0, result
    assert "Show this message and exit." in result.output
