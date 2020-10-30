

def if_neutral_planet_available(state):
    return any(state.neutral_planets())


def have_largest_fleet(state):
    return sum(planet.num_ships for planet in state.my_planets()) \
             + sum(fleet.num_ships for fleet in state.my_fleets()) \
           > sum(planet.num_ships for planet in state.enemy_planets()) \
             + sum(fleet.num_ships for fleet in state.enemy_fleets())




#if theres an enemy fleet in transit towards a neutral planet that is closer to us
# Returns dict dest close to us with an enemy fleet on the way
# with the amount of turns it'll take before the enemy fleet and the size of the enemy fleet
# dest = {dest planet ID : (turns, fleet size)}
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

#if we are about to lose a planet
# If an enemy fleet is on its way with a bigger number to one of our planets
# in the next 3(?) turns, add to planets dict
# planets = { planet ID : enemy fleet size}
def planet_status(state):
    
    planets = {}
    
    for enemy_fleet in state.enemy_fleets():
        
        # if the enemy's fleet is larger than the destination planet, the turns remaining are <= 3,
        # and the destination planet is in our list of planets, add that planet to dict
        if(enemy_fleet.num_ships > enemy_fleet.destination_planet.num_ships and enemy_fleet.turns_remaining <= 3
           and enemy_fleet.destination_planet in state.my_planets()):
            planets[enemy_fleet.destination_planet.ID] = enemy_fleet.num_ships
        
    return planets

#if we have a planet that is significantly larger than an opposing planet that is currently being suppressed
# if a planet is x2(?) num_ships than opposing planet, send to planets dict
# planets = {planet ID with double : opposing planet ID}
def check_planet_size(state):
    
    planets = {}
    
    my_fleets = state.my_fleets()
    
    for my_planet in state.my_planets():
        
        my_planetID = my_planet.ID
        my_planet_double = my_planet.num_ships * 2
        
        for enemy_planet in state.enemy_planets():
            
            # if we have a fleet on the way to this enemy planet and our planet*2 > enemy_planet,
            # add to planets dict
            if(my_fleets.destination_planet in my_fleets and my_fleets.destination_planet.ID is enemy_planet.ID
               and my_planet_double > enemy_planet.num_ships):
                
                planets[my_planetID] = enemy_planet.ID
            
    return planets

#if we are close enough to capture an opposing planet that just sent out a fleet before they regrow their forces
#def check_enemy_planet_size(state)

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
#def defense(state)

#check distance between all planets
# returns a dict dist with a pair (our planet, dest planet) and the distance between them
# dict = {(our planet ID, dest planet ID) :  distance}
def check_dist(state):
    
    dist = {}
    
    # need planet ids for this one
    for my_planet in state.my_planets():
        for dest_planet in state.not_my_planets():
            dist[(my_planet.ID, dest_planet.ID)] = state.distance(my_planet.ID, dest_planet.ID)
            
    return dist

#comparing fleet sizes of planets
# Compare our planet fleets vs every other planet fleets
# Returns dict sizes with a pair (our planet, other planet) and difference between two fleets
# difference = our fleet size - other planet fleet size
# sizes = {(our planet ID, other planet ID) : difference}
def check_fleet_sizes(state):
    
    sizes = {}
    
    for my_planet in state.my_planets():
        for other_planet in state.not_my_planets():
            sizes[(my_planet.ID, other_planet.ID)] = my_planet.num_ships - other_planet.num_ships
            
    return sizes

#determine what is a safe minimum fleet size for planets that are supressing other planets
#def safe_min(state)
