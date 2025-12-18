//! This is a skeleton file that can serve as a starting point for a Rust
//! console script. To run this script, use:
//! `cargo run --bin fibonacci -- <n>`
//!
//! Besides console scripts, this file can also be used as template for Rust modules.
//!
//! Note:
//!     This file can be renamed depending on your needs or safely removed if not needed.

use clap::Parser;

/// Fibonacci example function
///
/// # Arguments
///
/// * `n` - integer (must be > 0)
///
/// # Returns
///
/// n-th Fibonacci number
///
/// # Examples
///
/// ```
/// use rat_trig::fib;
/// assert_eq!(fib(1), 1);
/// assert_eq!(fib(2), 1);
/// assert_eq!(fib(3), 2);
/// assert_eq!(fib(4), 3);
/// assert_eq!(fib(5), 5);
/// assert_eq!(fib(6), 8);
/// ```
///
/// ```text
/// F(1)=1  F(2)=1  F(3)=2  F(4)=3  F(5)=5  F(6)=8  ...
///   *     *     **    ***   ***** ******** ...
/// ```
fn fib(n: u64) -> u64 {
    assert!(n > 0);
    let mut a = 1;
    let mut b = 1;
    for _ in 0..(n - 1) {
        let temp = a + b;
        a = b;
        b = temp;
    }
    a
}

/// Command line arguments
#[derive(Parser, Debug)]
#[command(author, about = "Just a Fibonacci demonstration")]
struct Args {
    /// n-th Fibonacci number
    n: u64,

    /// Set loglevel to INFO
    #[arg(short = 'v', long = "verbose", action = clap::ArgAction::SetTrue)]
    verbose: bool,

    /// Set loglevel to DEBUG
    #[arg(short = 'V', long = "very-verbose", action = clap::ArgAction::SetTrue)]
    very_verbose: bool,
}

fn main() {
    let args = Args::parse();

    // Set log level based on verbosity
    let log_level = if args.very_verbose {
        log::Level::Debug
    } else if args.verbose {
        log::Level::Info
    } else {
        log::Level::Error
    };

    // Simple logging setup
    env_logger::Builder::new()
        .filter_level(log_level.to_level_filter())
        .init();

    log::debug!("Starting crazy calculations...");

    let result = fib(args.n);
    println!("The {}-th Fibonacci number is {}", args.n, result);

    log::info!("Script ends here");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fib() {
        assert_eq!(fib(1), 1);
        assert_eq!(fib(2), 1);
        assert_eq!(fib(3), 2);
        assert_eq!(fib(4), 3);
        assert_eq!(fib(5), 5);
        assert_eq!(fib(6), 8);
        assert_eq!(fib(7), 13);
        assert_eq!(fib(8), 21);
        assert_eq!(fib(9), 34);
        assert_eq!(fib(10), 55);
    }

    #[test]
    #[should_panic]
    fn test_fib_zero() {
        fib(0);
    }
}
