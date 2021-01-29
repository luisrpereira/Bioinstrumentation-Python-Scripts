#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.ioloop import IOLoop, PeriodicCallback
from tornado import gen
from tornado.websocket import websocket_connect
import json as js
import datetime
import numpy as np



file = open( 'output.txt', 'w+')


class Client(object):
    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.connect()
        PeriodicCallback(self.keep_alive, 20000, io_loop=self.ioloop).start()
        self.ioloop.start()


    @gen.coroutine
    def connect(self):
        print ("trying to connect")
        try:
            self.ws = yield websocket_connect(self.url)
        except Exception as e:
            print ("connection error")
        else:
            print ("connected")
            self.run()

    @gen.coroutine
    def run(self):
        while True:
            msg = yield self.ws.read_message()
            if msg is None:
                print ("connection closed")
                self.ws = None
                break
            else:
                global ts
                # print(str(msg))
                try:
                    msgDict = js.loads(msg)
                except:
                    print("Erro de json")
                else:

                    print(msgDict["A1"][:])

                    data_value = msgDict["A1"]
                    data = np.array(data_value)

                    data.tofile(file, sep='\n', format='%s')
                    file.write("\n")


    def keep_alive(self):
        if self.ws is None:
            self.connect()
        else:
            self.ws.write_message("keep alive")

if __name__ == "__main__":
    client = Client("ws://localhost:9001", 5)
