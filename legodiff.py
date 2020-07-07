import sys
import colors
import xml.etree.ElementTree as ET
            
class ItemKey(object):
    def __init__(self, type, id):
        self.type = type
        self.id = id
        
    def __hash__(self): return hash(self.type) ^ hash(self.id)
    def __eq__(self, other): return self.type == other.type and self.id == other.id
    
    def __lt__(self, other):
        if self.type == other.type:
            return self.id < other.id
        elif self.type < other.type:
            return True
        return False
    
class ItemDesc(object):
    def __init__(self, key, color):
        self.key = key
        self.color = color
        
    def __hash__(self): return hash(self.key) ^ hash(self.color)
    def __eq__(self, other): return self.key == other.key and self.color == other.color
    
class ItemLot(object):
    def __init__(self):
        self._quantities = {}
        
    def addItem(self, color, quantity):
        total = quantity + self._quantities.setdefault(color, 0)
        if total == 0:
            del self._quantities[color]
        else:
            self._quantities[color] = total

    def addLot(self, other):
        for color, quantity in other.items():
            self.addItem(color, quantity)

    def subLot(self, other):
        for color, quantity in other.items():
            self.addItem(color, -quantity)
            
    def items(self): return self._quantities.items()

    def __len__(self): return len(self._quantities)

    def __str__(self):
        string = ''
        for color, quantity in sorted(self.items()):
            string += "  {:+d} x {}\n".format(quantity, color.name if color else '')
        return string
    
    def positiveQuantities(self): return sum(filter(lambda x: x > 0, self._quantities.values()))
    def negativeQuantities(self): return sum(filter(lambda x: x < 0, self._quantities.values()))
            
class ItemList(object):
    def __init__(self):
        self._lots = {}
        
    def addItem(self, desc, quantity):
        lot = self._lots.setdefault(desc.key, ItemLot())
        lot.addItem(desc.color, quantity)
        if len(lot) == 0:
            del self._lots[desc.color]

    def addList(self, other):
        for key, otherLot in other.items():
            lot = self._lots.setdefault(key, ItemLot())
            lot.addLot(otherLot)
            if len(lot) == 0:
                del self._lots[key]
        return self
            
    def subList(self, other):
        for key, otherLot in other.items():
            lot = self._lots.setdefault(key, ItemLot())
            lot.subLot(otherLot)
            if len(lot) == 0:
                del self._lots[key]
        return self

    def items(self): return self._lots.items()
    
    def clone(self): return ItemList().addList(self)
    
    def __add__(self, other): return self.clone().addList(other) 
    def __sub__(self, other): return self.clone().subList(other)
    
    def __str__(self):
        string = ''
        for key, lot in sorted(self.items()):
            net = lot.positiveQuantities() + lot.negativeQuantities()
            string += "{}:{}{}:\n".format(key.type, key.id, " ({:+d})".format(net) if net != 0 else '')
            string += str(lot)
            string += "\n"
            
        string += "{} items removed\n".format(-self.negativeQuantities())
        string += "{} items added\n".format(self.positiveQuantities())
        return string
    
    def positiveQuantities(self): return sum(x.positiveQuantities() for x in self._lots.values())
    def negativeQuantities(self): return sum(x.negativeQuantities() for x in self._lots.values())
    
def parseItemListXml(filename):
    itemList = ItemList()
    
    tree = ET.parse(filename)
    root = tree.getroot()
    for itemNode in root.findall('ITEM'):
        type = itemNode.findtext('ITEMTYPE')
        id = itemNode.findtext('ITEMID')
        colorNode = itemNode.find('COLOR')
        color = None if colorNode is None else colors.Color(int(colorNode.text))
        quantity = int(itemNode.findtext('MINQTY'))
        
        desc = ItemDesc(ItemKey(type, id), color)
        
        itemList.addItem(desc, quantity)
        
    return itemList

def main():
    if len(sys.argv) != 3:
        return
    
    a = parseItemListXml(sys.argv[1])
    b = parseItemListXml(sys.argv[2])
    
    print(b - a)
                
if __name__ == "__main__":
    main()