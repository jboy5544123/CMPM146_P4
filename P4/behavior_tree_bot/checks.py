

def if_neutral_planet_available(state):
    return any(state.neutral_planets())


def have_largest_fleet(state):
    return sum(planet.num_ships for planet in state.my_planets()) \
             + sum(fleet.num_ships for fleet in state.my_fleets()) \
           > sum(planet.num_ships for planet in state.enemy_planets()) \
             + sum(fleet.num_ships for fleet in state.enemy_fleets())




#if theres an enemy fleet in transit towards a neutral planet that is closer to us

#if we are about to lose a planet

#if we have a planet that is significantly larger than an opposing planet that is currently being suppressed

#if we are close enough to capture an opposing planet that just sent out a fleet before they regrow their forces

#if we are winning or losing

#check who is the weakest player in 3+ player games

#if we are about to take a planet and it will need defense

#check distance between all planets

#comparing fleet sizes of planets

#determine what is a safe minimum fleet size for planets that are supressing other planets
