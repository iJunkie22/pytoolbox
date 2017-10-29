# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import sys


class AsciiChar(object):
    # _asciiTable = collections.OrderedDict()

    # @staticmethod
    # def __new__(cls, ordinalDecInt, description="Foobar", symbol=None):
    #     obj = super(AsciiChar, cls).__new__(ordinalDecInt, description, symbol)
    #     AsciiChar._asciiTable[ordinalDecInt] = obj
    #     return obj

    # bin = property(lambda self: "{:08b}".format(self._ord))

    def __init__(self, ordinalDecInt, symbol=None, description="", escapeChar=None):
        """

        :type ordinalDecInt: int
        """
        self._ord = ordinalDecInt
        self._symbol = symbol
        self._description = description
        self._escapeChar = None

    @property
    def dec(self):
        return self._ord

    def __oct__(self):
        return oct(self._ord)

    def __hex__(self):
        return hex(self._ord)

    @property
    def oct(self):
        return "{:03o}".format(self._ord)

    @property
    def hex(self):
        return "{:02X}".format(self._ord)

    @property
    def bin(self):
        return "{:08b}".format(self._ord)

    @property
    def html(self):
        return "&#{:03d};".format(self._ord)

    @property
    def escape(self):
        if self._escapeChar:
            return "\\{}".format(self._escapeChar)
        else:
            return "\\x{}".format(self.hex)

    @property
    def symbol(self):
        if self._symbol:
            return self._symbol
        else:
            return unichr(self._ord)

    def __index__(self):
        return self._ord.__index__()

AsciiTable = map(lambda tup: AsciiChar(*tup), [
    (0, "NUL", "Null char"),
    (1, "SOH", "Start of Heading"),
    (2, "STX", "Start of Text"),
    (3, "ETX", "End of Text"),
    (4, "EOT", "End of Transmission"),
    (5, "ENQ", "Enquiry"),
    (6, "ACK", "Acknowledgment"),
    (7, "BEL", "Bell", "a"),
    (8, "BS", "Back Space", "b"),
    (9, "HT", "Horizontal Tab", "t"),
    (10, "LF", "Line Feed", "n"),
    (11, "VT", "Vertical Tab", "v"),
    (12, "FF", "Form Feed", "f"),
    (13, "CR", "Carriage Return", "r"),
    (14, "SO", "Shift Out / X-On"),
    (15, "SI", "Shift In / X-Off"),
    (16, "DLE", "Data Line Escape"),
    (17, "DC1", "Device Control 1"),
    (18, "DC2", "Device Control 2"),
    (19, "DC3", "Device Control 3"),
    (20, "DC4", "Device Control 4"),
    (21, "NAK", "Negative Acknowledgement"),
    (22, "SYN", "Synchronous Idle"),
    (23, "ETB", "End of Transmit Block"),
    (24, "CAN", "Cancel"),
    (25, "EM", "End of Medium"),
    (26, "SUB", "Substitute"),
    (27, "ESC", "Escape"),
    (28, "FS", "File Separator"),
    (29, "GS", "Group Separator"),
    (30, "RS", "Record Separator"),
    (31, "US", "Unit Separator"),
])

for printableCharOrd in xrange(32, 256):
    AsciiTable.append(AsciiChar(printableCharOrd))

if len(sys.argv) == 1:
    # No args were passed
    for asciiRowI in xrange(128):
        # print("{0.dec}".format(asciiRow))
        leftTable = "{0.dec}\t{0.oct}\t{0.hex}\t{0.bin}\t{0.symbol}".format(AsciiTable[asciiRowI])
        rightTable = "{0.dec}\t{0.oct}\t{0.hex}\t{0.bin}\t{0.symbol}".format(AsciiTable[asciiRowI+128])
        print("\t\t\t".join((leftTable, rightTable)))
