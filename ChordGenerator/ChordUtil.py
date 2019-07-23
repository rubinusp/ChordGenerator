from chord_id import ChordID
import math
import struct
import random
import wave

class ChordUtil:
    def playChord(self, chord_id):
        major7th = [0, 4, 7, 11]
        minor7th = [0, 3, 7, 10]
        domin7th = [0, 4, 7, 10]
        dimin7th = [0, 3, 6, 10]
        majorTri = [0, 4, 7]
        minorTri = [0, 3, 7]
        augmeTri = [0, 4, 8]
        diminTri = [0, 3, 6]

        if chord_id == ChordID.MAJOR_7TH:
            scale = major7th
        elif chord_id == ChordID.MINOR_7TH:
            scale = scale = minor7th
        elif chord_id == ChordID.DOMIN_7TH:
            scale = domin7th
        elif chord_id == ChordID.DIMIN_7TH:
            scale = dimin7th
        elif chord_id == ChordID.MAJOR_TRI:
            scale = majorTri
        elif chord_id == ChordID.MINOR_TRI:
            scale = minorTri
        elif chord_id == ChordID.AUGME_TRI:
            scale = augmeTri
        else:
            scale = diminTri

        # pow(2, 5/12) = obtain the equal ratio factor (i.e. 1.059246...) and then rise to 5 half steps above
        start_note = 220 * (pow(2, 5/12))

        temp = []
        for note in scale:
            note = start_note * (pow(2, note/12))
            temp.append(note)

        scale = temp

        self.writeChord(scale)

    def writeChord(self, scale):
        duration = 3
        volume = 300

        sampwidth = 4 # bytes
        framerate = 44100
        nframes = sampwidth * framerate

        writer = wave.open("chord.wav", "wb")
        params = (1, sampwidth, framerate, nframes, "NONE", "NONE")
            # nchannels, sampwidth, framerate, nframes, comptype, compname
        writer.setparams(params)

        for i in range(nframes):
            value = self.synChord(scale, i / framerate, volume)
            print(value)
            data = struct.pack("<h", int(value))
            writer.writeframesraw(data)

        writer.close()

    def synChord(self, scale, t, v):
        value = 0
        for i in range(len(scale)):
            value += v * math.sin(2 * math.pi * scale[i] * t)
        return value
