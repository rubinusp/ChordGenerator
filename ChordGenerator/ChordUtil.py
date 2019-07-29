import math
import struct
import wave


class ChordUtil:

    """ This class provides utility functions to read, write, and play chords.

    All utility functions should be static methods. """

    @staticmethod
    def exportChord(chord_id):
        # pow(2, 5/12) = obtain the equal ratio factor (i.e. 1.059246...) and then rise to 5 half steps above
        rootNote = 220 * (pow(2, 5/12))

        duration = 3
        amplitude = 50
        sampwidth = 4  # bytes
        framerate = 44100
        nframes = duration * framerate

        list = ChordUtil.genFreqList(rootNote, chord_id, amplitude, duration, framerate)

        writer = wave.open("chord.wav", "wb")
        params = (1, sampwidth, framerate, nframes, "NONE", "NONE")  # nchannels, sampwidth, framerate, nframes,
        # comptype, compname
        writer.setparams(params)
        for i in list:
            data = struct.pack("<h", int(i))
            writer.writeframesraw(data)

        writer.close()

    @staticmethod
    def genFreqList(rootNote, chord_id, amplitude, duration, framerate):
        """ generates the list of frequencies representing the sound of the chord """

        # obtain the scale given the root note and the type of chord
        scale = ChordUtil.__genScale(rootNote, chord_id)

        list = []
        for i in range(duration * framerate):
            value = ChordUtil.__synChord(scale, i / framerate, amplitude)
            list.append(value)
        return list

    @staticmethod
    def __genScale(rootNote, chord_id):
        """ generates the list of frequencies of each pitch in the given chord type """

        scale = chord_id.getScale()

        temp = []
        for note in scale:
            note = rootNote * (pow(2, note / 12))
            temp.append(note)

        return temp

    @staticmethod
    def __synChord(scale, t, A):
        value = 0
        for i in range(len(scale)):
            value += A * math.sin(2 * math.pi * scale[i] * t)
        return value

    @staticmethod
    def readWav():
        reader = wave.open("chord.wav", "rb")

        nframes = reader.getnframes()
        list = []
        for i in range(2000):
            value = reader.readframes(1)
            data = struct.unpack("<i", value)[0]
            list.append(data)

        reader.close()
        print(list)
        return list

    @staticmethod
    def fromIntToSPN(i):

        """ returns the corresponding scientific pitch notation (SPN) given the pitch index
        """

        # TODO: throws exception if i is out of range
        return {
            0:  "A0",
            1:  "B0",
            2:  "C1",
            3:  "D1",
            4:  "E1",
            5:  "F1",
            6:  "G1",
            7:  "A1",
            8:  "B1",
            9:  "C2",
            10: "D2",
            11: "E2",
            12: "F2",
            13: "G2",
            14: "A2",
            15: "B2",
            16: "C3",
            17: "D3",
            18: "E3",
            19: "F3",
            20: "G3",
            21: "A3",
            22: "B3",
            23: "C4",
            24: "D4",
            25: "E4",
            26: "F4",
            27: "G4",
            28: "A4",
            29: "B4",
            30: "C5",
            31: "D5",
            32: "E5",
            33: "F5",
            34: "G5",
            35: "A5",
            36: "B5",
            37: "C6",
            38: "D6",
            39: "E6",
            40: "F6",
            41: "G6",
            42: "A6",
            43: "B6",
            44: "C7",
            45: "D7",
            46: "E7",
            47: "F7",
            48: "G7",
            49: "A7",
            50: "B7",
            51: "C8",
        }[i]