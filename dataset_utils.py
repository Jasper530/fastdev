import random 

def sample_from_dataset(dataset, n=None, ratio=None):
    if not n and not ratio:
        print('Please enter #samples or ratio.')
        return 

    if n:
        return random.sample(dataset, n)
    elif ratio:
        return random.sample(dataset, int(ratio*len(dataset)))

def view_dict_info(d):
    print('-'*40)
    for key, value in d.items():
        print(f'{key}: {type(value)}')
    print('-'*40)
