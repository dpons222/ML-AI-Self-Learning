names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II']
months = ['October', 'September', 'September', 'November']
years = [1924, 1928, 1932, 1932]

def create_hurricane_dict(names, months, years):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i]
        }
    return hurricanes

hurricane_data = create_hurricane_dict(names, months, years)
print(hurricane_data)