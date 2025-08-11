# draw_diagram.py
# Draw a top-view diagram of 8 circles (2 rows x 4 cols), each radius = 3 cm
import matplotlib.pyplot as plt
from pathlib import Path

out_dir = Path(".")
r_cm = 3
scale_px_per_cm = 20
r = r_cm * scale_px_per_cm
diam = 2 * r
cols, rows = 4, 2
padding = int(r * 0.5)
width_px = int(cols * diam + 2 * padding)
height_px = int(rows * diam + 2 * padding)

fig = plt.figure(figsize=(width_px/100, height_px/100), dpi=100)
ax = fig.add_subplot(111)
ax.set_xlim(0, width_px)
ax.set_ylim(0, height_px)
ax.set_aspect('equal')
ax.axis('off')

for row in range(rows):
    for col in range(cols):
        cx = padding + r + col * diam
        cy = padding + r + row * diam
        circle = plt.Circle((cx, cy), r, fill=False, linewidth=2)
        ax.add_patch(circle)

rect = plt.Rectangle((padding, padding), cols*diam, rows*diam, fill=False, linewidth=2, linestyle='--')
ax.add_patch(rect)

ax.text(width_px*0.02, height_px*0.05, r"$r = 3\ \mathrm{cm}$", fontsize=10)
ax.text(width_px*0.02, height_px*0.10, r"$d = 2r = 6\ \mathrm{cm}$", fontsize=10)

img_path = out_dir / "pack_8_balls.png"
plt.savefig(img_path, bbox_inches='tight', dpi=150)
plt.close(fig)
print(f"Saved diagram to {img_path}")
