import sys
import os


class Marker:

    SWITCH = True

    _RESET = '\x1b[0m'

    _FG = '38'
    _BG = '48'

    @staticmethod
    def _hex_to_rgb(color: str) -> tuple:
        """
        #ffffff -> (255, 255, 255)
        """
        color = color.strip('#')
        return int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)

    @classmethod
    def _format(cls, fg, bg):
        fg_tag = f'\x1b[{cls._FG};2;{fg[0]};{fg[1]};{fg[2]}m' if fg else str()
        bg_tag = f'\x1b[{cls._BG};2;{bg[0]};{bg[1]};{bg[2]}m' if bg else str()
        return f'{fg_tag}{bg_tag}'

    @staticmethod
    def _is_valid_rgb_color_tuple(data):
        """
        RGB tuple must contain 3 numbers and all of them must between 0 to 255.
        """
        if not (isinstance(data, tuple) and len(data) == 3):
            return False
        for value in data:
            if not (isinstance(value, int) and 0 <= value <= 255):
                return False
        return True

    @staticmethod
    def _is_valid_hex_color_code(data):
        """
        Hex color code required prefix "#", followed with 6 numbers and or alphabets which including
        "0" to "9" and "A" to "F" (case-insensitive).
        """
        if not (isinstance(data, str) and data.startswith('#')):
            return False
        color = data.strip('#').upper()
        if len(color) != 6:
            return False
        for character in color:
            if character.isdigit():
                continue
            if character in {'A', 'B', 'C', 'D', 'E', 'F'}:
                continue
            return False
        return True

    @classmethod
    def _rgb_adapter(cls, color):
        if color is None:
            return None
        if cls._is_valid_rgb_color_tuple(data=color):
            return color
        if cls._is_valid_hex_color_code(data=color):
            return cls._hex_to_rgb(color=color)
        raise ValueError(f'Input color required "hex color code" or a "RGB color tuple". {color}')

    @classmethod
    def get_tag(cls, fg=None, bg=None):
        """
        Call the function without any params will return reset tag.
        :param fg: foreground(text) color, accept 2 different way to set color '#ffffff' or (255, 255, 255)
        :type fg: str or tuple
        :param bg: background color, accept 2 different way to set color '#ffffff' or (255, 255, 255)
        :type bg: str or tuple
        :rtype: str
        :return: terminal color tag
        """
        if not cls.SWITCH:
            return str()
        if fg is None and bg is None:
            return cls._RESET
        tag = cls._format(fg=cls._rgb_adapter(color=fg),
                          bg=cls._rgb_adapter(color=bg))
        return tag

    @classmethod
    def print(cls, line, fg=None, bg=None, end='\n', file=sys.stdout, flush=False):
        """
        :param line: A line you'd like to display on the terminal.
        :type line: str
        :param fg: foreground(text) color, accept 2 different way to set color '#ffffff' or (255, 255, 255)
        :type fg: str or tuple
        :param bg: background color, accept 2 different way to set color '#ffffff' or (255, 255, 255)
        :type bg: str or tuple
        :param end: Optional. Specify what to print at the end. Default is '\n' (line feed)
        :param file: Optional. An object with a write method. Default is sys.stdout
        :param flush: Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False
        :rtype: None
        :return: None
        """
        tag = cls.get_tag(fg=fg, bg=bg)
        reset = cls._RESET if cls.SWITCH else str()
        print(f'{tag}{line}{reset}', end=end, file=file, flush=flush)

    @classmethod
    def set(cls, fg=None, bg=None, mark=False):
        """
        :param fg: foreground(text) color, accept 2 different way to set color '#ffffff' or (255, 255, 255)
        :type fg: str or tuple
        :param bg: background color, accept 2 different way to set color '#ffffff' or (255, 255, 255)
        :type bg: str or tuple
        :param mark: toggle divider, default is False.
        :type mark: bool
        :rtype: None
        :return: None
        """
        if mark and cls.SWITCH:
            print(f'{" START ":=^76}', end='\r', flush=True)
        tag = cls.get_tag(fg=fg, bg=bg)
        print(tag)

    @classmethod
    def reset(cls, mark=False):
        """
        :param mark: toggle divider, default is False.
        :type mark: bool
        """
        if not cls.SWITCH:
            return None
        if mark:
            print(f'{" END ":=^76}', end='\r', flush=True)
        print(cls._RESET)
