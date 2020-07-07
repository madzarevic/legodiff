import re
import sys
from enum import Enum, unique

@unique
class Color(Enum):
    def __lt__(self, other): return self.value < other.value 
    
    White = 1
    VeryLightGray = 49
    VeryLightBluishGray = 99
    LightBluishGray = 86
    LightGray = 9
    DarkGray = 10
    DarkBluishGray = 85
    Black = 11
    DarkRed = 59
    Red = 5
    Rust = 27
    Salmon = 25
    LightSalmon = 26
    SandRed = 58
    ReddishBrown = 88
    Brown = 8
    DarkBrown = 120
    DarkTan = 69
    Tan = 2
    LightFlesh = 90
    Flesh = 28
    MediumDarkFlesh = 150
    DarkFlesh = 91
    FabulandBrown = 106
    FabulandOrange = 160
    EarthOrange = 29
    DarkOrange = 68
    Orange = 4
    MediumOrange = 31
    BrightLightOrange = 110
    LightOrange = 32
    VeryLightOrange = 96
    DarkYellow = 161
    Yellow = 3
    BrightLightYellow = 103
    LightYellow = 33
    LightLime = 35
    YellowishGreen = 158
    MediumLime = 76
    Lime = 34
    OliveGreen = 155
    DarkGreen = 80
    Green = 6
    BrightGreen = 36
    MediumGreen = 37
    LightGreen = 38
    SandGreen = 48
    DarkTurquoise = 39
    LightTurquoise = 40
    Aqua = 41
    LightAqua = 152
    DarkBlue = 63
    Blue = 7
    DarkAzure = 153
    MediumAzure = 156
    MediumBlue = 42
    MaerskBlue = 72
    BrightLightBlue = 105
    LightBlue = 62
    SkyBlue = 87
    SandBlue = 55
    BlueViolet = 97
    DarkBlueViolet = 109
    Violet = 43
    MediumViolet = 73
    LightViolet = 44
    DarkPurple = 89
    Purple = 24
    LightPurple = 93
    MediumLavender = 157
    Lavender = 154
    SandPurple = 54
    Magenta = 71
    DarkPink = 47
    MediumDarkPink = 94
    BrightPink = 104
    Pink = 23
    LightPink = 56
    TransClear = 12
    TransBlack = 13
    TransRed = 17
    TransNeonOrange = 18
    TransOrange = 98
    TransLightOrange = 164
    TransNeonYellow = 121
    TransYellow = 19
    TransNeonGreen = 16
    TransBrightGreen = 108
    TransGreen = 20
    TransDarkBlue = 14
    TransMediumBlue = 74
    TransLightBlue = 15
    TransVeryLtBlue = 113
    TransLightPurple = 114
    TransPurple = 51
    TransDarkPink = 50
    TransPink = 107
    ChromeGold = 21
    ChromeSilver = 22
    ChromeAntiqueBrass = 57
    ChromeBlack = 122
    ChromeBlue = 52
    ChromeGreen = 64
    ChromePink = 82
    PearlWhite = 83
    PearlVeryLightGray = 119
    PearlLightGray = 66
    FlatSilver = 95
    PearlDarkGray = 77
    MetalBlue = 78
    PearlLightGold = 61
    PearlGold = 115
    FlatDarkGold = 81
    Copper = 84
    MetallicSilver = 67
    MetallicGreen = 70
    MetallicGold = 65
    MilkyWhite = 60
    GlowInDarkWhite = 159
    GlowInDarkOpaque = 46
    GlowInDarkTrans = 118
    GlitterTransClear = 101
    GlitterTransNeonGreen = 163
    GlitterTransLightBlue = 162
    GlitterTransPurple = 102
    GlitterTransDarkPink = 100
    SpeckleBlackSilver = 111
    SpeckleBlackGold = 151
    SpeckleBlackCopper = 116
    SpeckleDBGraySilver = 117

def main():
    lineRegex = re.compile("\\s*(\\d+)\\s+([\\w\\s-]+?)\\s+(\\d+)\\s+(\\d+)\\s+(\\d+)\\s+(\\d+)\\s+(\\d+\\s+-\\s+\\d+)\\s*")
    nameRegex = re.compile("[\\s-]+")
    for line in sys.stdin:
        m = lineRegex.match(line)
        if m:
            id = m.group(1)
            name = nameRegex.sub('', m.group(2))
            print("{} = {}".format(name, id))


if __name__ == "__main__":
    main()