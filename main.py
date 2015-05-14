#!/usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gtk,Gdk,GdkPixbuf
import os 

class BookplatesWindow:

    head = 1
    body = 1
    legs = 1

    def WindowDeleteEvent(self, widget, event):
        # return false so that window will be destroyed
        return False

    def WindowDestroy(self, wideget, *data):
        # exit main loop
        Gtk.main_quit()

    def __init__(self):
        # Create top level window
        window = Gtk.Window()
        window.set_title("Bookplates")
        window.set_default_size(300,200)
        window.connect("delete-event", self.WindowDeleteEvent)
        window.connect("destroy", self.WindowDestroy)

        # paint first screen
        self.paint_head_screen()
        window.show_all()

    def paint_head_screen(self):
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

        # Create next button
        b_head_next = Gtk.Button("Next")
        b_head_next.connect("clicked", self.next_head_clicked)
        layout.put(b_head_next, 250, 150)

    def paint_body_screen(self):
        # Create layout container
        layout = Gtk.Layout()
        layout.set_size(300, 200)
        window.add(layout)

        # Create end button
        b_end = Gtk.Button("End")
        b_end.connect("clicked", self.end_clicked)
        layout.put(b_end, 0, 0)

        # Create image for head1
        o_body1 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/body1.gif", 100, 80)
        i_body1 = Gtk.Image().new_from_pixbuf(o_body1)
        b_body1 = Gtk.Button()
        b_body1.set_image(i_body1)
        b_body1.connect("clicked", self.body1_clicked)
        layout.put(b_body1, 0, 50)

        # Create image for head2
        o_body2 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/body2.gif", 100, 80)
        i_body2 = Gtk.Image().new_from_pixbuf(o_body2)
        b_body2 = Gtk.Button()
        b_body2.set_image(i_body2)
        b_body2.connect("clicked", self.body2_clicked)
        layout.put(b_body2, 105, 50)

        # Create image for head3
        o_body3 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/body3.gif", 100, 80)
        i_body3 = Gtk.Image().new_from_pixbuf(o_body3)
        b_body3 = Gtk.Button()
        b_body3.set_image(i_body3)
        b_body3.connect("clicked", self.body3_clicked)
        layout.put(b_body3, 210, 50)

        # Create back button
        b_back = Gtk.Button("Back")
        b_back.connect("clicked", self.back_body_clicked)
        layout.put(b_back, 0, 150)

        # Create next button
        b_next = Gtk.Button("Next")
        b_next.connect("clicked", self.next_body_clicked)
        layout.put(b_next, 250, 150)

    def paint_legs_screen(self):
        # Create layout container
        layout = Gtk.Layout()
        layout.set_size(300, 200)
        window.add(layout)

        # Create end button
        b_end = Gtk.Button("End")
        b_end.connect("clicked", self.end_clicked)
        layout.put(b_end, 0, 0)

        # Create image for legs1
        o_legs1 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/legs1.gif", 100, 80)
        i_legs1 = Gtk.Image().new_from_pixbuf(o_legs1)
        b_legs1 = Gtk.Button()
        b_legs1.set_image(i_legs1)
        b_legs1.connect("clicked", self.legs1_clicked)
        layout.put(b_legs1, 0, 50)

        # Create image for legs2
        o_legs2 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/legs2.gif", 100, 80)
        i_legs2 = Gtk.Image().new_from_pixbuf(o_legs2)
        b_legs2 = Gtk.Button()
        b_legs2.set_image(i_legs2)
        b_legs2.connect("clicked", self.legs2_clicked)
        layout.put(b_legs2, 105, 50)

        # Create image for legs3
        o_legs3 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/legs3.gif", 100, 80)
        i_legs3 = Gtk.Image().new_from_pixbuf(o_legs3)
        b_legs3 = Gtk.Button()
        b_legs3.set_image(i_legs3)
        b_legs3.connect("clicked", self.legs3_clicked)
        layout.put(b_legs3, 210, 50)

        # Create back button
        b_back = Gtk.Button("Back")
        b_back.connect("clicked", self.back_legs_clicked)
        layout.put(b_back, 0, 150)

        # Create print button
        b_print = Gtk.Button("Print")
        b_print.connect("clicked", self.print_robot_clicked)
        layout.put(b_print, 250, 150)

    # end button on all screens will exit
    def end_clicked(self, button):
        print "exiting"

    # back button on body and legs screens only
    def back_body_clicked(self, button):
        self.paint_head_screen()

    def back_legs_clicked(self, button):
        self.paint_body_screen()

    # next button on head and body screens only
    def next_head_clicked(self, button):
        self.paint_body_screen()

    def next_body_clicked(self, button):
        self.paint_legs_screen()

    # print button on legs screen
    def print_robot_clicked(self, button):
        os.system("convert -pointsize 20 -size 200x400 xc:white /home/pi/robots/head" + self.head + ".gif -geometry +0+10 -composite /home/pi/robots/body" + self.body + ".gif -geometry +0+110 -composite /home/pi/robots/legs" + self.legs + ".gif -geometry +0+205 -composite label:'Monica & Stephanie' -append /home/pi/temp-final-robot.gif")
        os.system("lpr -o page-left=20 -o page-right=20 -o media='4x6' -P piprinter /home/pi/temp-final-robot.gif")
        os.system("rm /home/pi/temp-final-robot.gif")

    def head1_clicked(self, button):
        head = 1

    def head2_clicked(self, button):
        head = 2

    def head3_clicked(self, button):
        head = 3

    def body1_clicked(self, button):
        body = 1

    def body2_clicked(self, button):
        body = 2

    def body3_clicked(self, button):
        body = 3

    def legs1_clicked(self, button):
        legs = 1

    def legs2_clicked(self, button):
        legs = 2

    def legs3_clicked(self, button):
        legs = 3

def main():
    # enter the main loop
    Gtk.main()
    return 0

if __name__ == "__main__":
    BookplatesWindow()
    main()
