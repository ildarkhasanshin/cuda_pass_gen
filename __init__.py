import os
import random
from cudatext import *

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_pass_gen.ini')

pass_length = 8
pass_symbols = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ!?.'

class Command:
    
    def __init__(self):
        global pass_length
        global pass_symbols
        pass_length = int(ini_read(fn_config, 'options', 'pass_length', str(pass_length)))
        pass_symbols = ini_read(fn_config, 'options', 'pass_symbols', str(pass_symbols))

    def config(self):
        ini_write(fn_config, 'options', 'pass_length', str(pass_length))
        ini_write(fn_config, 'options', 'pass_symbols', str(pass_symbols))
        file_open(fn_config)
        
    def run(self):
        pass_gen = ''
        for x in range(pass_length):
            pass_gen = pass_gen + random.choice(list(pass_symbols))
        x0, y0, x1, y1 = ed.get_carets()[0]
        ed.insert(x0, y0, pass_gen)