#! /usr/bin/env python
#-*- encoding:utf-8 -*-


import gtk
import pygtk
pygtk.require('2.0')
import serial


class Progduino:
    def __init__(self):
        self.janela = gtk.Window()

        self.janela.set_title("ProgDuino - 0.1")
        self.janela.set_position(gtk.WIN_POS_CENTER)
        self.janela.set_border_width(15)
        self.janela.connect('destroy', lambda w: gtk.main_quit())
        self.conteudo = gtk.VBox(False, 1)

        #Box para Modificação/ Envio de acordes
        self.boxChord = gtk.HBox(False, 1)
        self.chordChange = gtk.combo_box_entry_new_text()
        self.chordChange.append_text('')
        self.boxChord.pack_start(self.chordChange)
        chords = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        for chord in chords:
            self.chordChange.append_text(chord)
        self.chordChange.set_active(1)

        self.typeChordChange = gtk.combo_box_entry_new_text()
        self.typeChordChange.append_text('')
        self.boxChord.pack_start(self.typeChordChange)
        typeChords = ['Major', 'Minor', 'Diminuto']
        for typeChord in typeChords:
            self.typeChordChange.append_text(typeChord)
        self.typeChordChange.set_active(1)

        self.btnSend = gtk.Button("Send Chord")
        self.btnSend.connect('clicked', self.on_send_chord_clicked)
        self.boxChord.pack_start(self.btnSend)
        self.conteudo.pack_start(self.boxChord)

        #Box com outras configurações.
        self.confChord = gtk.VBox(False, 1)

        self.button1 = gtk.RadioButton(None, "radio button1")
        # button1.connect("toggled", self.callback, "radio button 1")
        self.confChord.pack_start(self.button1, gtk.TRUE, gtk.TRUE, 0)
        self.button1.show()

        self.button2 = gtk.RadioButton(None, "radio button2")
        # button2.connect("toggled", self.callback, "radio button 2")
        self.button2.set_active(gtk.TRUE)
        self.confChord.pack_start(self.button2, gtk.TRUE, gtk.TRUE, 0)
        self.button2.show()

        self.conteudo.pack_start(self.confChord)

        self.janela.add(self.conteudo)
        self.janela.show_all()

    def on_send_chord_clicked(self, *args):
        print 'Teste Acorde', self.chordChange.get_active(), self.typeChordChange.get_active()

if __name__ == '__main__':
    app = Progduino()
    gtk.main()
