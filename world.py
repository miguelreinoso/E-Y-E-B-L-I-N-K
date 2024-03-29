# E Y E B L I N K

# ====================================== WORLD ================================================

import enemies
import random

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self,player):
        pass 


class ThreeCyborgsTile(MapTile):
    def intro_text(self):
        return """
        There are lots of shelves full of parts, dirt and junk. 
        You can see a stand with three cyborgs on it. 
        They look asleep and abandoned for some reason.
        """

class StartTile(MapTile):
    def intro_text(self):
        return """
        There's only a wall with a strange drawing on it.
        There are doors to the east and the west.
        There's a plastic curtain to the north.
        """

class CrystalMachineTile(MapTile):
    def intro_text(self):
        return """
        Some sort of machinery is inside a crystal container
        with a built-in electromagnetic door.
        The door seems operated from a panel on the right.
        You look carefully at the panel and see a red button,
        a keypad and a holographic display.
        """

class DesertTile(MapTile):
    def intro_text(self):
        return """
        You open the door but you can't go nowhere from here.
        The door is suspended on the nothingness.
        All you can see is an infinite desert.
        """

class CenterTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in another chamber.
        There are doors on your left and right.
        In the center there's a drawing, it seems a labyrinth ...
        To the north there's a long and dark corridor.
        """

class OceanTile(MapTile):
    def intro_text(self):
        return """
        You open the door but you can't go nowhere from here.
        The door is suspended on the nothingness.
        All you can see is an infinite ocean.
        """

class ExitTile(MapTile):
    def intro_text(self):
        return """
        After walking for a while you arrive to a large room.
        Poweful lights and pure white walls are so bright that you can barely open your eyes.
        The only thing here is an artifact like a ring. It's void within.
        It has flashing lights on it.
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.75:
            self.enemy = enemies.GlassSpider()
            self.alive_text = "A Glass Spider attacks you!"
            self.dead_text = '''The floor is full of Glass Spider junk.
    ...
    
    There's nothing more here but the remainings of some droids.''' 
        else:
            self.enemy = enemies.Guardian()
            self.alive_text = "A Guardian attacks you!"
            self.dead_text =  '''The floor is full of Guardian parts.
    ...
    
    There's nothing more here but the remainings of some droids.''' 

        super().__init__(x,y)

    def intro_text(self):
        if self.enemy.is_alive():
            return self.alive_text 
        else: 
            return self.dead_text
        

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))

world_map = [
    [EnemyTile(0,0),ExitTile(1,0),EnemyTile(2,0)],
    [DesertTile(0,1),CenterTile(1,1),OceanTile(2,1)],
    [ThreeCyborgsTile(0,2),StartTile(1,2),CrystalMachineTile(2,2)]
]

def tile_at(x,y): # locates the tile at a coordinate
    if x < 0 or y < 0: 
        return None                                                                               
    try:
        return world_map[y][x]
    except IndexError:
        return None 
