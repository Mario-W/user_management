import sys
from user_views import app

if __name__ == '__main__':
    command = sys.argv
    if len(command) > 1:
        ip_port = command[1]
        ip_port_list = ip_port.split(':')
        if not len(ip_port_list) == 2:
            print('command is invalid. please enter ip:port ')
        else:
            app.run(ip_port_list[0], ip_port_list[1])
    else:
        app.run()
