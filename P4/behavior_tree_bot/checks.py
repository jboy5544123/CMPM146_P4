import math
from math import floor

def if_neutral_planet_available(state):
    return any(state.neutral_planets())


def have_largest_fleet(state):
    return sum(planet.num_ships for planet in state.my_planets()) \
             + sum(fleet.num_ships for fleet in state.my_fleets()) \
           > sum(planet.num_ships for planet in state.enemy_planets()) \
             + sum(fleet.num_ships for fleet in state.enemy_fleets())




#if theres an enemy fleet in transit towards a neutral planet that is closer to us
# return neautral planet closest to us and enemy fleet size
# return (closest_neutral, enemy fleet size)
def check_surrounding_planets(state):
    
    B = False
    closest_neutral_dist = math.inf
    closest_neutral = None
    
    for enemy_fleet in state.enemy_fleets():
        
        enemy_dest = enemy_fleet.destination_planet # gets planet ID
        
        for my_planet in state.my_planets():
            
            dist1 = state.distance(my_planet.ID, enemy_dest)
            
            if((enemy_dest.owner == 0) and (dist1 < closest_neutral_dist)):
                
                B = True
                closest_neutral = enemy_dest
                closest_neutral_dist = dist1
     
    return B
    #return (B, closest_neutral, closest_neutral_dist)
            
  
'''
# This is the one that returns all the closest ones

def check_surrounding_planets(state):
    
    dest = {}
    neutral_planets = state.neutreal_planets()
    
    for enemy_fleet in state.enemy_fleets(): # search all enemy fleets
        
        enemy_fleet_dest = enemy_fleet.destination_planet
        enemy_fleetID = enemy_fleet_dest.ID # get plane ID of current enemy fleet's dest planet
        
        for my_planet in state.my_planets():
    
            # if an enemy fleet's destination planet is the current neutral planet and
            # the fleet's trip length is longer than the distance between us and one of our planets,
            # put that into dest
            dist1 = enemy_fleet.total_trip_length
            if(enemy_fleet_dest in neutral_planets and dist1 > state.distance(my_planet.ID, enemy_fleetID)):
                
                dest[enemy_fleetID] = (enemy_fleet.turns, enemy_fleet.num_ships)
            
    return dest
'''

#if we are about to lose a planet
# if enemy fleet is number of turns away
# checking this function?
#def planet_status(state):


#if we have a planet that is significantly larger than an opposing planet that is currently being suppressed
# if a planet is x2(?) num_ships than opposing planet, check if it's the max amount of all we found
# Returns planet ID with the highest number of fleets available
# (best planet ID, max fleet)
def check_planet_size(state):
    
    B = False
    max_fleet = 0
    best_planet = None
    
    fleet_dest = [] # fleet_dest = [dest planet ID]
    # checking our fleets and if they're going to opposing planets first
    for my_fleets in state.my_fleets():
        
        # if(my_fleets.destination_planet.owner == 2)
        if(my_fleets.destination_planet in state.enemy_planets()): # if owned by enemy
            fleet_dest.append(my_fleets.destination_planet)
     
    # looking for max fleet
    for my_planet in state.my_planets():
        
        for enemy_planet in state.enemy_planets():
            
            # if we have a fleet going to that planet, the number of ships we have is bigger than
            # the enemy planet's, and it's the max fleet so far
            if((enemy_planet.ID in fleet_dest) and (my_planet.num_ships > enemy_planet.num_ships) and
               (my_planet.num_ships > max_fleet)):
                
                B = True
                best_planet = my_planet.ID
                max_fleet = my_planet.num_ships
                
    return B
    #return (B, best_planet, max_fleet)

#if we are close enough to capture an opposing planet that just sent out a fleet before they regrow their forces
# For every enemy fleet, check if we have a planet that's the same distance/same amoutn of turns
# away from destination planet and min planet.num_ships > fleet strength-planet ships
# return boolean
def check_enemy_forces(state):
    
    for enemy_fleet in state.my_fleets():
        
        enemy_dist = enemy_fleet.total_trip_length
        enemy_dest = enemy_fleet.destination_planet
        
        
        for my_planet in state.my_planets():
        
            our_dist = state.distance(my_planet.ID, enemy_dest)
            our_ships = find_available_ships(my_planet)
            
            # if same distance as enemy and our num is greater then send true
            if((our_dist == enemy_dist) and (our_ships > (enemy_fleet.num_ships - enemy_dest.num_ships))):
                return True
            
    return False
    
'''
def check_enemy_forces(state):
    
#if we are about to lose a planet
# if enemy fleet is number of turns away
# checking this function?
#def planet_status(state):

    close_by = False
    closest_planet_dist = math.inf
    our_closest_planet = None
    enemy_src_planet = None
    
    for enemy_fleet in state.enemy_fleets():
        
        # enemy fleet distance is the same for one of our planets
        # and it's safe
        if(enemy_fleet.turns_remaining == enemy_fleet.total_trip_length):
            
            enemy_src = enemy_fleet.source_planet
            
            for my_planet in state.my_planets():
                
                dist = state.distance(my_planet.ID, enemy_src)
                
                if(dist < closest_planet_dist):
                    
                    close_by = True
                    our_closest_planet = my_planet.ID
                    enemy_src_planet = enemy_src
                    closest_planet_dist = dist
                
    return (close_by, our_closest_planet, enemy_src_planet)        
'''        
            

