import math
import struct
import wave


class ChordUtil:

    """ This class provides utility functions to read, write, and play chords.

    All utility functions should be static methods. """

    @staticmethod
    def playChord(chord_id):
        scale = chord_id.getScale()

        # pow(2, 5/12) = obtain the equal ratio factor (i.e. 1.059246...) and then rise to 5 half steps above
        start_note = 220 * (pow(2, 5/12))

        # obtain the list of the actual frequencies
        temp = []
        for note in scale:
            note = start_note * (pow(2, note/12))
            temp.append(note)

        scale = temp

        ChordUtil.__writeChord(scale)

    @staticmethod
    def __writeChord(scale):
        duration = 3
        amplitude = 300

        sampwidth = 4 # bytes
        framerate = 44100
        nframes = sampwidth * framerate

        writer = wave.open("chord.wav", "wb")
        params = (1, sampwidth, framerate, nframes, "NONE", "NONE") # nchannels, sampwidth, framerate, nframes,
                                                                    # comptype, compname
        writer.setparams(params)

        for i in range(nframes):
            value = ChordUtil.__synChord(scale, i / framerate, amplitude)
            data = struct.pack("<h", int(value))
            writer.writeframesraw(data)

        writer.close()

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
