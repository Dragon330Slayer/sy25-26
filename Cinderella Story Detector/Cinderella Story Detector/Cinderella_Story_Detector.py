seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
winners = ['Purdue', 'FDU', 'FAU', 'Memphis', 'Duke', 'Oral Roberts', 'UVA', 'Furman', 'Kentucky', 'Pitt', 'Kansas', 'Howard', 'Texas', 'Penn St', 'UCLA', 'UNC Asheville']
total_upsets = (0)
for i in seeds:
    if i >= 10:
        print(f"{i} Cinderella Alert! {winners[seeds.index(i)]} pulls the upset!")
    if i >= 10:
        total_upsets = total_upsets + 1
print("Total upsets =" ,total_upsets)
