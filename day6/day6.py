# PART 1
def get_orbits(orbit_map):

    # Calculate number of direct and indirect orbits for each space body
    still = True
    num_orbits = {'COM': 0}
    prev_len = -1
    while still:
        snapshot = num_orbits.copy()
        for core_element in snapshot:
            if core_element in orbit_map:
                for orbiting_element in orbit_map[core_element]:
                    num_orbits[orbiting_element] = num_orbits[core_element] + 1

        if len(num_orbits) == prev_len:
            still = False

        prev_len = len(num_orbits)

    # Get total amount of orbits
    total_orbits = 0
    for body in num_orbits:
        total_orbits += num_orbits[body]

    return total_orbits


# PART 2
def get_transfers(orbit_map):
    s = 'YOU'
    sc = 0
    sd = {}
    e = 'SAN'
    ec = 0
    ed = {}

    while True:
        for body in orbit_map:
            if s in orbit_map[body]:
                s = body
                sd[body] = sc
                sc += 1
            if e in orbit_map[body]:
                e = body
                ed[body] = ec
                ec += 1

        for k in sd:
            if k in ed.keys():
                return sd[k] + ed[k]



if __name__ == "__main__":
    f = open("../inputs/day6.txt", "r")

    orbits = {}

    # Build orbit dictionary from input file
    for line in f:

        o = line.split(')')
        o[1] = o[1].split('\n')[0]
        if o[0] not in orbits:
            orbits[o[0]] = [o[1]]
        else:
            orbits[o[0]].append(o[1])

    res1 = get_orbits(orbits)

    print('There are', res1, 'orbits in the map data.')

    res2 = get_transfers(orbits)

    print('A total amount of', res2, 'transfers are needed to move from YOU to SAN.')

