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

        freqs = ChordUtil.genSynthesizedChordFreqs(rootNote, chord_id, amplitude, duration, framerate)

        writer = wave.open("chord.wav", "wb")
        params = (1, sampwidth, framerate, nframes, "NONE", "NONE")  # nchannels, sampwidth, framerate, nframes,
        # comptype, compname
        writer.setparams(params)
        for freq in freqs:
            data = struct.pack("<h", freq)
            writer.writeframesraw(data)

        writer.close()

    @staticmethod
    def genSynthesizedChordFreqs(rootFreq, chord_id, amplitude, duration, framerate):

        """ generates the list of synthesized frequencies corresponding to the chord.

        Frequencies are rounded to the nearest integer. Any root note should be converted to root frequency by
        fromIntToFreq(i) before being passed as argument. """

        # obtain the scale given the root note and the type of chord
        scaleFreqs = ChordUtil.__genScaleFreqs(rootFreq, chord_id)

        list = []
        for i in range(duration * framerate):
            value = int(ChordUtil.__synScaleFreqs(scaleFreqs, i / framerate, amplitude))
            list.append(value)
        return list

    @staticmethod
    def genSingleNoteFreq(rootFreq, chord_id, duration, framerate, amplitude):

        """ generates the list of some lists, where each list element contains the name of the note in relation to the
        chord or single note frequencies corresponding to each note of the chord.

        Frequencies are rounded to the nearest integer. Any root note should be converted to root frequency by
        fromIntToFreq(i) before being passed as argument. """

        # obtain the scale given the root note and the type of chord
        scaleFreqs = ChordUtil.__genScaleFreqs(rootFreq, chord_id)

        list = []
        i = 0
        for freq in scaleFreqs:
            name = ChordUtil.fromIntToNoteName(chord_id.getScale()[i])
            list.append(name)
            i += 1

            temp = []
            for j in range(duration * framerate):
                value = int(ChordUtil.__computeNoteFreq(freq, j / framerate, amplitude))
                temp.append(value)
                print(value)
            list.append(temp)

        return list

    @staticmethod
    def __genScaleFreqs(rootFreq, chord_id):

        """ generates the list of frequencies of each note in the given chord type.
        """

        scale = chord_id.getScale()

        list = []
        for note in scale:
            note = rootFreq * (pow(2, note / 12))
            list.append(note)

        return list

    @staticmethod
    def __synScaleFreqs(scaleFreqs, t, A):

        value = 0
        for i in range(len(scaleFreqs)):
            value += ChordUtil.__computeNoteFreq(scaleFreqs[i], t, A)
        return value

    @staticmethod
    def __computeNoteFreq(freq, t, A):
        return A * math.sin(2 * math.pi * freq * t)

    @staticmethod
    def readWav():
        reader = wave.open("chord.wav", "rb")

        nframes = reader.getnframes()
        list = []
        for i in range(nframes):
            value = reader.readframes(1)
            data = struct.unpack("<i", value)[0]
            list.append(data)

        reader.close()
        print(list)
        return list

    @staticmethod
    def fromIntToSPN(i):

        """ returns the corresponding scientific pitch notation (SPN) given the pitch index.
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

    @staticmethod
    def fromIntToFreq(i):

        """ returns the corresponding frequency given the pitch index.
        """

        # TODO: throws exception if i is out of range
        return {
            0: 28,
            1: 31,
            2: 33,
            3: 37,
            4: 41,
            5: 44,
            6: 49,
            7: 55,
            8: 62,
            9: 65,
            10: 73,
            11: 82,
            12: 87,
            13: 98,
            14: 110,
            15: 124,
            16: 131,
            17: 147,
            18: 165,
            19: 175,
            20: 196,
            21: 220,
            22: 247,
            23: 262,
            24: 294,
            25: 330,
            26: 349,
            27: 392,
            28: 440,
            29: 494,
            30: 523,
            31: 587,
            32: 659,
            33: 699,
            34: 784,
            35: 880,
            36: 988,
            37: 1047,
            38: 1175,
            39: 1319,
            40: 1397,
            41: 1568,
            42: 1760,
            43: 1976,
            44: 2093,
            45: 2349,
            46: 2637,
            47: 2794,
            48: 3136,
            49: 3520,
            50: 3951,
            51: 4186,
        }[i]

    @staticmethod
    def fromIntToNoteName(i):

        """ returns the name of the note given the index of note in the scale defined in Chord_id.py
        """

        return {
            0: "Root note",
            3: "Third note",
            4: "Third note",
            6: "Fifth note",
            7: "Fifth note",
            8: "Fifth note",
            10: "Seventh note",
            11: "Seventh note",
        }[i]

