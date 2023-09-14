"""
    ---Task 1---
    Задание 1.
Условие:
Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

*Задание 2. *
• Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.
"""
from checkout import checkout
from hash_calc import calc_crc32
from text_in_result import is_text_in_command_output

FOLDERIN = '/tmp/user/folder1'
FOLDEROUT = '/tmp/user/out'

def test_list():
    assert checkout(f'cd {FOLDEROUT}; 7zz l arch1.7z', 'Path = arch1.7z')

def test_crc32():
    crc = calc_crc32(f'{FOLDEROUT}/arch1.7z')
    assert is_text_in_command_output(f'cd {FOLDEROUT}; 7zz h arch1.7z', crc)
