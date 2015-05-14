#!/usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gtk,Gdk,GdkPixbuf
import os 

class BookplatesWindow:

    def WindowDeleteEvent(self, widget, event):
        # return false so that window will be destroyed
        return False

    def WindowDestroy(self, wideget, *data):
        # exit main loop
        Gtk.main_quit()

    def __init__(self):
        self.paint_first_screen()

    def paint_first_screen(self):
        # Create top level window
        window = Gtk.Window()
        window.set_title("Bookplates")
        window.set_default_size(300,200)
        window.connect("delete-event", self.WindowDeleteEvent)
        window.connect("destroy", self.WindowDestroy)

        # Create layout container 
        layout = Gtk.Layout()
        layout.set_size(300, 200)
        window.add(layout)

        # Create end button
        b_end = Gtk.Button("End")
        b_end.connect("clicked", self.end_clicked)
        layout.put(b_end, 0, 0)

        # Create image for head1
        o_head1 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/head1.gif", 100, 80)
        i_head1 = Gtk.Image().new_from_pixbuf(o_head1)
        b_head1 = Gtk.Button()
        b_head1.set_image(i_head1)
        b_head1.connect("clicked", self.head1_clicked)
        layout.put(b_head1, 0, 50)

        # Create image for head2
        o_head2 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/head2.gif", 100, 80)
        i_head2 = Gtk.Image().new_from_pixbuf(o_head2)
        b_head2 = Gtk.Button()
        b_head2.set_image(i_head2)
        b_head2.connect("clicked", self.head2_clicked)
        layout.put(b_head2, 105, 50)

        # Create image for head3
        o_head3 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/head3.gif", 100, 80)
        i_head3 = Gtk.Image().new_from_pixbuf(o_head3)
        b_head3 = Gtk.Button()
        b_head3.set_image(i_head3)
        b_head3.connect("clicked", self.head3_clicked)
        layout.put(b_head3, 210, 50)

        # Create back button
        b_back = Gtk.Button("Back")
        b_back.connect("clicked", self.back_clicked)
        layout.put(b_back, 0, 150)

        # Create next button
        b_next = Gtk.Button("Next")
        b_next.connect("clicked", self.next_clicked)
        layout.put(b_next, 250, 150)

        window.show_all()

    def end_clicked(self, button):
        print "exiting"

    def back_clicked(self, button):
        print "exiting"

    def next_clicked(self, button):
        print "exiting"

    def head1_clicked(self, button):
        print "Hello, World 1!"
        os.system("lpr -o page-left=20 -o page-right=20 -o media='4x6' -P piprinter /home/pi/bookplates/robots/head1.gif")

    def head2_clicked(self, button):
        print "Hello, World 2!"
        os.system("lpr -o page-left=20 -o page-right=20 -o media='4x6' -P piprinter /home/pi/bookplates/robots/head2.gif")

    def head3_clicked(self, button):
        print "Hello, World 3!"
        os.system("lpr -o page-left=20 -o page-right=20 -o media='4x6' -P piprinter /home/pi/bookplates/robots/head3.gif")

def main():
    # enter the main loop
    Gtk.main()
    return 0

if __name__ == "__main__":
    BookplatesWindow()
    main()
