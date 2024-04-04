import os

USER_HOME = os.path.expanduser('~')
LOG_DIRECTORY = USER_HOME+"/Documents/Ableton/User Library/Remote Scripts"
try:
    os.makedirs(LOG_DIRECTORY, exist_ok=True)
except TypeError:
    try:
        os.makedirs(LOG_DIRECTORY)
    except OSError:
        pass
LOG_FILE = LOG_DIRECTORY + "/log.txt"

log_num = 0


def log(message):
    global log_num
    if log_num == 0:
        with open(LOG_FILE, 'a') as f:
            f.write('====================\n')
    temp = ''
    if not(message.__class__.__module__ == 'builtins'):
        for att in dir(message):
            value = getattr(message, att)
            temp += att + ' ' + str(getattr(message, att)) + '\n'
        message = temp

    with open(LOG_FILE, 'a') as f:
        if type(message) == list:
            message = '\n'.join(message)
        f.write(str(log_num) + ' ' + str(message) + '\n')
    log_num += 1