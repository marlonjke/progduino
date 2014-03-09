#! /usr/bin/env python
#-*- encoding:utf-8 -*-
import gtk
import pygtk
pygtk.require('2.0')
import serial

port = '/dev/ttyACM0'
baud_rate = 9600

try:
    com = serial.Serial(port, baud_rate)
except:
    print 'Dispositivo não conectado'

class Progduino:
    def __init__(self):


        self.janela = gtk.Window()
        self.janela.set_title("The Wakemanduino - 0.1")
        self.janela.set_position(gtk.WIN_POS_CENTER)
        self.janela.set_border_width(15)
        self.janela.connect('destroy', lambda w: gtk.main_quit())
        self.conteudo = gtk.VBox(False, 1)

        #Box para Modificação/ Envio de acordes
        self.boxChord = gtk.HBox(False, 1)

        self.btnSend = gtk.Button("Send")
        self.btnSend.connect('clicked', self.on_send_chord_clicked)
        self.boxChord.pack_start(self.btnSend)

        self.chordChange = gtk.combo_box_entry_new_text()
        self.chordChange.append_text('')
        self.boxChord.pack_start(self.chordChange)

        self.chords = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        for chord in self.chords:
            self.chordChange.append_text(chord)

        self.chordChange.set_active(1)

        self.typeChordChange = gtk.combo_box_entry_new_text()
        self.typeChordChange.append_text('')
        self.boxChord.pack_start(self.typeChordChange)

        self.typeChords = ['Major', 'Minor', 'Diminuto']
        for typeChord in self.typeChords:
            self.typeChordChange.append_text(typeChord)

        self.typeChordChange.set_active(1)
        self.conteudo.pack_start(self.boxChord)

        #Box com outras configurações.
        self.confChord = gtk.HBox(False, 1)

        self.onoff = False
        self.btOnOff = gtk.Button('off')
        self.btOnOff.set_size_request(37, 25)
        self.btOnOff.connect('clicked', self.on_onoff_clicked)
        self.confChord.pack_start(self.btOnOff, False, False, 0)

        self.actualChord = gtk.Label()
        self.set_actual_chord()
        self.confChord.pack_start(self.actualChord, False, False, 0)

        self.conteudo.pack_start(self.confChord)
        self.janela.add(self.conteudo)
        self.janela.show_all()

    def set_actual_chord(self):
        data = str(self.chords[self.chordChange.get_active() - 1]) + ' ' + str(self.typeChords[self.typeChordChange.get_active() -1])
        self.actualChord.set_label('Actual Chord: ' + data)

    def on_send_chord_clicked(self, *args):
        data = str(self.chords[self.chordChange.get_active() - 1]) + ' ' + str(self.typeChords[self.typeChordChange.get_active() -1])
        print data
        self.set_actual_chord()
        self.send_data(data)


    def on_onoff_clicked(self, *args):
        self.onoff = not self.onoff

        self.send_data(self.onoff)

        if self.onoff:
            self.btOnOff.set_label('on')
        else:
            self.btOnOff.set_label('off')

    def send_data(self, data):
        # com.write(data)
        print data

if __name__ == '__main__':
    app = Progduino()
    gtk.main()
