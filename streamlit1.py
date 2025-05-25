import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter fungsi produksi
A = 1
alpha = 0.5
beta = 0.5

# Buat grid nilai x dan y
x = np.linspace(1, 100, 50)  # kedelai (kg/hari)
y = np.linspace(1, 100, 50)  # tenaga kerja (orang/hari)
X, Y = np.meshgrid(x, y)

# Fungsi produksi Cobb-Douglas
Z = A * (X ** alpha) * (Y ** beta)

# Visualisasi permukaan
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Label
ax.set_title("Permukaan Fungsi Produksi Tahu")
ax.set_xlabel("Kedelai (kg/hari)")
ax.set_ylabel("Tenaga Kerja (orang/hari)")
ax.set_zlabel("Produksi (unit tahu)")

plt.show()
