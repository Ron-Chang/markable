# VARImarkABLE

## Aim:
- Render text in terminal
    * hex color tag string. e.g. '#ff00ff'
    * rgb tuple. e.g. (255, 0, 255)
- Render single/multiple lines
- Global trigger

## How to use:
    
```python
from path.name import Varimarkable
```

- render a single line:
```python
Varimarkable.dye(line='Hello World!', fg='#ff0000')
```
or
```python
Varimarkable.dye(line='Hello World!', fg=(255, 0, 0))
```

- set a start point for multiple lines rendering:
```python
Varimarkable.set_color(bg='#ffff00')
print('SOMETHING')
print('TEST')
print('DEBUG')
Varimarkable.reset_color()
```

- Disable all tags
```python
from path.name import Varimarkable
Varimarkable.SWITCH = False
```

If you like my work, please consider buying me a coffee or [PayPal](https://paypal.me/RonDevStudio?locale.x=zh_TW)
Thank you for your support! Cheers! 🎉
<a href="https://www.buymeacoffee.com/ronchang" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" align="right"></a>
