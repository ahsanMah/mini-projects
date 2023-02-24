#%%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def julia(N):
    # Create the mandelbrot set
    x = np.linspace(-2, 2, N)   # real axis
    y = np.linspace(-2, 2, N)       # imaginary axis
    zs = x + 1j * y[:, np.newaxis]  # complex plane
    c = -0.123 + 0.745j
    # c = -0.4 + 0.6j
    # c = -0.8 + 0.156j
    # c = -0.7269 + 0.1889j
    counts = np.zeros((N, N), dtype=np.uint8)
    cutoff = 3
    # z = counts[]
    for i in range(N):
        for j in range(N):
            # c = complex(-1.5 + i / 50, -1 + j / 50)
            z = zs[i, j]
            for k in np.arange(100):
                z = z * z + c
                if abs(z) > cutoff:
                    counts[i, j] = k
                    break
    
    return counts

def fast_julia(N, max_iters=255):
    # Create the mandelbrot set
    x = np.linspace(-2, 2, N)   # real axis
    y = np.linspace(-2, 2, N)       # imaginary axis
    zs = x + 1j * y[:, np.newaxis]  # complex plane
    c = -0.123 + 0.745j
    # c = -0.4 + 0.6j
    # c = -0.8 + 0.156j
    # c = -0.7269 + 0.1889j
    counts = np.zeros((N, N), dtype=np.uint8)
    cutoff_mask = np.ones((N, N), dtype=np.uint8)
    cutoff = 3
    # z = counts[]
    # for i in range(max_iters):
    #     # i want to multiply by 1 or z[i,j] 
    #     zs *= (~cutoff_mask)+(zs * cutoff_mask) #FIXME: yeah this multiplies by zero idiot
    #     zs += (c * cutoff_mask)
    #     cutoff_mask = np.abs(zs) < cutoff
    #     # zs *= cutoff_mask
    #     counts += cutoff_mask
    
    for i in range(max_iters):
        zs *= zs
        zs += c
        counts += np.abs(zs) < cutoff

    counts[counts == max_iters] = 0
    return counts


# %%
m = fast_julia(200, 100)
plt.imshow(m, cmap='hot')
plt.axis("off")
plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
plt.colorbar()
plt.tight_layout()
#%%
m = julia(200)
plt.imshow(m, cmap='hot')
plt.axis("off")
plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
plt.colorbar()
plt.tight_layout()

# %%
%timeit julia(200)
# %%
%timeit fast_julia(200, 100)
# %%
