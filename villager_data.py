"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
       # open the file       # file = open(path)
    # create a set
    # get species info from file object and add each species to the set
    # return the created set

    each_species = set()
    file = open(filename)
    for line in file:
        line = line.rstrip()
        species = line.split('|')
        each_species.add(species[1])
    print(each_species)

    return species



def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    #open the file 
    #create an empty list for villagers
    #iterate over the data
    #strip the whitespace
    #split the the elements that separated by | for the first 2 indices
    #set up parameters that default all(species) unless a argument is passed in 
    #
    #append the names to villagers list

    file = open(filename)
    villagers = []
    for line in file:
        line = line.rstrip()    #strip the whitespace
        # print(type(line))
        attributes = line.split('|')  # creates a list
        print(attributes)
        name, species, personality, hobby, motto = attributes
        print(name, species)
        if species == search_string or search_string == "All": 
            villagers.append(name)
        


    # TODO: replace this with your code

    return sorted(villagers)
get_villagers_by_species('villagers.csv')


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    return []


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

    # TODO: replace this with your code

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

    # TODO: replace this with your code


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

    # TODO: replace this with your code
