"""
Property-based tests for trigonometry functions using Hypothesis.

This module contains property-based tests for the archimedes, spread, spread_law,
and triple_quad_formula functions from rat_trig.trigonom module. These tests
verify mathematical properties that should hold for all valid inputs.
"""

from fractions import Fraction
from hypothesis import given, strategies as st, assume
import pytest

from rat_trig.trigonom import (
    archimedes, spread, spread_law, triple_quad_formula,
    dot, cross, quad
)


# Strategy for generating numeric values (int, Fraction, float)
numeric_strategy = st.one_of(
    st.integers(min_value=1, max_value=100),  # Use positive values for quadrances
    st.fractions(min_value=1, max_value=100, max_denominator=100),
    st.floats(min_value=0.1, max_value=100.0, allow_nan=False, allow_infinity=False)
)

# Strategy for generating 2D vectors with numeric components
vector_strategy = st.tuples(numeric_strategy, numeric_strategy)

# Strategy for spread values (between 0 and 1)
spread_strategy = st.one_of(
    st.fractions(min_value=0, max_value=1, max_denominator=100),
    st.floats(min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False)
)


@given(numeric_strategy, numeric_strategy, numeric_strategy)
def test_archimedes_symmetry(q1, q2, q3):
    """Test that Archimedes function is symmetric in its first two arguments"""
    result1 = archimedes(q1, q2, q3)
    result2 = archimedes(q2, q1, q3)
    assert result1 == result2


@given(numeric_strategy, numeric_strategy, numeric_strategy)
def test_archimedes_non_negative(q1, q2, q3):
    """Test that Archimedes function returns non-negative values for valid triangles"""
    # For a valid triangle, the sum of any two sides must be greater than the third
    # In terms of quadrances, this means: sqrt(q1) + sqrt(q2) > sqrt(q3)
    # We'll test this property for cases where it holds
    assume(q1 > 0 and q2 > 0 and q3 > 0)
    assume(abs(q1 + q2 - q3) < 2 * (q1 * q2) ** 0.5)  # Triangle inequality for quadrances
    
    result = archimedes(q1, q2, q3)
    assert result >= 0


@given(vector_strategy, vector_strategy)
def test_spread_range(v1, v2):
    """Test that spread is always between 0 and 1"""
    # Avoid zero vectors which would cause division by zero
    assume(v1 != (0, 0) and v2 != (0, 0))
    
    result = spread(v1, v2)
    assert 0 <= result <= 1


@given(vector_strategy, vector_strategy)
def test_spread_parallel_vectors(v1, v2):
    """Test that spread is 0 for parallel vectors"""
    # Create a parallel vector by scaling
    k = 2  # Scaling factor
    v2_parallel = (v1[0] * k, v1[1] * k)
    
    result = spread(v1, v2_parallel)
    assert result == 0


@given(vector_strategy)
def test_spread_perpendicular_vectors(v):
    """Test that spread is 1 for perpendicular vectors"""
    # Create a perpendicular vector by rotating 90 degrees
    v_perp = (-v[1], v[0])
    
    result = spread(v, v_perp)
    assert result == 1


@given(vector_strategy, vector_strategy)
def test_spread_symmetry(v1, v2):
    """Test that spread is symmetric: spread(v1, v2) = spread(v2, v1)"""
    # Avoid zero vectors
    assume(v1 != (0, 0) and v2 != (0, 0))
    
    result1 = spread(v1, v2)
    result2 = spread(v2, v1)
    assert result1 == result2


@given(vector_strategy, vector_strategy)
def test_spread_formula_consistency(v1, v2):
    """Test that spread formula is consistent with cross and quad functions"""
    # Avoid zero vectors
    assume(v1 != (0, 0) and v2 != (0, 0))
    
    spread_result = spread(v1, v2)
    cross_sq = cross(v1, v2) ** 2
    quad_product = quad(v1) * quad(v2)
    expected = cross_sq / quad_product
    
    # Allow for floating point precision issues
    if isinstance(spread_result, float):
        assert abs(spread_result - expected) < 1e-10
    else:
        assert spread_result == expected


