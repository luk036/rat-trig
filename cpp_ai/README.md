# rat-trig C++

A C++20 implementation of Norman Wildberger's Rational Trigonometry.

## Overview

Rational Trigonometry is a new approach to classical trigonometry, developed by Norman Wildberger, that aims to simplify and clarify the subject by using only rational numbers and operations, rather than irrational numbers and limits.

This C++ library provides:
- **Type-safe** implementations using C++20 concepts
- **Header-only** design for easy integration
- **Modern C++** features (constexpr, concepts, templates)
- **Comprehensive tests** using doctest
- **Multiple build systems** support (CMake and xmake)
- **Examples** and **CLI tools**

## Features

### Core Functions
- `archimedes()`: Calculates qudrea using Archimedes' formula
- `cross()`: 2D cross product
- `dot()`: Dot product
- `quad()`: Quadrance (squared length)
- `spread()`: Spread between vectors (rational alternative to sine squared)
- `spread_law()`: Rational trigonometry's law of spreads
- `triple_quad_formula()`: Triple quad formula
- `fib()`: Fibonacci function (example utility)

### Type Support
The library uses C++20 concepts to support:
- Integers (`int`, `long`, `int64_t`, etc.)
- Floating-point numbers (`float`, `double`, `long double`)
- Any type that supports basic arithmetic operations

## Building

### Prerequisites
- C++20 compatible compiler (GCC 10+, Clang 10+, MSVC 2019+)
- CMake 3.20+ or xmake

### Using CMake
```bash
mkdir build && cd build
cmake ..
cmake --build .
```

### Using xmake
```bash
xmake
```

### Build Options
- `BUILD_SHARED_LIBS`: Build shared library (default: ON)
- `BUILD_TESTS`: Build tests (default: ON)
- `BUILD_EXAMPLES`: Build examples (default: ON)

## Usage

### As a Library
```cpp
#include "rat_trig/trigonom.hpp"
#include <iostream>

int main() {
    using namespace rat_trig;
    
    // Calculate Archimedes' formula
    double q1 = 0.5;
    double q2 = 0.25;
    double q3 = 1.0 / 6.0;
    double result = archimedes(q1, q2, q3);
    std::cout << "Result: " << result << std::endl;
    
    // Calculate cross product
    std::array<int, 2> v1 = {1, 2};
    std::array<int, 2> v2 = {3, 4};
    int cross_result = cross(v1, v2);
    std::cout << "Cross product: " << cross_result << std::endl;
    
    return 0;
}
```

### Running Examples
```bash
# Build examples first
./basic_usage
./fibonacci 10
./fibonacci -v 10    # Verbose
./fibonacci -V 10    # Very verbose
```

### Running Tests
```bash
# Build tests first
./tests
```

## API Documentation

### `archimedes(q1, q2, q3)`
Calculates the qudrea of a triangle using Archimedes' formula.

**Parameters:**
- `q1`, `q2`, `q3`: Quadrances (squared distances) of triangle sides

**Returns:** `4*q1*q2 - (q1 + q2 - q3)^2`

### `cross(v1, v2)`
Calculates the 2D cross product of two vectors.

**Parameters:**
- `v1`, `v2`: 2D vectors `[x, y]`

**Returns:** `v1.x * v2.y - v1.y * v2.x`

### `dot(v1, v2)`
Calculates the dot product of two vectors.

**Parameters:**
- `v1`, `v2`: 2D vectors `[x, y]`

**Returns:** `v1.x * v2.x + v1.y * v2.y`

### `quad(v)`
Calculates the quadrance (squared length) of a vector.

**Parameters:**
- `v`: 2D vector `[x, y]`

**Returns:** `v.x² + v.y²`

### `spread(v1, v2)`
Calculates the spread between two vectors (square of sine of angle).

**Parameters:**
- `v1`, `v2`: 2D vectors `[x, y]`

**Returns:** `cross(v1, v2)² / (quad(v1) * quad(v2))`

### `spread_law(q1, q2, q3)`
Calculates the spread using the law of spreads.

**Parameters:**
- `q1`, `q2`, `q3`: Quadrances of triangle sides

**Returns:** `(4*q1*q2 - (q1 + q2 - q3)²) / (4*q1*q2)`

### `triple_quad_formula(q1, q2, s3)`
Calculates using the triple quad formula.

**Parameters:**
- `q1`, `q2`: Quadrances
- `s3`: Spread value

**Returns:** `(q1 + q2)² - 4*q1*q2*(1 - s3)`

### `fib(n)`
Calculates the n-th Fibonacci number.

**Parameters:**
- `n`: Positive integer

**Returns:** n-th Fibonacci number

## Project Structure
```
cpp_ai/
├── include/rat_trig/
│   └── trigonom.hpp     # Main header file
├── src/
│   └── trigonom.cpp     # Implementation (mostly empty - header-only)
├── tests/               # doctest test files
├── examples/            # Example programs
├── CMakeLists.txt       # CMake build configuration
├── xmake.lua           # xmake build configuration
└── README.md           # This file
```

## License
MIT License - see LICENSE file for details.

## Author
Wai-Shing Luk (luk036@gmail.com)

## Acknowledgments
- Norman Wildberger for developing Rational Trigonometry
- The doctest team for the excellent testing framework
- The C++ community for modern C++ features