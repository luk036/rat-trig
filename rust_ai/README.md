# rat-trig - Rational Trigonometry in Rust

A Rust implementation of Norman Wildberger's Rational Trigonometry.

## Overview

Rational Trigonometry is a new approach to classical trigonometry, developed by Norman
Wildberger, that aims to simplify and clarify the subject by using only rational numbers
and operations, rather than irrational numbers and limits.

In traditional trigonometry, concepts such as the sine, cosine, and tangent of an angle
are typically defined using circles and the unit circle in particular. These definitions
involve irrational numbers and limits, which can make the subject more difficult to
understand and work with.

In rational trigonometry, Wildberger replaces these circular definitions with ones based
on lines and line segments, which allows for a more straightforward and intuitive approach.
The fundamental concepts in rational trigonometry are the "quadaverage" and the "dilated
directed angle," which are defined in terms of lines and line segments, rather than circles.

## Features

- **Archimedes' formula**: Calculate the quadrea of a triangle
- **Vector operations**: Cross product, dot product, and quadrance (squared length)
- **Spread calculations**: Rational alternative to sine squared
- **Spread law**: Rational trigonometry's version of the law of sines
- **Triple quad formula**: Relationship between three quadrances
- **Multiple numeric types**: Support for integers, fractions, and floating-point numbers
- **CLI tool**: Fibonacci number calculator example

## Installation

Add this to your `Cargo.toml`:

```toml
[dependencies]
rat-trig = "0.1.0"
```

Or install the CLI tool:

```bash
cargo install --path .
```

## Usage

### As a Library

```rust
use rat_trig::{archimedes, cross, dot, quad, spread, spread_law, triple_quad_formula};
use num_rational::Ratio;

// Calculate Archimedes' formula
let q1 = Ratio::new(1, 2);
let q2 = Ratio::new(1, 4);
let q3 = Ratio::new(1, 6);
let result = archimedes(q1, q2, q3);
println!("Archimedes: {}", result);

// Calculate cross product
let v1 = [1, 2];
let v2 = [3, 4];
let cross_result = cross(v1, v2);
println!("Cross product: {}", cross_result);

// Calculate spread
let spread_result = spread(v1, v2);
println!("Spread: {}", spread_result);
```

### CLI Tool

The package includes a Fibonacci calculator as an example CLI tool:

```bash
# Calculate the 10th Fibonacci number
cargo run --bin fibonacci -- 10

# With verbose output
cargo run --bin fibonacci -- -v 10

# With very verbose output
cargo run --bin fibonacci -- -V 10
```

## API Reference

### Core Functions

- `archimedes(q1, q2, q3)`: Calculate quadrea using Archimedes' formula
- `cross(v1, v2)`: Calculate 2D cross product
- `dot(v1, v2)`: Calculate dot product
- `quad(v)`: Calculate quadrance (squared length)
- `spread(v1, v2)`: Calculate spread between vectors
- `spread_law(q1, q2, q3)`: Calculate spread using spread law
- `triple_quad_formula(q1, q2, s3)`: Calculate using triple quad formula
- `fib(n)`: Calculate n-th Fibonacci number

### Numeric Types

The library uses a `Numeric` trait that supports:
- Integers (`i32`, `i64`, etc.)
- Rational numbers (`num_rational::Ratio`)
- Floating-point numbers (`f32`, `f64`)

## Examples

See the `examples/` directory for more usage examples.

## Testing

Run the tests with:

```bash
cargo test
```

Run tests with verbose output:

```bash
cargo test -- --nocapture
```

## License

MIT License - see LICENSE file for details.

## Author

Wai-Shing Luk <luk036@gmail.com>

## Acknowledgments

- Norman Wildberger for developing Rational Trigonometry
- The Rust community for excellent tooling and libraries
