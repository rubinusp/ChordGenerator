from chord_id import ChordID
import wave

class ChordUtil:
    def playChord(self, chord_id):
        major7th = {0, 4, 7, 11}
        minor7th = {0, 3, 7, 10}
        domin7th = {0, 4, 7, 10}
        dimin7th = {0, 3, 6, 10}
        majorTri = {0, 4, 7}
        minorTri = {0, 3, 7}
        augmeTri = {0, 4, 8}
        diminTri = {0, 3, 6}

        if chord_id == ChordID.MAJOR_7TH:
            scale = major7th
        elif chord_id == ChordID.MINOR_7TH:
            scale = minor7th
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
        start_note = 220*(pow(2, 5/12))

        for note in scale:
            note = start_note * (pow(2, note/12))

    def writeChord(self, chord_id):
        writer = wave.open("chord.wav", "wb")
