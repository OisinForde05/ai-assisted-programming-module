from validate_b import validate_email


def test_standard_email():
    assert validate_email("user@example.com") is True


def test_missing_dot_after_at():
    assert validate_email("user@example") is False


def test_too_long_email():
    assert validate_email("a" * 300 + "@example.com") is False
