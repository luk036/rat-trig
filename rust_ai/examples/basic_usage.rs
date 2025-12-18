//! Basic usage examples for the rat-trig library

use num_rational::Ratio;
use rat_trig::{archimedes, cross, dot, quad, spread, spread_law, triple_quad_formula};

fn main() {
    println!("=== Rational Trigonometry Examples ===\n");

    // Example 1: Archimedes' formula
    println!("1. Archimedes' formula:");
    let q1 = Ratio::new(1, 2);
    let q2 = Ratio::new(1, 4);
    let q3 = Ratio::new(1, 6);
    let arch_result = archimedes(q1, q2, q3);
    println!("   archimedes({}, {}, {}) = {}", q1, q2, q3, arch_result);
    println!();

    // Example 2: Vector operations
    println!("2. Vector operations:");
    let v1 = [1, 2];
    let v2 = [3, 4];

    let cross_result = cross(v1, v2);
    let dot_result = dot(v1, v2);
    let quad_result = quad(v1);

    println!("   v1 = {:?}, v2 = {:?}", v1, v2);
    println!("   cross(v1, v2) = {}", cross_result);
    println!("   dot(v1, v2) = {}", dot_result);
    println!("   quad(v1) = {}", quad_result);
    println!();

    // Example 3: Spread calculation
    println!("3. Spread calculation:");
    let v3 = [Ratio::new(1, 1), Ratio::new(2, 1)];
    let v4 = [Ratio::new(3, 1), Ratio::new(4, 1)];
    let spread_result = spread(v3, v4);
    println!("   v3 = {:?}, v4 = {:?}", v3, v4);
    println!("   spread(v3, v4) = {}", spread_result);
    println!();

    // Example 4: Spread law
    println!("4. Spread law:");
    let q1_sl = 5;
    let q2_sl = 25;
    let q3_sl = 20;
    let spread_law_result = spread_law(q1_sl, q2_sl, q3_sl);
    println!(
        "   spread_law({}, {}, {}) = {}",
        q1_sl, q2_sl, q3_sl, spread_law_result
    );
    println!();

    // Example 5: Triple quad formula
    println!("5. Triple quad formula:");
    let q1_tq = Ratio::new(5, 1);
    let q2_tq = Ratio::new(25, 1);
    let s3_tq = Ratio::new(4, 125);
    let triple_quad_result = triple_quad_formula(q1_tq, q2_tq, s3_tq);
    println!(
        "   triple_quad_formula({}, {}, {}) = {}",
        q1_tq, q2_tq, s3_tq, triple_quad_result
    );
    println!();

    // Example 6: Different numeric types
    println!("6. Working with different numeric types:");

    // Integers
    let int_result = archimedes(2, 4, 6);
    println!("   Integers: archimedes(2, 4, 6) = {}", int_result);

    // Floats
    let float_result = archimedes(2.0, 4.0, 6.0);
    println!("   Floats: archimedes(2.0, 4.0, 6.0) = {}", float_result);

    // Mixed (requires same type in Rust)
    let mixed_q1 = Ratio::new(1, 1);
    let mixed_q2 = Ratio::new(1, 2);
    let mixed_q3 = Ratio::new(2, 1);
    let mixed_result = archimedes(mixed_q1, mixed_q2, mixed_q3);
    println!("   Fractions: archimedes(1, 1/2, 2) = {}", mixed_result);
}
