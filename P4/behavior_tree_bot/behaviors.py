import sys
from math import floor
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
def cheese(state):

    #sending_planet = find_my_strongest_planet(state)
    #enemy_planet = find_enemy_weakest_planet(state)
    
    sending_planet = max(state.my_planets(), key=lambda t: t.num_ships, default=None)
    enemy_planet = min(state.enemy_planets(), key=lambda t: t.num_ships, default=None)
    
    check = find_available_ships(state, sending_planet)
    
    if(check > 0):
        return issue_order(state, sending_planet.ID, enemy_planet.ID, check)
    else:
        return False

    #Suppression - continually send ships at the rate they are being made at a certain enemy planet after









    #Charge - Check to see if at a significantly higher fleet count than an opposing planet if so fire if not continue charging

    #

#Spreading Strategy:
    '''

    #taking a neutral planet thats closer to us right after it is taken by opponent
def over_spreading(state):


    available_ships = find_my_strongest_planet(state).num_ships

    sending_planet = state.my_planets()[0]

    #maybe implement something to find the best planet to use
    sending_planet = find_my_strongest_planet(state)


    for neut_planet in state.neutral_planets():
        for enemy_fleet in state.enemy_fleets():
            if (enemy_fleet.destination_planet == neut_planet and state.distance(enemy_fleet.source_planet, neut_planet) <= state.distance(sending_planet, neut_planet)):
                neutral_planet = neut_planet


    issue_order(state, sending_planet.ID, neutral_planet.ID, find_available_ships(sending_planet))


    #taking a neutral planet that is reasonably close to us in order of least cost while maintaining out original fleet count
    #to a reasonable degree
def spread(state):
    #(1) assign weights to distance to planet, cost, and growth weight
    distance_weight = 1
    cost_weight = 1
    growth_weight = 1


    #(2) find the neutral planet that is most efficient to claim
    value = 1000000

    planet_to_take = (state.neutral_planets())[0]

    for planet in state.neutral_planets():
        planet_value = planet.num_ships*cost_weight + planet.growth_rate*growth_weight + state.distance(state.my_planets[0], planet)*distance_weight

        if(planet_value <= value):
            value = planet_value
            planet_to_take = planet

    #(3) check the enemy fleet size to see if you can claim safely
    enemy_ships_available = 0
    my_ships_available = 0
    my_strongest_planet = find_my_strongest_planet(state)
    enemy_strongest_planet = find_enemy_strongest_planet(state)
    for planets in state.my_planets():
        my_ships_available += planets.num_ships
        #if(my_strongest_planet.num_ships <= planet.num_ships):
        #    my_strongest_planet = planet

    for planets in state.enemy_planets():
        enemy_ships_available += planets.num_ships
        #if(enemy_strongest_planet.num_ships <= planet.num_ships):
        #    enemy_strongest_planet = planet


    if(my_strongest_planet.num_ships>=(enemy_ships_available/(len(state.enemy_planets())+1)) and my_strongest_planet.num_ships + (state.distance(my_strongest_planet.ID,enemy_strongest_planet.ID)*my_strongest_planet.growth_rate) >= enemy_strongest_planet.num_ships*0.5):
        issue_order(state, my_strongest_planet.ID, planet_to_take.ID, find_available_ships(my_strongest_planet))
        '''


def find_my_strongest_planet(state):
    my_strongest_planet = state.my_planets()[0]
    for planet in state.my_planets():
        if(my_strongest_planet.num_ships <= planet.num_ships):
            my_strongest_planet = planet

    return my_strongest_planet


def find_enemy_strongest_planet(state):
    enemy_strongest_planet = state.enemy_planets()[0]
    for planet in state.enemy_planets():
        if(enemy_strongest_planet.num_ships <= planet.num_ships):
            enemy_strongest_planet = planet

    return enemy_strongest_planet


def find_my_weakest_planet(state):
    my_weakest_planet = state.my_planets()[0]
    for planet in state.my_planets():
        if(my_weakest_planet.num_ships >= planet.num_ships):
            my_weakest_planet = planet

    return my_weakest_planet


def find_enemy_weakest_planet(state):
    enemy_weakest_planet = state.enemy_planets()[0]
    for planet in state.enemy_planets():
        if(enemy_weakest_planet.num_ships >= planet.num_ships):
            enemy_weakest_planet = planet

    return enemy_weakest_planet


def find_minimum_fleet_size(planet, state):
    min_fleet = 0
    enemy_strongest_planet = max(state.enemy_planets(), key=lambda t: t.num_ships, default=None)
    #my_strongest_planet = max(state.my_planets(), key=lambda t: t.num_ships, default=None)
    min_fleet = floor(((enemy_strongest_planet.num_ships)-1) - (state.distance(planet.ID,enemy_strongest_planet.ID)*planet.growth_rate))

    return min_fleet

def find_available_ships(state, planet):
    
    available_ships = 0
    available_ships = floor((planet.num_ships) - find_minimum_fleet_size(planet, state))

    return available_ships


#Defending Strategy:

    #only defend if you have the resources to defend

    #if the opponent is sending a fleet to take one of our planets and we have time to rienforce it, rienforce the planet

    #if one of our planets needs defence defend it

    #if we are about to take a planet defend it

    #when a planet is about to get taken from us. if we are winning then dont abandon the planet,
    #if we are losing abandon the planet unless its our last planet

    #

