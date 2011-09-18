#!/usr/bin/python2

import pygtk
pygtk.require('2.0')
import gtk


class Calculator:
    def __init__(self):
        
        #Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Simply add the numbers")
        self.window.set_border_width(10)
        self.window.resize(300,100)
        
        vbox = gtk.VBox(True, 10)
        self.window.add(vbox)

        #Creating the two text labels
        self.entry_num1 = gtk.Entry()
        self.entry_num2 = gtk.Entry()

        self.entry_num1.set_max_length(50)
        self.entry_num2.set_max_length(50)

        vbox.pack_start(self.entry_num1, True, True, 0)
        vbox.pack_start(self.entry_num2, True, True, 0)

        #Creating the result label
        self.label_result = gtk.Label("Result is: ")
        self.label_result.set_justify(gtk.JUSTIFY_LEFT)
        vbox.pack_start(self.label_result, False, False, 0)


        #Creating the calculate and exit button
        hbox_buttons = gtk.HBox(True, 10)
        button_calculate = gtk.Button("Calculate")
        button_quit = gtk.Button("Quit")

        button_quit.connect("clicked", lambda wid: gtk.main_quit())
        button_calculate.connect("clicked", self.add_numbers)

        hbox_buttons.pack_start(button_calculate, True, True, 0)
        hbox_buttons.pack_start(button_quit, True, True, 0)
        vbox.pack_start(hbox_buttons, True, True, 0)
        
        self.window.connect("destroy", lambda wid: gtk.main_quit())
        self.window.connect("delete_event", lambda a1,a2:gtk.main_quit())

        self.window.show_all()
    
    def add_numbers(self, data=None):
        try:
            num1 = int(self.entry_num1.get_text())
            num2 = int(self.entry_num2.get_text())
        except ValueError:
            self.label_result.set_text("Non integer values. Pls correct.")
        self.label_result.set_text("Result is: "+str(num1+num2))

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    app = Calculator()
    main()
