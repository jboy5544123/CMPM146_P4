import sys
sys.path.insert(0, '../')
from planet_wars import issue_order


def attack_weakest_enemy_planet(state): 
    # (1) If we currently have a fleet in flight, abort plan.
    if len(state.my_fleets()) >= 1:
        return False

    # (2) Find my strongest planet.
    strongest_planet = max(state.my_planets(), key=lambda t: t.num_ships, default=None)

    # (3) Find the weakest enemy planet.
    weakest_planet = min(state.enemy_planets(), key=lambda t: t.num_ships, default=None)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else:
        # (4) Send half the ships from my strongest planet to the weakest enemy planet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)


def spread_to_weakest_neutral_planet(state):
    # (1) If we currently have a fleet in flight, just do nothing.
    if len(state.my_fleets()) >= 1:
        return False

    # (2) Find my strongest planet.
    strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)

    # (3) Find the weakest neutral planet.
    weakest_planet = min(state.neutral_planets(), key=lambda p: p.num_ships, default=None)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else:
        # (4) Send half the ships from my strongest planet to the weakest enemy planet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)


#Attacking Strategy:

    #Cheese - attacking an enemy planet that just sent a fleet to another planet

    #Suppression - continually send ships at the rate they are being made at a certain enemy planet after

    #Charge - Check to see if at a significantly higher fleet count than an opposing planet if so fire if not continue charging

    #

#Spreading Strategy:

    #taking a neutral planet thats closer to us right after it is taken by opponent

    #taking a neutral planet that is reasonably close to us in order of least cost while maintaining out original fleet count
    #to a reasonable degree

    #


#Defending Strategy:

    #only defend if you have the resources to defend

    #if the opponent is sending a fleet to take one of our planets and we have time to rienforce it, rienforce the planet

    #if one of our planets needs defence defend it

    #if we are about to take a planet defend it

    #when a planet is about to get taken from us. if we are winning then dont abandon the planet,
    #if we are losing abandon the planet unless its our last planet

    #