#if we are winning or losing
# if we have less planets than the enemy, return 0; otherwise, return 1
def check_status(state):
    
    if(len(state.my_planets()) < len(state.enemy_planets())):
        return 0
    return 1

#check who is the weakest player in 3+ player games
# if we're the weakest, return 1; otherwise, return 2
def find_weakest_player(state):
    
    if(len(state.my_planets()) > len(state.enemy_planets())):
        return 1
    return 2

#if we are about to take a planet and it will need defense
# If we have a fleet <= 1 turn away from taking planet, check if there are
# enemy fleets on the way and close by; if there is, return true and otherwise return false
# returns planet at most risk of being overpowered
# return (True/False, planet ID, enemy fleet's size)
def defense(state):
    
    close_by = False
    planet = None
    cost = 0
    
    for my_fleet in state.my_fleets():
        
        if((my_fleet.turns_remaining <= 1) and (my_fleet.destination_planet.owner == 0)):
            
            for enemy_fleet in state.enemy_fleets():
                
                # if the enemy fleet is the same destination planet as my_fleet
                # and it is at most risk by comparing number of ships
                if((enemy_fleet.destination_planet == my_fleet.destination_planet) and
                   (my_fleet.num_ships < enemy_fleet.num_ships) and (cost < enemy_fleet.num_ships)):
                    
                    close_by = True
                    planet = enemy_fleet.destination_planet
                    cost = enemy_fleet.num_ships
                    
    return (close_by, planet, cost)
    

#check distance between all planets
# returns planets with the greatest distance
def max_dist(state):
    
    max_dist = 0
    our_planet = None
    dest_planet = None
    
    for my_planet in state.my_planets():
        for dest_planet in state.not_my_planets():
            
            if(state.distance(my_planet.ID, dest_planet.ID) > max_dist):
                
                our_planet = my_planet.ID
                other_planet = dest_planet.ID
                
    return (our_planet, dest_planet)

'''
# check distance but it's a list'
# returns a dict dist with a pair (our planet, dest planet) and the distance between them
# dict = {(our planet ID, dest planet ID) :  distance}
def check_dist(state):
    
    dist = {}
    
    # need planet ids for this one
    for my_planet in state.my_planets():
        for dest_planet in state.not_my_planets():
            dist[(my_planet.ID, dest_planet.ID)] = state.distance(my_planet.ID, dest_planet.ID)
            
    return dist
'''

# compares fleet sizes vs every other
# Returns list with planet id with biggest positive different and biggest negative difference
# l = [(planet IDs, best positive), (planet IDs, worst negative)]
def check_fleet_sizes(state):
    
    l = []
    max_pos = 0
    max_neg = 0
    
    for my_planet in state.my_planets():
        for other_planet in state.not_my_planets():
            
            diff = my_planet.num_ships - other_planet.num_ships
            
            if((diff > max_pos)):
                max_my_planet = my_planet.ID
                max_other_planet = other_planet.ID
                max_pos = diff
                
            if((diff < max_neg)):
                min_my_planet = my_planet.ID
                min_other_planet = other_planet.ID
                max_neg = diff
                
    l.append(((max_my_planet, max_other_planet), max_pos))
    l.append(((min_my_planet, min_other_planet), max_neg))
    
    return l
    
    

'''
#comparing fleet sizes of planets (returns list)
# Compare our planet fleets vs every other planet fleets
# Returns planet id with biggest positive different and biggest negative difference
# (planet ID, best positive), (planet ID, best negative)
def check_fleet_sizes(state):
    
    sizes = {}
    
    for my_planet in state.my_planets():
        for other_planet in state.not_my_planets():
            sizes[(my_planet.ID, other_planet.ID)] = my_planet.num_ships - other_planet.num_ships
            
    return sizes
'''

#determine what is a safe minimum fleet size for planets that are supressing other planets
# checks enemy fleets on the way to our planets; finds biggest fleet
# and sends that to determine how much we need to add later
def safe_min(state):
    
    safe_min = 0
    my_planets = state.my_planets()
    
    for enemy_fleet in state.enemy_fleets():
        
        if((enemy_fleet.destination_planet in my_planets) and (enemy_fleet.num_ships > safe_min)):
            
            safe_min = enemy_fleet.num_ships
        
    return safe_min

# HELPER FCNS

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
    enemy_strongest_planet = find_enemy_strongest_planet(state)
    my_strongest_planet = find_my_strongest_planet(state)
    min_fleet = floor(((enemy_strongest_planet.num_ships)-1) - (state.distance(planet,enemy_strongest_planet)*planet.growth_rate))

    return min_fleet

def find_available_ships(planet):
    available_ships = 0
    available_ships = floor((planet.num_ships) - find_minimum_fleet_size(planet))

    return available_ships