@given(numeric_strategy, numeric_strategy, numeric_strategy)
def test_spread_law_range(q1, q2, q3):
    """Test that spread law returns values between 0 and 1 for valid triangles"""
    # Use positive values for quadrances
    assume(q1 > 0 and q2 > 0 and q3 > 0)
    
    # For a valid triangle, the sum of any two sides must be greater than the third
    # In terms of quadrances, this means: sqrt(q1) + sqrt(q2) > sqrt(q3)
    # We'll test this property for cases where it holds
    assume(abs(q1 + q2 - q3) < 2 * (q1 * q2) ** 0.5)  # Triangle inequality for quadrances
    
    result = spread_law(q1, q2, q3)
    assert 0 <= result <= 1


@given(numeric_strategy, numeric_strategy, numeric_strategy)
def test_spread_law_symmetry(q1, q2, q3):
    """Test that spread law is symmetric in first two arguments"""
    result1 = spread_law(q1, q2, q3)
    result2 = spread_law(q2, q1, q3)
    assert result1 == result2


@given(vector_strategy, vector_strategy)
def test_spread_law_vector_consistency(v1, v2):
    """Test that spread law is consistent with spread function for vectors"""
    # Avoid zero vectors
    assume(v1 != (0, 0) and v2 != (0, 0))
    
    # Calculate quadrances
    q1 = quad(v1)
    q2 = quad(v2)
    # Calculate q3 using the law of cosines in rational trigonometry
    v_diff = (v1[0] - v2[0], v1[1] - v2[1])
    q3 = quad(v_diff)
    
    spread_direct = spread(v1, v2)
    spread_from_law = spread_law(q1, q2, q3)
    
    # Allow for floating point precision issues
    if isinstance(spread_direct, float) or isinstance(spread_from_law, float):
        assert abs(spread_direct - spread_from_law) < 1e-10
    else:
        assert spread_direct == spread_from_law


@given(numeric_strategy, numeric_strategy, spread_strategy)
def test_triple_quad_formula_range(q1, q2, s3):
    """Test that triple quad formula returns reasonable values"""
    assume(q1 >= 0 and q2 >= 0 and 0 <= s3 <= 1)
    
    result = triple_quad_formula(q1, q2, s3)
    # The result should be non-negative for valid inputs
    assert result >= 0


@given(numeric_strategy, numeric_strategy, spread_strategy)
def test_triple_quad_formula_symmetry(q1, q2, s3):
    """Test that triple quad formula is symmetric in first two arguments"""
    result1 = triple_quad_formula(q1, q2, s3)
    result2 = triple_quad_formula(q2, q1, s3)
    assert result1 == result2


@given(numeric_strategy, numeric_strategy, spread_strategy)
def test_triple_quad_formula_extreme_cases(q1, q2, s3):
    """Test triple quad formula for extreme cases"""
    assume(q1 >= 0 and q2 >= 0 and 0 <= s3 <= 1)
    
    # When spread is 0, result should be (q1 - q2)^2
    if s3 == 0:
        result = triple_quad_formula(q1, q2, s3)
        expected = (q1 - q2) ** 2
        # Allow for floating point precision issues
        if isinstance(result, float) or isinstance(expected, float):
            assert abs(result - expected) < 1e-10
        else:
            assert result == expected
    
    # When spread is 1, result should be (q1 + q2)^2
    if s3 == 1:
        result = triple_quad_formula(q1, q2, s3)
        expected = (q1 + q2) ** 2
        # Allow for floating point precision issues
        if isinstance(result, float) or isinstance(expected, float):
            assert abs(result - expected) < 1e-10
        else:
            assert result == expected


@given(vector_strategy, vector_strategy)
def test_triple_quad_formula_vector_consistency(v1, v2):
    """Test that triple quad formula is consistent with vector operations"""
    # Avoid zero vectors
    assume(v1 != (0, 0) and v2 != (0, 0))
    
    q1 = quad(v1)
    q2 = quad(v2)
    s3 = spread(v1, v2)
    
    result = triple_quad_formula(q1, q2, s3)
    # According to the formula: (q1 + q2)^2 - 4*q1*q2*(1-s3)
    expected = (q1 + q2) ** 2 - 4 * q1 * q2 * (1 - s3)
    
    # Allow for floating point precision issues
    if isinstance(result, float) or isinstance(expected, float):
        assert abs(result - expected) < 1e-10
    else:
        assert result == expected





if __name__ == "__main__":
    import pytest

    pytest.main()