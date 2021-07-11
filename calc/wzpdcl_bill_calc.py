# NOT TESTED, Rate from here, only for residential cases
# http://www.wzpdcl.org.bd/sites/default/files/files/wzpdcl.portal.gov.bd/law/4c2893eb_5dec_4679_b462_8b8e7a35110a/2020-03-15-09-32-8a64cf6756b231d80763f130963e3c20.pdf
class Chunk:
    def __init__(self, units, rate) -> None:
        self.units = units
        self.rate = rate

    def cost(self) -> int:
        return self.units * self.rate
    
    def __repr__(self) -> str:
        return f'Chunk(units={self.units}, rate={self.rate})'


def get_chunks(units):
    orig_unit = units
    out = []
    if units <= 50:
        out.append(Chunk(units=50, rate=3.75))
    else:
        out.append(Chunk(units=75, rate=4.19))

    units = orig_unit - 75
    if units > 0:
        u = min(125, units)
        out.append(Chunk(units=u, rate=5.72))
    
    units = orig_unit - 200
    if units > 0:
        u = min(100, units)
        out.append(Chunk(units=u, rate=6.00))

    units = orig_unit - 300
    if units > 0:
        u = min(100, units)
        out.append(Chunk(units=u, rate=6.34))

    units = orig_unit - 400
    if units > 0:
        u = min(200, units)
        out.append(Chunk(units=u, rate=9.94))

    units = orig_unit - 600
    if units > 0:
        out.append(Chunk(units=units, rate=11.46))

    return out


def total_bill(units):
    values = get_chunks(units)
    total = 0
    for v in values:
        total += v.cost()
    
    return total

total_unit = int(input('Total units: '))
print('Total calculated bill:', round(total_bill(total_unit), 2))