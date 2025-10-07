"""
Example test file demonstrating pytest basics.

Run tests with:
    make test
    make test-cov
"""

import pytest


def add(a: int, b: int) -> int:
    """Simple function to demonstrate testing."""
    return a + b


def divide(a: float, b: float) -> float:
    """Divide two numbers, raising error on division by zero."""
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b


class TestBasicMath:
    """Example test class demonstrating various test patterns."""

    def test_add_positive_numbers(self) -> None:
        """Test adding two positive numbers."""
        result = add(2, 3)
        assert result == 5

    def test_add_negative_numbers(self) -> None:
        """Test adding negative numbers."""
        result = add(-2, -3)
        assert result == -5

    def test_add_zero(self) -> None:
        """Test adding zero."""
        result = add(5, 0)
        assert result == 5

    def test_divide_normal(self) -> None:
        """Test normal division."""
        result = divide(10, 2)
        assert result == 5.0

    def test_divide_by_zero_raises_error(self) -> None:
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match='Cannot divide by zero'):
            divide(10, 0)

    @pytest.mark.parametrize(
        'a,b,expected',
        [
            (10, 2, 5),
            (9, 3, 3),
            (15, 5, 3),
            (100, 10, 10),
        ],
    )
    def test_divide_parametrized(self, a: float, b: float, expected: float) -> None:
        """Test division with multiple parameter sets."""
        result = divide(a, b)
        assert result == expected


# Example fixture
@pytest.fixture
def sample_data() -> dict[str, int]:
    """Fixture providing sample data for tests."""
    return {'value': 42, 'count': 10}


def test_with_fixture(sample_data: dict[str, int]) -> None:
    """Example test using a fixture."""
    assert sample_data['value'] == 42
    assert sample_data['count'] == 10
