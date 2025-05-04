import os
import random
from cudatext import *

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_pass_gen.ini')

pass_length = 8
pass_symbols = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!?.@#$%'
pass_unique = 1

class Command:

    def __init__(self):
        global pass_length
        global pass_symbols
        global pass_unique
        pass_length = int(ini_read(fn_config, 'options', 'pass_length', str(pass_length)))
        pass_symbols = ini_read(fn_config, 'options', 'pass_symbols', str(pass_symbols))
        pass_unique = int(ini_read(fn_config, 'options', 'pass_unique', str(pass_unique))) # without repeating characters

    def config(self):
        ini_write(fn_config, 'options', 'pass_length', str(pass_length))
        ini_write(fn_config, 'options', 'pass_symbols', str(pass_symbols))
        ini_write(fn_config, 'options', 'pass_unique', str(pass_unique))
        file_open(fn_config)

    def run(self):
        pass_gen = ''
        for x in range(pass_length):
            symbol = random.choice(list(pass_symbols))
            if pass_unique:
                while symbol in pass_gen:
                    symbol = random.choice(list(pass_symbols))
            pass_gen = pass_gen + symbol
        x0, y0, x1, y1 = ed.get_carets()[0]
        if (y0, x0) > (y1, x1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        ed.insert(x1, y1, pass_gen)
        ed.set_caret(x1 + pass_length, y1, x1, y1)