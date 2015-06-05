#!/usr/bin/python
# -*- coding: utf-8 -*-
# Trellis keyboard programming courtesy Tony DiCola - Adafruit blog

from gi.repository import Gtk,Gdk,GdkPixbuf
import os, sys, time 

class HeadScreen(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Choose head")
        self.maximize()
        self.paint_head_screen()

    def paint_head_screen(self):
        grid = Gtk.Grid()
        self.add(grid)

        # Create end button
        b_end = Gtk.Button("End")
        b_end.connect("clicked", self.end_clicked)

        # Create image for head1
        o_head1 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/head1.gif", 100, 80)
        i_head1 = Gtk.Image().new_from_pixbuf(o_head1)
        b_head1 = Gtk.Button()
        b_head1.set_image(i_head1)
        b_head1.connect("clicked", self.head_clicked, 1)

        # Create image for head2
        o_head2 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/head2.gif", 100, 80)
        i_head2 = Gtk.Image().new_from_pixbuf(o_head2)
        b_head2 = Gtk.Button()
        b_head2.set_image(i_head2)
        b_head2.connect("clicked", self.head_clicked, 2)

        # Create image for head3
        o_head3 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/head3.gif", 100, 80)
        i_head3 = Gtk.Image().new_from_pixbuf(o_head3)
        b_head3 = Gtk.Button()
        b_head3.set_image(i_head3)
        b_head3.connect("clicked", self.head_clicked, 3)

        grid.add(b_end)
        grid.attach_next_to(b_head1, b_end, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(b_head2, b_head1, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(b_head3, b_head2, Gtk.PositionType.RIGHT, 2, 1)

    def head_clicked(self, button, head):
        s_body = BodyScreen(head)
        s_body.show_all()
        self.destroy()

    def end_clicked(self, button):
        self.destroy()
        Gtk.main_quit()
        # Configure to run in a loop - create the head screen again
        s_head = HeadScreen()
        s_head.show_all()
        Gtk.main()

class BodyScreen(Gtk.Window):

    def __init__(self, head):
        Gtk.Window.__init__(self, title="Choose body")
        self.maximize()
        self.paint_body_screen(head)

    def paint_body_screen(self, head):
        grid = Gtk.Grid()
        self.add(grid)

        # Create end button
        b_end = Gtk.Button("End")
        b_end.connect("clicked", self.end_clicked)

        # Create image for head1
        o_body1 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/body1.gif", 100, 80)
        i_body1 = Gtk.Image().new_from_pixbuf(o_body1)
        b_body1 = Gtk.Button()
        b_body1.set_image(i_body1)
        b_body1.connect("clicked", self.body_clicked, head, 1)

        # Create image for head2
        o_body2 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/body2.gif", 100, 80)
        i_body2 = Gtk.Image().new_from_pixbuf(o_body2)
        b_body2 = Gtk.Button()
        b_body2.set_image(i_body2)
        b_body2.connect("clicked", self.body_clicked, head, 2)

        # Create image for head3
        o_body3 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/body3.gif", 100, 80)
        i_body3 = Gtk.Image().new_from_pixbuf(o_body3)
        b_body3 = Gtk.Button()
        b_body3.set_image(i_body3)
        b_body3.connect("clicked", self.body_clicked, head, 3)

        grid.add(b_end)
        grid.attach_next_to(b_body1, b_end, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(b_body2, b_body1, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(b_body3, b_body2, Gtk.PositionType.RIGHT, 2, 1)

    def body_clicked(self, button, head, body):
        s_legs = LegsScreen(head, body)
        s_legs.show_all()
        self.destroy()

    def end_clicked(self, button):
        self.destroy()
        Gtk.main_quit()
        # Configure to run in a loop - create the head screen again
        s_head = HeadScreen()
        s_head.show_all()
        Gtk.main()

class LegsScreen(Gtk.Window):

    def __init__(self, head, body):
        Gtk.Window.__init__(self, title="Choose legs")
        self.maximize()
        self.paint_legs_screen(head, body)

    def paint_legs_screen(self, head, body):
        grid = Gtk.Grid()
        self.add(grid)

        # Create end button
        b_end = Gtk.Button("End")
        b_end.connect("clicked", self.end_clicked)

        # Create image for legs1
        o_legs1 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/legs1.gif", 100, 80)
        i_legs1 = Gtk.Image().new_from_pixbuf(o_legs1)
        b_legs1 = Gtk.Button()
        b_legs1.set_image(i_legs1)
        b_legs1.connect("clicked", self.legs_clicked, head, body, 1)

        # Create image for legs2
        o_legs2 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/legs2.gif", 100, 80)
        i_legs2 = Gtk.Image().new_from_pixbuf(o_legs2)
        b_legs2 = Gtk.Button()
        b_legs2.set_image(i_legs2)
        b_legs2.connect("clicked", self.legs_clicked, head, body, 2)

        # Create image for legs3
        o_legs3 = GdkPixbuf.Pixbuf().new_from_file_at_size("robots/legs3.gif", 100, 80)
        i_legs3 = Gtk.Image().new_from_pixbuf(o_legs3)
        b_legs3 = Gtk.Button()
        b_legs3.set_image(i_legs3)
        b_legs3.connect("clicked", self.legs_clicked, head, body, 3)

        grid.add(b_end)
        grid.attach_next_to(b_legs1, b_end, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(b_legs2, b_legs1, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(b_legs3, b_legs2, Gtk.PositionType.RIGHT, 2, 1)

    def legs_clicked(self, button, head, body, legs):
        s_name = NameScreen(head, body, legs)
        s_name.show_all()
        self.destroy()

    def end_clicked(self, button):
        self.destroy()
        Gtk.main_quit()
        # Configure to run in a loop - create the head screen again
        s_head = HeadScreen()
        s_head.show_all()
        Gtk.main()


class NameScreen(Gtk.Window):
    def __init__(self, head, body, legs):
        Gtk.Window.__init__(self, title="Type name")
        self.maximize()
        self.paint_name_screen(head, body, legs)

    def paint_name_screen(self, head, body, legs):
        grid = Gtk.Grid()
        grid.set_row_spacing(20)
        self.add(grid)

        # Create end button
        b_end = Gtk.Button("End")
        b_end.connect("clicked", self.end_clicked)

        # get name from keyboard
        t_entry = Gtk.Entry()

        b_print = Gtk.Button("Print")
        b_print.connect("clicked", self.print_clicked, head, body, legs, t_entry)

        grid.add(b_end)
        grid.attach_next_to(t_entry, b_end, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(b_print, t_entry, Gtk.PositionType.BOTTOM, 1, 2)        
        t_entry.grab_focus()

    def print_clicked(self, button, head, body, legs, t_entry):
        name = t_entry.get_text()

        os.system("convert -pointsize 20 -size 200x400 xc:white /home/pi/robots/head" + str(head) + ".gif -geometry +0+10 -composite /home/pi/robots/body" + str(body) + ".gif -geometry +0+110 -composite /home/pi/robots/legs" + str(legs) + ".gif -geometry +0+205 -composite caption:'        " + name + "' -append /home/pi/temp-robot.gif")
        time.sleep(1)
        #os.system("convert -size 250x500 xc:white /home/pi/robots/rexlibris.gif -geometry +10+10 -composite /home/pi/temp-robot.gif -geometry +0+50 -composite -append /home/pi/temp-final-robot.gif")
        #time.sleep(5)
        os.system("lpr -o page-left=20 -o media='10x20' -P piprinter /home/pi/temp-robot.gif")

        time.sleep(3)
        Gtk.main_quit()
        time.sleep(4)
        self.destroy()

        # Configure to run in a loop - create the head screen again
        s_head = HeadScreen()
        s_head.show_all()
        Gtk.main()

    def end_clicked(self, button):
        self.destroy()
        Gtk.main_quit()
        # Configure to run in a loop - create the head screen again
        s_head = HeadScreen()
        s_head.show_all()
        Gtk.main()

import Adafruit_Trellis
class TrellisKeyboard:
    def __init__(self):
        self.matrix0 = Adafruit_Trellis.Adafruit_Trellis()
        self.matrix1 = Adafruit_Trellis.Adafruit_Trellis()
        self.trellis = Adafruit_Trellis.Adafruit_TrellisSet(matrix0, matrix1)
        self.trellis.begin((0x70,  I2C_BUS), (0x71, I2C_BUS))
    
    def readChar(self):
        charPressed = 99
        # If a button was just pressed or released...
        if trellis.readSwitches():
            # go through every button
            for i in range(numKeys):
                # if it was pressed, turn it on
                if trellis.justPressed(i):
                    charPressed = i
                    trellis.setLED(i)
                # if it was released, turn it off
                    trellis.clrLED(i)
            # tell the trellis to set the LEDs we requested
            trellis.writeDisplay()
        return charPressed

if __name__ == "__main__":
    s_head = HeadScreen()
    s_head.show_all()
    Gtk.main()
