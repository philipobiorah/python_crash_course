def groups_per_user(group_dictionary):
    user_groups = {}
    

    for group , users in group_dictionary.items():
        for user in users:

            if user in user_groups:

                user_groups[user].append(group)
            else:
                user_groups[user] = [group]

    return (user_groups)




print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)


print(wardrobe)