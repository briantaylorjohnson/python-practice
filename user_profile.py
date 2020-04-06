### Chapter 8: Functions

## Using Arbitrary Keyword Arguments

# User Profile Exammple --> Know that I will receive information on user, but don't what information

def build_profile(first, last, **user_info):
""" The double asterisk tells the function to pack the additional key-value pairs into a dictionary it creates """
""" May see **kwargs which stands for keyword arguments """
    
    """ Build a dictionary containing everything we know about a user. """
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')

print(user_profile)