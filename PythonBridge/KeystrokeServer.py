import socket
import sys
import pyautogui

#USER_HOME = os.path.expanduser('~')
#LOG_DIRECTORY = USER_HOME + "/Documents/Ableton/User Library/Remote Scripts"
#try:
#    os.makedirs(LOG_DIRECTORY, exist_ok=True)
#except TypeError:
#    try:
#        os.makedirs(LOG_DIRECTORY)
#    except OSError:
#        pass
#LOG_FILE = LOG_DIRECTORY + "/log.txt"
#log_num = 0
#shutdown = False


# def log(message):
#     global log_num
#     with open(LOG_FILE, 'a') as f:
#         if type(message) == list:
#             message = '\n'.join(message)
#         f.write(str(log_num) + ' ' + str(message) + '\n')
#     log_num += 1

def handle_connection(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode()
        if message == "SHUTDOWN":
            conn.close()
            global shutdown
            shutdown = True
            return
        pyautogui.hotkey(message.split('+'))
        conn.sendall("OK".encode())


def main(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('127.0.0.1', port))
            s.listen()
            while not shutdown:
                conn, addr = s.accept()
                with conn:
                    handle_connection(conn, addr)
    except Exception as e:
        #log(f"Error: {e}")
        pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    main(int(sys.argv[1]))
