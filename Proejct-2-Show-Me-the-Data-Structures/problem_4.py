class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    if user in group.get_users(): # Found the user as an individual user in the group
        return True
    else: # There is a possibility that user might be a part of sub-group
        if len(group.get_groups()) == 0: # If there are no subgroups in the current group, return False
            return False
        else:
            
            for single_group in group.get_groups():
                # Recursively call the same function till we exhaust all the sub-groups
                if is_user_in_group(user, single_group):
                    return True
    
    return False

# As given in the problem statement
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Self test #1
print(is_user_in_group(user='parent_user', group=parent))
# Output: False

# Self test #2
print(is_user_in_group(user='child_user', group=parent))
# Output: False

# Self test #3
print(is_user_in_group(user='sub_child_user', group=parent), '\n')
# Output: True

# Self test #4 : Entering empty string
print(is_user_in_group(user='', group=parent))
# Output: False