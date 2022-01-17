#!/usr/bin/env python3

class Stream:
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        self.pos = 0

    @property
    def remain(self):
        return self.size - self.pos

    def getbinary(self, n):
        end = self.pos + n
        if end > self.size: raise EOFError
        res = self.data[self.pos:end]
        self.pos = end
        return res

    def getbits(self, n):
        return int(self.getbinary(n), 2)

    def getsubstream(self, n):
        return Stream(self.getbinary(n))

class Packet:
    def __init__(self, stream):
        self.version = stream.getbits(3)
        self.type_id = stream.getbits(3)
        self.children = []

        if self.type_id == 4:
            v = -1
            value = 0
            while v & 16:
                v = stream.getbits(5)
                value = (value << 4) | (v & 15)
        elif stream.getbits(1):
            for i in range(stream.getbits(11)):
                self.children.append(Packet(stream))
        else:
            substream = stream.getsubstream(stream.getbits(15))
            while substream.remain >= 11:
                self.children.append(Packet(substream))

        if self.type_id == 0:
            value = sum(p.value for p in self.children)
        elif self.type_id == 1:
            value = 1
            for p in self.children: value *= p.value
        elif self.type_id == 2:
            value = min(p.value for p in self.children)
        elif self.type_id == 3:
            value = max(p.value for p in self.children)
        elif self.type_id != 4:
            a, b = self.children
            if self.type_id == 5: value = int(a.value >  b.value)
            if self.type_id == 6: value = int(a.value <  b.value)
            if self.type_id == 7: value = int(a.value == b.value)
        self.value = value

    def __str__(self):
        s = f"V{self.version:02d} T{self.type_id:02d} V{self.value}"
        return s

    def dump(self, level=0):
        print("  " * level + "- " + str(self))
        for c in self.children:
            c.dump(level+1)

    def version_sum(self):
        return self.version + sum(p.version_sum() for p in self.children)

def HexDecode(hexdata):
    return ''.join(format(int(x,16),'04b') for x in hexdata.strip())

def run(hexdata, silent=False):
    if not silent:
        print(hexdata)
    doc = Packet(Stream(HexDecode(hexdata)))
    doc.dump()
    print("version sum:", doc.version_sum())
    print("top-level value:", doc.value)
    print()

if __name__ == "__main__":
    run("D2FE28")
    run("38006F45291200")
    run("EE00D40C823060")
    run("8A004A801A8002F478")
    run("620080001611562C8802118E34")
    run("C0015000016115A2E0802F182340")
    run("A0016C880162017C3686B18A3D4780")

    run(open("input.txt").read())
