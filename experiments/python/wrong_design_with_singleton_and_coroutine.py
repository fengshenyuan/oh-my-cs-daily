# -*- coding:utf8 -*-

# WRONG DESIGN NOTE
# --------------------------------------------------------------------
# Guo Yuan 2018/01/06
# --------------------------------------------------------------------
# kupper_url = "http://localhost:8888/kupper"
# mophy_url = "http://localhost:8888/mophy"
#
# after start the application
# access kupper_url, wait 2 seconds, then access mophy_url
# you'll see that mophy request handler change kupper request
# handler's db_session without notification, and kupper request
# handler closed mophy request handler's db_session!
# it's totally a wrong design trying to manage coroutine's individual
# resource with a singleton db controller.
# since every coroutine need individual db session, the best way is
# keep this resource only in the control of current coroutine, which means
# every coroutine needs a db controller instance, instead of a singletion
# db controller for whole application.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import gen
import time
import logging

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class DBController(object):

    def __init__(self, x=0):
        self.db_session = None


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Mophy~")
        return


class KupperHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        # init db controller
        db_ctl = DBController()
        logging.info("before kupper use :" + str(db_ctl.db_session))

        kupper_session = "kupper_session"
        db_ctl.db_session = kupper_session
        logging.info("after kupper init :" + str(db_ctl.db_session))

        logging.info("kupper is using session:" + str(db_ctl.db_session))
        yield gen.sleep(5.0)

        logging.info("kupper end use session:" + str(db_ctl.db_session))

        # close db controller
        db_ctl.db_session = None
        logging.info("after kupper close :" + str(db_ctl.db_session))


class MoPhyHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        # init db controller
        db_ctl = DBController()
        logging.info("before mophy use :" + str(db_ctl.db_session))

        mophy_session = "mophy_session"
        db_ctl.db_session = mophy_session
        logging.info("after mophy init :" + str(db_ctl.db_session))

        logging.info("mophy is using session:" + str(db_ctl.db_session))
        yield gen.sleep(5.0)

        logging.info("mophy is using again db_ctl: " + str(db_ctl.db_session))
        logging.info("mophy end use db_ctl: " + str(db_ctl.db_session))

        # close db controller
        db_ctl.db_session = None
        logging.info("after mophy close :" + str(db_ctl.db_session))


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/kupper", KupperHandler),
        (r"/mophy", MoPhyHandler),

    ])

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    logging.info(application.settings)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
