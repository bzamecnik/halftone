# halftone

Halftoning in Python.

```shell
pip install halftone
```

```
import halftone as ht
import PIL.Image

img = PIL.Image.open('foo.png')

halftoned = ht.halftone(img, ht.euclid_dot(spacing=8, angle=30))

halftoned.save('bar.png)
```

<img src="examples/gradient_halftone.png">

Check the example notebook: [notebooks/halftoning.ipynb]([notebook/halftoning.ipynb]).
