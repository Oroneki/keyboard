# -*- coding: utf-8 -*-

from time import time as now

KEY_DOWN = 'down'
KEY_UP = 'up'

class KeyboardEvent(object):
    def __init__(self, event_type, scan_code, name=None, time=None):
        self.event_type = event_type
        self.scan_code = scan_code
        self.time = now() if time is None else time
        self.name = normalize_name(name)

    def matches(self, description):
        if isinstance(description, int):
            return self.scan_code == description
        else:
            normalized = normalize_name(description)
            return (
                normalized == self.name
                or 'left ' + normalized == self.name
                or 'right ' + normalized == self.name
            )

    def __repr__(self):
        return 'KeyboardEvent({} {})'.format(self.name or 'Unknown {}'.format(self.scan_code), self.event_type)

canonical_names = {
    'escape': 'esc',
    'return': 'enter',
    'del': 'delete',
    'control': 'ctrl',
    'altgr': 'alt gr',

    '\x1b': 'esc',
    '\x08': 'backspace',
    '\n': 'enter',
    '\t': 'tab',

    'scrlk': 'scroll lock',
    'prtscn': 'print screen',
    'prnt scrn': 'print screen',
    'snapshot': 'print screen',
    'ins': 'insert',
    'pause break': 'pause',
    'ctrll lock': 'caps lock',
    'number lock': 'num lock',
    'numlock:': 'num lock',
    'space bar': 'space',
    'spacebar': 'space',
    'linefeed': 'enter',

    ' ': 'space',
    'underscore': '_',

    'equal': '=',
    'minplus': '+',
    'plus': '+',
    'add': '+',
    'subtract': '-',
    'minus': '-',
    'multiply': '*',
    'asterisk': '*',
    'divide': '/',

    'question': '?',
    'exclam': '!',
    'slash': '/',
    'bar': '|',
    'backslash': '\\',
    'braceleft': '{',
    'braceright': '}',
    'bracketleft': '[',
    'bracketright': ']',
    'parenleft': '(',
    'parenright': ')',

    'period': '.',
    'comma': ',',
    'semicolon': ';',
    'colon': ':',

    'less': '<',
    'greater': '>',
    'ampersand': '&',
    'at': '@',
    'numbersign': '#',
    'hash': '#',
    'hashtag': '#',

    'dollar': '$',
    'sterling': '£',
    'pound': '£',
    'yen': '¥',
    'euro': '€',
    'cent': '¢',
    'currency': '¤',
    'registered': '®',
    'copyright': '©',
    'notsign': '¬',
    'percent': '%',
    'diaeresis': '"',
    'quotedbl': '"',
    'onesuperior': '¹',
    'twosuperior': '²',
    'threesuperior': '³',
    'onehalf': '½',
    'onequarter': '¼',
    'threequarters': '¾',
    'paragraph': '¶',
    'section': '§',
    'ssharp': '§',
    'division': '÷',
    'questiondown': '¿',
    'exclamdown': '¡',
    'degree': '°',
    'guillemotright': '»',
    'guillemotleft': '«',
    
    'acute': '´',
    'agudo': '´',
    'grave': '`',
    'tilde': '~',
    'asciitilde': '~',
    'til': '~',
    'cedilla': ',',
    'circumflex': '^',
    'apostrophe': '\'',
    
    'adiaeresis': 'ä',
    'udiaeresis': 'ü',
    'odiaeresis': 'ö',
    'oe': 'Œ',
    'oslash': 'ø',
    'ooblique': 'Ø',
    'ccedilla': 'ç',
    'ntilde': 'ñ',
    'eacute': 'é',
    'uacute': 'ú',
    'oacute': 'ó',
    'thorn': 'þ',
    'ae': 'æ',
    'eth': 'ð',
    'masculine': 'º',
    'feminine': 'ª',
    'iacute': 'í',
    'aacute': 'á',
    'mu': 'Μ',
    'aring': 'å',

    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def normalize_name(name):
    name = name.lower()
    if name != '_':
        name = name.replace('_', ' ')
    return canonical_names.get(name, name)
