# MARKABLE

## Aim:
- Render text in terminal
    * __HEX__ color tag string. e.g. `'#ff00ff'`
    * __RGB__ tuple. e.g. `(255, 0, 255)`
- Render single/multiple lines
- Global trigger

## How to use:
> Note: Marker.print() method inherited few parameters from print(`end='\n'`, `flush=False`, `file=sys.stdout`)

### - Proceed a single line:

```python
from markable import Marker

Marker.print(line='Hello World!', fg='#ff0000')  # case-insensitive
Marker.print(line='Hello World!', fg=(255, 0, 0))
```

### - Proceed a multiple lines:

```python
from markable import Marker

Marker.set(bg='#ffff00')  # set start point
print('SOMETHING')  # do 
print('TEST')  # somethin
print('DEBUG')  # here
Marker.reset()  # reset to default
```

### - Global trigger:

```python
from markable import Marker
Marker.SWITCH = False
```

If you like my work, please consider buying me a coffee or [PayPal](https://paypal.me/RonDevStudio?locale.x=zh_TW)
Thanks for your support! Cheers! 🎉
<a href="https://www.buymeacoffee.com/ronchang" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" align="right"></a>
