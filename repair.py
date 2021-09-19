import sys
import codecs

map = {
        "Tren?ín":              "Trenčín",
        "stupe?":               "stupeň",
        "Ostražitos?":          "Ostražitosť", 
        "Ve?mi":                "Veľmi",
        "Byt?a":                "Bytča", 
        "?adca":                "Čadca", 
        "Levo?a":               "Levoča",
        "Lu?enec":              "Lučenec", 
        "Pieš?any":             "Piešťany",
        "Rož?ava":              "Rožňava", 
        "Ša?a":                 "Šaľa", 
        "Stará ?ubov?a":        "Stará ľubovňa",
        "Topo??any":            "Topoľčany",
        "Tur?ianske Teplice":   "Turčianske Teplice",
        "Ve?ký Krtíš":          "Veľký Krtíš",
        "Vranov nad Top?ou":    "Vranov nad Topľou"
} 

def repair(line):
    for key in map:
        line = line.replace(key, map[key])
            
    return line

output = open(sys.argv[2], "w")

with codecs.open(sys.argv[1], mode="r", encoding="windows-1250") as input:
    while True:
        line = input.readline()
        if not line:
            break;
        
        output.write(repair(line))
        
output.close()
