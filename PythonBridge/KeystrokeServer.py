import socket
import sys
import pyautogui
import os

# USER_HOME = os.path.expanduser('~')
# LOG_DIRECTORY = USER_HOME + "/Documents/Ableton/User Library/Remote Scripts"
# try:
#    os.makedirs(LOG_DIRECTORY, exist_ok=True)
# except TypeError:
#    try:
#        os.makedirs(LOG_DIRECTORY)
#    except OSError:
#        pass
# LOG_FILE = LOG_DIRECTORY + "/log.txt"
# log_num = 0
#
#
# def log(message):
#     global log_num
#     with open(LOG_FILE, 'a') as f:
#         if type(message) == list:
#             message = '\n'.join(message)
#         f.write(str(log_num) + ' ' + str(message) + '\n')
#     log_num += 1
#
shutdown = False

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
        elif message.startswith(";") and message.endswith(";"):
            #log("Complexe Command")
            stripped = message[1:-1]
            #log(stripped)
            commands = stripped.split(";")
            if commands[0] == "UPDATE_FILESYSTEM" and len(commands) == 2:
                try:
                    temp_path = os.path.join(commands[1],"temp.txt")
                    with open(temp_path, 'w') as f:
                        f.write("This is a temporary file. created to force 'Places' update")
                    os.remove(temp_path)
                except Exception as e:
             #       log(f"Error: {e}")
                    pass
                conn.sendall("OK".encode())
                return
            else:
                #log("Invalid Command")
                conn.sendall("ERROR".encode())
                return
        else:
            #log(message)
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
        print(f"Error: {e}")
        pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    main(int(sys.argv[1]))
