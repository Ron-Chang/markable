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
    
    - render single line by the method 'dye':
        ```python
        Varimarkable.dye(line='Hello World!', fg='#ff0000')
        ```
        or
        ```python
        Varimarkable.dye(line='Hello World!', fg=(255, 0, 0))
        ```

    - set multiple lines render start point:
        ```python
        Varimarkable.set_color(bg='#ffff00')
        print('SOMETHING')
        print('TEST')
        print('DEBUG')
        Varimarkable.reset()
        ```

    - Disable all tags
        ```python
        from path.name import Varimarkable
        Varimarkable.SWITCH = False
        ```

