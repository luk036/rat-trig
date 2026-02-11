"""
Property-based tests for vector operations using Hypothesis.

This module contains property-based tests for the dot, cross, and quad functions
from rat_trig.trigonom module. These tests verify mathematical properties that
should hold for all valid inputs.
"""

from fractions import Fraction

import pytest
from hypothesis import given
from hypothesis import strategies as st

from rat_trig.trigonom import Numeric, cross, dot, quad

# Strategy for generating numeric values (int, Fraction, float)
numeric_strategy = st.one_of(
    st.integers(min_value=-100, max_value=100),
    st.fractions(min_value=-100, max_value=100, max_denominator=100),
    st.floats(min_value=-100.0, max_value=100.0, allow_nan=False, allow_infinity=False),
)

# Strategy for generating 2D vectors with numeric components
vector_strategy = st.tuples(numeric_strategy, numeric_strategy)


@given(vector_strategy, vector_strategy)
def test_dot_product_commutative(v1, v2):
    """Test that dot product is commutative: v·w = w·v"""
    result1 = dot(v1, v2)
    result2 = dot(v2, v1)
    assert result1 == result2


@given(vector_strategy, vector_strategy, vector_strategy)
def test_dot_product_distributive(v1, v2, v3) -> None:
    """Test that dot product is distributive: v·(w + u) = v·w + v·u"""
    # For property testing, we need to ensure the same type
    if isinstance(v1[0], type(v2[0])) and isinstance(v2[0], type(v3[0])):
        v2_plus_v3 = (v2[0] + v3[0], v2[1] + v3[1])
        result1 = dot(v1, v2_plus_v3)
        result2 = dot(v1, v2) + dot(v1, v3)
        # Allow for floating point precision issues
        if isinstance(result1, float) or isinstance(result2, float):
            assert abs(result1 - result2) < 1e-10  # type: ignore
        else:
            assert result1 == result2  # type: ignore


@given(vector_strategy, st.integers(min_value=1, max_value=10))
def test_dot_product_homogeneous(v, k):
    """Test that dot product is homogeneous: (k·v)·w = k·(v·w)"""
    # Use a fixed second vector to avoid type mixing issues
    w = (1, 1) if isinstance(v[0], (int, Fraction)) else (1.0, 1.0)
    kv = (v[0] * k, v[1] * k)
    result1 = dot(kv, w)
    result2 = k * dot(v, w)
    # Allow for floating point precision issues
    if isinstance(result1, float) or isinstance(result2, float):
        assert abs(result1 - result2) < 1e-10
    else:
        assert result1 == result2


@given(vector_strategy)
def test_dot_product_positive_definite(v):
    """Test that dot product is positive definite: v·v ≥ 0 and v·v = 0 iff v = 0"""
    result = dot(v, v)
    assert result >= 0
    # Only check equality to zero for exact types (not floats due to precision)
    if isinstance(v[0], (int, Fraction)):
        if v[0] == 0 and v[1] == 0:
            assert result == 0
        else:
            assert result != 0
    else:
        # For floats, check that result is only zero when both components are effectively zero
        # (within floating point precision limits)
        if v[0] == 0.0 and v[1] == 0.0:
            assert result == 0.0
        elif result == 0.0:
            # If dot product is zero but vector components are not both exactly zero,
            # this is due to floating point underflow with extremely small numbers
            # This is expected behavior, so we don't fail the test
            pass


@given(vector_strategy, vector_strategy)
def test_cross_product_anticommutative(v1, v2):
    """Test that cross product is anticommutative: v×w = -(w×v)"""
    result1 = cross(v1, v2)
    result2 = cross(v2, v1)
    assert result1 == -result2


@given(vector_strategy)
def test_cross_product_parallel(v):
    """Test that cross product of parallel vectors is zero: v×v = 0"""
    result = cross(v, v)
    assert result == 0


