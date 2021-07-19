"""Exercise 52 - Planisphere."""


class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


central_corridor = Room
  print(dedent("""
                     The Gothon of Planet Percal #25 have invaded your ship and
                     destroyed your entire crew. You are the last surviving
                     member and your last mission is to get the neutron destruct
                     bomb from the Weapon Amory, put it in the bridge, and 
                     blow the ship up after getting into an scape pod.

                     You're running down the central corridor to the Weapons 
                     Armory when a Gothon jumps out, red scaly skin, dark grimy 
                     teeth, and evil clow costume flowing around his hate 
                     filled body. He's blocking the door to the Armory and 
                     about to pull a weapon to blast you.
                     """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                         Quick on the draw you yank out your blaster and fire 
                         it at the Gothon. His clow costume is flowing and 
                         moving around his budy, which throws off your aim. 
                         Your laser hits his costume but misses hum entirely. 
                         This completely ruins his brand new costume his mother 
                         bought him, whitch makes him fly into an insane rage 
                         and blast you repeatedly in the face until you are 
                         dead.  Then he eats you. 
                         """))
            return 'death'

        elif action == "dodge!":
            print(dedent(""" 
                         Like a world class boxer you dodge. weave, slip and 
                         slide right as the Gothon's blaster cranks a laser 
                         past your head.    In the middle of your artful dodge 
                         your foot slips and you bang your head on the metal 
                         wall and pass out.    You wake up shortly after only to
                         die as the Gothon stomps on your head and eats you.
                         """))
            return 'death'

        elif action == 'tell a joke':
            print(dedent("""
                         Lucky for you they made you learn Gothon insults in 
                         the academy. you tell the one Gothon joke you know: 
                         Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, 
                         fur fvgf nebhag gut ubhfr.  The Gothon stops, tries 
                         not to laugh, then busts out loughing and can't move. 
                         While he's laughing you run up and shoot hum square in 
                         the head putting hum down, them jump through the 
                         Weapon Armory door.
                         """))
            return "laser_weapon_armory"

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent(""" 
                     You do a dive roll into the Weapon Armory, crouch and scan 
                     the room for more Gothons that might be hiding.    It's dead 
                     quiet, too quiet. You stand yo and run to the far side of 
                     the room and find the neutron bomb in its container.
                     There's a keypad lock on the box and you need the code to 
                     get the bomb out. If you get the code wrong 10 times then 
                     the lock cloese forever and you can't get the bomb.    The
                     code is 3 digits.
                     """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("|keypad|> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZEDDDD!")
            guesses += 1
            guess = input("|keypad|> ")

        if guess == code:
            print(dedent("""
                  The container clicks open and the seal breaks, letting 
                  gas out.    You grab the neutron bomb and run as fast as
                  you can to the bridge where you must place it in the 
                  right spot.
                  """))
            return 'the_bridge'

        else:
            print(dedent("""
                  The lock buzzes one last time and then you hear a 
                  sickening melting sound as the machanism is fused 
                  together. You decide to sit there, and finnaly the 
                  Gothons blow up the ship from their ship and you die.
                  """))
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              You burst onto the Bridge with the neutron destruct bomb 
              under your arm and surprise 5 Gothons who are trying to 
              take control of the ship.   Each of then has an even uglier
              clow costume than the last.   They haven't pulled their 
              weapons out yet, as they see the active bomb under your 
              arm and don't want to set it off.
              """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons 
                and make a leap for the door. Right as you drop it a 
                Gothon shoots you right in the back killing you. As
                you die you see abitger Gothon frantically try to 
                disarm the bomb. You die knowing they will probably 
                blow up when it goes off.
                """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent(""" 
                You point your blaster at the bomb unter your arm and 
                the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then 
                carefully place the bomb on the floor, pointing your
                blaster at it. You then jump back through the door, 
                punch the close button and blast the lock so the 
                Gothons can't get out.  Now that the bomb is placed
                you run to the scape pod to get off this tin can.
                """))
            return 'escape_pod'

        else:
            print("DOES NOT COMPUT!")
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to 
            the escape pod before the whole ship explodes.   It seems 
            like hardly any Gothon are on the ship, so your run is
            clear of interference.   You get to the chamber with the 
            escape pods, and now need to pick one to take.    Some of
            them could be damaged but you don't have time to look.
            There's 5 pods, wich one do you take?
            """))

        good_pod = randint(1,5)
        guess = input('[pod #]> ')


        if int(guess) != good_pod:
            print(dedent("""
                         You jump into pod {guess} and hit the eject button.
                         The pod escapes outo into the void of space, then
                         implodes as the hull ruptures, crushing your body into
                         jam jelly.
                         """))
            return 'death'
        else:
            print(dedent("""
                         You jump into pod {guess} and hit the eject button.
                         The pod easily slides out into space heading to the
                         planet below.   As it flies to the planet, you look
                         back and see your ship implode then explode like a
                         bright star. taking out the Gothon ship at the same
                         time.   You won!
                         """))

            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

