PLANETS = (
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune"
)

def bf(planet1: str, planet2: str) -> tuple:
    """
    Takes two planet names and returns a tuple containing all planets
    whose orbits are located between the orbit of planet1 and planet2,
    sorted by proximity to the Sun.

    Args:
        planet1 (str): The name of the first planet.
        planet2 (str): The name of the second planet.

    Returns:
        tuple: A tuple of planet names located between planet1 and planet2,
               sorted by proximity to the Sun. Returns an empty tuple if
               planet1 or planet2 are not correct planet names, or if
               there are no planets in between.
    """
    # 1. Input Validation: Check if planet names are valid
    if planet1 not in PLANETS or planet2 not in PLANETS:
        return ()

    # 2. Find the indices of the given planets in our ordered list
    index1 = PLANETS.index(planet1)
    index2 = PLANETS.index(planet2)

    # 3. Determine the range for slicing
    # We need to find the smaller and larger index to correctly slice the PLANETS tuple.
    # The planets between will be from (min_index + 1) to (max_index - 1).
    start_slice_index = min(index1, index2)
    end_slice_index = max(index1, index2)

    # 4. Check if there are any planets in between
    # If the planets are the same or adjacent (e.g., Mercury and Venus),
    # then end_slice_index - start_slice_index will be 0 or 1,
    # meaning no planets are strictly *between* them.
    if end_slice_index - start_slice_index <= 1:
        return ()

    # 5. Slice the PLANETS tuple to get the planets in between
    # Python slicing is [start:end], where 'start' is inclusive and 'end' is exclusive.
    # So, to get planets between index 'A' and 'B', we slice from 'A+1' up to 'B'.
    result_planets = PLANETS[start_slice_index + 1 : end_slice_index]

    return result_planets