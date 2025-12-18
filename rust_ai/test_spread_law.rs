fn spread_law(q_1: i32, q_2: i32, q_3: i32) -> i32 {
    let numerator = 4*q_1*q_2 - (q_1 + q_2 - q_3)*(q_1 + q_2 - q_3);
    let denominator = 4 * q_1 * q_2;
    numerator / denominator
}

fn main() {
    let q_1 = 5;
    let q_2 = 25;
    let q_3 = 20;
    println!("spread_law({}, {}, {}) = {}", q_1, q_2, q_3, spread_law(q_1, q_2, q_3));
}
