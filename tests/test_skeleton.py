import logging

import pytest

from rat_trig.skeleton import fib, main, parse_args

__author__ = "Wai-Shing Luk"
__copyright__ = "Wai-Shing Luk"
__license__ = "MIT"


def test_fib():
    """API Tests"""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    assert fib(20) == 6765
    with pytest.raises(AssertionError):
        fib(-10)


def test_main(capsys):
    """CLI Tests"""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(["7"])
    captured = capsys.readouterr()
    assert "The 7-th Fibonacci number is 13" in captured.out


def test_parse_args():
    """Test parsing of command line arguments"""
    with pytest.raises(SystemExit):
        parse_args(["--version"])
    args = parse_args(["-v", "1"])
    assert args.loglevel == logging.INFO
    args = parse_args(["-vv", "1"])
    assert args.loglevel == logging.DEBUG
    args = parse_args(["1"])
    assert args.n == 1
