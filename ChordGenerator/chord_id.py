from enum import IntEnum


class ChordID(IntEnum):
    MAJOR_7TH = 1
    MINOR_7TH = 2
    DOMIN_7TH = 3
    DIMIN_7TH = 4
    MAJOR_TRI = 5
    MINOR_TRI = 6
    AUGME_TRI = 7
    DIMIN_TRI = 8

    def getScale(self):
        major7th = [0, 4, 7, 11]
        minor7th = [0, 3, 7, 10]
        domin7th = [0, 4, 7, 10]
        dimin7th = [0, 3, 6, 10]
        majorTri = [0, 4, 7]
        minorTri = [0, 3, 7]
        augmeTri = [0, 4, 8]
        diminTri = [0, 3, 6]

        if self.value == 1:
            return major7th
        elif self.value == 2:
            return minor7th
        elif self.value == 3:
            return domin7th
        elif self.value == 4:
            return dimin7th
        elif self.value == 5:
            return majorTri
        elif self.value == 6:
            return minorTri
        elif self.value == 7:
            return augmeTri
        elif self.value == 8:
            return diminTri
        else:
            return None

    @staticmethod
    def fromTextToChordId(text):

        """ returns the chord id correspodning to the chord name. """

        if text == "Major Seventh":
            return ChordID.MAJOR_7TH
        elif text == "Minor Seventh":
            return ChordID.MINOR_7TH
        elif text == "Dominant Seventh":
            return ChordID.DOMIN_7TH
        elif text == "Diminished Seventh":
            return ChordID.DIMIN_7TH
        elif text == "Major Triad":
            return ChordID.MAJOR_TRI
        elif text == "Minor Triad":
            return ChordID.MINOR_TRI
        elif text == "Augmented Triad":
            return ChordID.AUGME_TRI
        elif text == "Diminished Triad":
            return ChordID.DIMIN_TRI
        else:
            return None
