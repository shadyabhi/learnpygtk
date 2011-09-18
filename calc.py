#!/usr/bin/python2

import pygtk
pygtk.require('2.0')
import gtk


class Calculator:
    def __init__(self):
        #Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        
        self.window.set_title("Simply add the numbers")

        self.window.connect("destroy", lambda wid: gtk.main_quit())
        self.window.connect("delete_event", lambda a1,a2:gtk.main_quit())

        self.window.set_border_width(10)
        self.window.resize(200,200)
        self.window.show_all()


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    app = Calculator()
    main()
