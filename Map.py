class Map:
    CHAR_DIC = {
            " " : "free",
            "X" : "robot",
            "O" : "obstacle",
            "." : "obstacle",
            "U" : "exit"
            
    }
    def __init__(self, map_content, map_name):
        self.map_name = map_name
        tmp_rows = map_content.split("\n")
        tmp_arr = [list(row) for row in tmp_rows]
        x = 0;
        y = 0;
        self.width = len(tmp_arr[0])
        self.height = len(tmp_arr)
        self.map_arr = []
        for row in tmp_arr:
            map_row = []
            x = 0
            for col in row:
                if (col == 'X'):
                    self.posx = x
                    self.posy = y
                zone = Zone(self.CHAR_DIC[col], col)
                map_row.append(zone)
                x += 1
            self.map_arr.append(map_row)
            y += 1
    def __str__(self):
        return "\n".join(["".join([zone.symbol for zone in row]) for row in self.map_arr])

    def move(self, x, y):
        if self.posx + x >= 0 and self.posy + y >= 0 and self.posx + x < self.width and self.posy < self.height:
            if (self.map_arr[self.posy + y][self.posx + x]).type == 'free':
                self.map_arr[self.posy][self.posx] = Zone("free", " ")
                self.map_arr[self.posy + y][self.posx + x] = Zone("robot", "X")
                self.posx += x
                self.posy += y
            if (self.map_arr[self.posy + y][self.posx + x]).type == 'exit':
                return 1


class Zone:
    def __init__(self, zone_type, zone_symbol):
        self.symbol = zone_symbol
        self.type = zone_type
    
    
