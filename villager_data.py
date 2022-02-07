"""Functions to parse a file containing villager data."""

filename = open("villagers.csv")
file_All_Lines_2List = []
for line in filename: # each line in the file is a string
    line = line.rstrip().split("|") # remove space at end and line split. Reassign to line, now type(line): list
    file_All_Lines_2List.append(line)


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    species = []
    for elem in file_All_Lines_2List:
        species.append(elem[1])

    species = set(species)

    return species

# print(all_species(filename))

def get_villagers_by_species(filename, search_string=None):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    if search_string is None: 
        for elem in file_All_Lines_2List:
            villagers.append(elem[0])
    else:
        for elem in file_All_Lines_2List:
            if elem[1] == search_string:
                villagers.append(elem[0])

    return sorted(villagers)

# print(get_villagers_by_species(filename))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    def all_hobbies(filename):
        """Return a set of unique hobbies in the given file.
        Arguments:
            - filename (str): the path to a data file
        Return:
            - set[str]: a set of strings
        """
        hobbies = []
        for elem in file_All_Lines_2List:
            hobbies.append(elem[3])

        hobbies = set(hobbies)
        return hobbies
        
    hobbies = all_hobbies(filename)
    all_names_by_hobby =[]
    for hobby in hobbies:
        names_same_hobby = []
        for elem in file_All_Lines_2List:
            if elem[3] == hobby:
                names_same_hobby.append(elem[0])
        all_names_by_hobby.append(names_same_hobby)

    return all_names_by_hobby


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    for elem in file_All_Lines_2List:
        elem_tuple = tuple(elem)
        all_data.append(elem_tuple)
       
    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    for elem in file_All_Lines_2List:
        if elem[0] == villager_name:
            return elem[4]
    return None



def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    for elem in file_All_Lines_2List:
        if elem[0] == villager_name:
            personality = elem[3]
            break
    
    names_same_personality = []
    for elem in file_All_Lines_2List:
        if elem[3] == personality:
            names_same_personality.append(elem[0])
    return names_same_personality


if __name__ == "__main__":
    # print(all_species(filename))
    # print(get_villagers_by_species(filename,"Bear"))
    # print(all_names_by_hobby(filename))
    # print(find_motto(filename, "Audie"))
    # print(find_likeminded_villagers(filename, "Audie"))
    print(all_data(filename))


