# Colored bricks
Colored brick nodes for Luanti Minetest.

![Preview](https://raw.githubusercontent.com/limafresh/coloredbricks/main/preview.png)

## Information for developers
The textures were created by applying noise to a flat texture.

To create a new brick texture, you can follow these steps:

1. Make a copy of `brick_flat.png` (for example, `brick_flat1.png`).
2. Change the color of the bricks in `brick_flat1.png` in a raster graphics editor.
3. Python and the Pillow library are required. Pillow can be installed using

```
pip install Pillow
```

Run:

```
python noise.py brick_flat1.png brick_name.png
```

Optionally, you could also add intensity (--intensity or -i), for example

```
python noise.py brick_flat1.png brick_name.png -i=20
```
