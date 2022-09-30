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
        attributes_list = line.split('|')  # ['Cyrano', 'Aardvark', ]
        each_species.add(attributes_list[1])
    print(each_species)

    return attributes_list


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
        # print(attributes)
        name, species, personality, hobby, motto = attributes
        # print(name, species)
        if species == search_string or search_string == "All": 
            villagers.append(name)

    # TODO: replace this with your code

    return sorted(villagers)
# print(get_villagers_by_species('villagers.csv'))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    # [['Andrea', 'Julia'], ['Marie-Claire'], ["Khaled"]]
    # initialize several lists, one for each hobby
        # education = []
        # fitness = []
        # reading = []
    # for each line, determine the hobby for that villager and that tells
        # us which list to add the name to
    # put all of the hobby lists into the list to return
    
    fitness = []
    education = []
    fashion = []
    music = []
    play = []
    nature = []

    file = open(filename)

    for line in file:
        line = line.rstrip()
        attributes =  line.split('|')
        hobby = attributes[3]
        name = attributes[0]

        if hobby == 'Fitness':
            fitness.append(name)
        if hobby == 'Education':
            education.append(name)
        if hobby == 'Fashion':
            fashion.append(name)
        if hobby == 'Music':
            music.append(name)
        if hobby == 'Play':
            play.append(name)
        if hobby == 'Nature':
            nature.append(name)

    return [
        fashion,
        fitness,
        education,
        music, 
        play,
        nature
        ]
# print("ALL NAMES BY HOBBY: ", all_names_by_hobby('villagers.csv'))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    # create an empty list to store the data
    # open the file 
    # strip the white space 
    # split by "|" delimiter (will return a list)
    # make the 


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
