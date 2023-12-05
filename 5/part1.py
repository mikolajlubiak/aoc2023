import re

with open('input.txt', 'r') as input:
    data = input.read().split('\n\n') # Split the input by \n\n to get the seeds category, the seed-to-soil map, and so on

    # Create a dictionary with seed as the key and nested dictionary as the value.
    # The nested dictionary has properties like seed, soild, and so on, as the key, and the corresponding number as a value.
    # This initiates all the seeds with all the properties, other that seed. equal to -1.
    seeds = {}
    for seed in re.sub(r'.*: ', '', data[0]).split(' '):
        seeds.update(
            {
                seed: {
                    'seed': int(seed),
                    'soil': -1,
                    'fertilizer': -1,
                    'water': -1,
                    'light': -1,
                    'temperature': -1,
                    'humidity': -1,
                    'location': -1,
                }
            }
        )

    for category in data[1:]: # Exclude the seeds category
        header = re.findall(r'\b\w+\b', category.split('\n')[0]) # The header (for eg. 'seed-to-soil map:') split to extract the interesting data
        type = (header[0], header[2]) # First one is the source, and the second one is the destination.
        for line in filter(None, category.split('\n')[1:]): # Go over every number series
            destination = int(line.split(' ')[0])
            source = int(line.split(' ')[1])
            length = int(line.split(' ')[2])
            for seed, properties in seeds.items(): # Go over every seed and update it.
                if properties[type[0]] in range(source, source+length): # If the source is in the scope
                    properties[type[1]] = destination+(properties[type[0]]-source) # Update the corresponding property (like soil, or location)
                    seeds[seed].update(properties)

    # Go over every seed. If the property value is -1, then change to property value to the value of seed.
    for seed in seeds:
        for property in seeds[seed]:
            if seeds[seed][property] == -1:
                seeds[seed][property] = seeds[seed]['seed']

    lowest_location = min(seeds[seed]['location'] for seed in seeds) # Check what is the lowest location
    print(lowest_location)