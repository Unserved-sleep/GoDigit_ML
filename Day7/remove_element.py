colors = ['Red','Green', 'Pink', 'Blue', 'Black', 'Purple', 'Yellow', 'Magenta', 'Brown']
index_to_remove = [0,2,5]

new_colors = []
new_colors = list(map(lambda x: colors[x] if x not in index_to_remove else None, range(len(colors))))
new_colors = list(filter(None, new_colors))
print(new_colors)


new_colors = []
for i, colors in enumerate(colors):
    if i not in index_to_remove:
        new_colors.append(colors)
print(new_colors)
