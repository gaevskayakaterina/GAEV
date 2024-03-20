#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('', 9090))
message = 'hello, world!'
sock.send(message.encode('utf-8'))

data = sock.recv(1024)
sock.close()

print(data)