positions = ([23,46.0,8.3],[3,46.0,8.3])
mouvement = []
mouvement.append(positions[0][1:3])
mouvement.append(positions[1][1:3])

print(mouvement)
alt_diff = positions[-1][0] - positions[-2][0]
print(alt_diff)