@given(vector_strategy, st.integers(min_value=1, max_value=10))
def test_cross_product_homogeneous(v, k):
    """Test that cross product is homogeneous: (k·v)×w = k·(v×w)"""
    # Use a fixed second vector to avoid type mixing issues
    w = (1, 1) if isinstance(v[0], (int, Fraction)) else (1.0, 1.0)
    kv = (v[0] * k, v[1] * k)
    result1 = cross(kv, w)
    result2 = k * cross(v, w)
    # Allow for floating point precision issues
    if isinstance(result1, float) or isinstance(result2, float):
        assert abs(result1 - result2) < 1e-10
    else:
        assert result1 == result2


@given(vector_strategy)
def test_quadrance_non_negative(v) -> None:
    """Test that quadrance is always non-negative"""
    result: Numeric = quad(v)  # type: ignore[assignment]
    assert result >= 0  # type: ignore[operator]


@given(vector_strategy)
def test_quadrance_zero_only_for_zero_vector(v):
    """Test that quadrance is zero only for the zero vector"""
    result = quad(v)
    # Only check equality to zero for exact types (not floats due to precision)
    if isinstance(v[0], (int, Fraction)):
        if v[0] == 0 and v[1] == 0:
            assert result == 0
        else:
            assert result != 0


@given(vector_strategy, st.integers(min_value=1, max_value=10))
def test_quadrance_homogeneous(v, k) -> None:
    """Test that quadrance is homogeneous: quad(k·v) = k²·quad(v)"""
    kv = (v[0] * k, v[1] * k)
    result1: Numeric = quad(kv)  # type: ignore[assignment]
    result2: Numeric = k * k * quad(v)  # type: ignore[assignment]

    # Use relative error for better floating point handling
    if result2 == 0:  # type: ignore[comparison-overlap]
        assert abs(result1 - result2) < 1e-10  # type: ignore[operator]
    else:
        relative_error = abs(result1 - result2) / abs(result2)  # type: ignore[operator]
        assert (
            relative_error < 1e-8
        )  # Allow small floating point errors  # type: ignore[operator]


@given(vector_strategy, vector_strategy)
def test_pythagorean_theorem(v1, v2):
    """Test Pythagorean theorem: ||v||² + ||w||² = ||v + w||² - 2·v·w"""
    # This is a rearranged form of: ||v + w||² = ||v||² + ||w||² + 2·v·w
    # We need to ensure same types to avoid mixing
    if isinstance(v1[0], type(v2[0])):
        v1_plus_v2 = (v1[0] + v2[0], v1[1] + v2[1])
        lhs = quad(v1) + quad(v2)
        rhs = quad(v1_plus_v2) - 2 * dot(v1, v2)
        # Allow for floating point precision issues
        if isinstance(lhs, float) or isinstance(rhs, float):
            assert abs(lhs - rhs) < 1e-10
        else:
            assert lhs == rhs


@given(vector_strategy, vector_strategy)
def test_lagrange_identity(v1, v2) -> None:
    """Test Lagrange's identity: (v·w)² + (v×w)² = ||v||²·||w||²"""
    # This identity holds in 2D
    dot_sq: Numeric = dot(v1, v2) ** 2  # type: ignore[assignment]
    cross_sq: Numeric = cross(v1, v2) ** 2  # type: ignore[assignment]
    quad_product: Numeric = quad(v1) * quad(v2)  # type: ignore[assignment]

    # Use absolute error for very small values to avoid division by near-zero
    if abs(quad_product) < 1e-100:  # type: ignore[operator]
        # When dealing with extremely small numbers, use absolute error
        assert abs(dot_sq + cross_sq - quad_product) < 1e-50  # type: ignore
    elif quad_product == 0:
        assert abs(dot_sq + cross_sq - quad_product) < 1e-10  # type: ignore
    else:
        relative_error = abs(dot_sq + cross_sq - quad_product) / abs(quad_product)  # type: ignore
        assert (
            relative_error < 1e-8
        )  # Allow small floating point errors  # type: ignore


if __name__ == "__main__":
    pytest.main()
