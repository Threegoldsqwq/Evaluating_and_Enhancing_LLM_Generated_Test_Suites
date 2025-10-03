def parse_music(music_string: str) -> list[int]:
    """
    Parses a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each
    note lasts.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string: A string containing musical notes separated by spaces.

    Returns:
        A list of integers, where each integer represents the beat duration
        of a corresponding note in the input string.

    Examples:
        >>> parse_music('o o| .| o| o| .| .| .| .| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
        >>> parse_music('o')
        [4]
        >>> parse_music('.| o| o')
        [1, 2, 4]
        >>> parse_music('')
        []
    """
    # Define the mapping from note ASCII representation to beat duration
    note_duration_map = {
        'o': 4,   # whole note
        'o|': 2,  # half note
        '.|': 1   # quarter note
    }

    # Split the input string into individual note representations
    # An empty string will result in an empty list if using .split()
    # or [''] if using .split(' '). We handle the empty string case explicitly.
    if not music_string:
        return []

    note_representations = music_string.split()

    # List to store the resulting beat durations
    beat_durations = []

    # Iterate through each note representation and convert it to its beat duration
    for note_str in note_representations:
        if note_str in note_duration_map:
            beat_durations.append(note_duration_map[note_str])
        else:
            # Handle unrecognized note types.
            # Depending on requirements, one might raise an error,
            # log a warning, or skip the note.
            # For this problem, we assume valid input as per the problem description.
            # For robustness, we could add:
            # raise ValueError(f"Unrecognized musical note format: '{note_str}'")
            pass # Skipping unrecognized notes for now, assuming valid input

    return beat_durations