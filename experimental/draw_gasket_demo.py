"""
Apollonian Gasket Demo - GPU-accelerated generation of Apollonian circles.

This module demonstrates using Numba CUDA to generate Apollonian circles
(also known as Apollonian gasket) using the complex Descartes circle theorem.
The algorithm creates a fractal of circles that are all tangent to each other.

Example:
    Run with: python draw_gasket_demo.py
"""

import matplotlib.pyplot as plt
import numpy as np
from numba import cuda


# The kernel handles the complex arithmetic and linear flipping
# kz = curvature * complex_center
@cuda.jit
def flip_circles_kernel(
    ks, kzs_real, kzs_imag, indices, out_ks, out_kzs_real, out_kzs_imag
):
    """CUDA kernel to flip circles using the complex Descartes theorem.

    Applies the Descartes circle theorem in complex form to generate
    new circles from existing ones. Each thread processes one branch
    of the recursive gasket construction.

    :param ks: Array of curvatures.
    :param kzs_real: Array of real parts of complex curvatures.
    :param kzs_imag: Array of imaginary parts of complex curvatures.
    :param indices: Array of indices defining which circles to flip.
    :param out_ks: Output array for new curvatures.
    :param out_kzs_real: Output array for new complex curvature real parts.
    :param out_kzs_imag: Output array for new complex curvature imaginary parts.
    """
    idx = cuda.grid(1)
    if idx < indices.shape[0]:
        # Identify the 4 circles in this branch
        i1 = indices[idx, 0]
        i2 = indices[idx, 1]
        i3 = indices[idx, 2]
        i4 = indices[idx, 3]  # The circle to be replaced (the "old" root)

        # 1. Curvature Flip (Descartes' Theorem)
        # k_new = 2*(k1 + k2 + k3) - k4
        out_ks[idx] = 2.0 * (ks[i1] + ks[i2] + ks[i3]) - ks[i4]

        # 2. Complex Curvature Flip (Complex Descartes' Theorem)
        # kz_new = 2*(kz1 + kz2 + kz3) - kz4
        out_kzs_real[idx] = (
            2.0 * (kzs_real[i1] + kzs_real[i2] + kzs_real[i3]) - kzs_real[i4]
        )
        out_kzs_imag[idx] = (
            2.0 * (kzs_imag[i1] + kzs_imag[i2] + kzs_imag[i3]) - kzs_imag[i4]
        )


def draw_gasket():
    """Generate and visualize an Apollonian gasket using GPU computation.

    Sets up an initial configuration of four mutually tangent circles
    and uses the complex Descartes theorem to generate new circles
    that fill the gaps between them.
    """
    # k = -1 (outer), k = 2, 2, 3 (inner)
    ks = np.array([-1.0, 2.0, 2.0, 3.0], dtype=np.float32)

    # Calculate initial centers (z) and then complex curvatures (kz = k*z)
    # Centers chosen to satisfy mutual tangency for these specific curvatures
    z = np.array([0 + 0j, -0.5 + 0j, 0.5 + 0j, 0 + 0.666j], dtype=np.complex64)
    kz = ks * z

    # Move to Device
    d_ks = cuda.to_device(ks)
    d_kz_real = cuda.to_device(kz.real.astype(np.float32))
    d_kz_imag = cuda.to_device(kz.imag.astype(np.float32))

    # Define which triplets to "flip" to find new circles
    # This matrix defines the recursive branches
    indices = np.array(
        [
            [0, 1, 2, 3],  # Keep 0,1,2, flip 3
            [0, 1, 3, 2],  # Keep 0,1,3, flip 2
            [0, 2, 3, 1],  # Keep 0,2,3, flip 1
            [1, 2, 3, 0],  # Keep 1,2,3, flip 0
        ],
        dtype=np.int32,
    )
    d_indices = cuda.to_device(indices)

    # Output buffers
    out_ks = cuda.device_array(4, dtype=np.float32)
    out_kz_r = cuda.device_array(4, dtype=np.float32)
    out_kz_i = cuda.device_array(4, dtype=np.float32)

    # Launch kernel
    threadsperblock = 32
    blockspergrid = (indices.shape[0] + (threadsperblock - 1)) // threadsperblock
    flip_circles_kernel[blockspergrid, threadsperblock](
        d_ks, d_kz_real, d_kz_imag, d_indices, out_ks, out_kz_r, out_kz_i
    )

    # Bring results back to CPU
    final_ks = out_ks.copy_to_host()
    final_z = (out_kz_r.copy_to_host() + 1j * out_kz_i.copy_to_host()) / final_ks

    # Visualization
    fig, ax = plt.subplots(figsize=(8, 8))
    for i in range(len(final_ks)):
        r = abs(1 / final_ks[i])
        circle = plt.Circle(
            (final_z[i].real, final_z[i].imag), r, fill=False, color="blue"
        )
        ax.add_artist(circle)

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect("equal")
    plt.title("GPU Generated Apollonian Circles (Numba CUDA)")
    plt.show()


if __name__ == "__main__":
    draw_gasket()
