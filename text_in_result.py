import logging
import subprocess


def is_text_in_command_output(command, text):
    """
        Проверяет, содержится ли указанный текст в выводе выполнения команды.

        Args:
            command (str): Команда для выполнения.
            text (str): Текст, который нужно найти в выводе команды.

        Returns:
            bool: True, если текст найден в выводе команды, False в противном случае.
        """
    try:
        output = subprocess.check_output(command, shell=True, encoding='utf-8')

        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        logging.error(f'{e}')
        return False
