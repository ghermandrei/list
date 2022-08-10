consum = [
    ## 10-20 km/h           50-60 km/h           100-120km/h          150-160km/h
    [2.0,                     5.0,                  4.0,                8.0],
    [3.0,                     4.0,                  5.0,                9.0],
    [5.0,                     4.8,                  7.0,               12.0],
]
col_labels=["10-20km/h","50-60km/h","100-120km/h","150-160km/h"]
raw_labels = [
    '1.2L',
    '2.0L',
    '8.0L',]
print(end="    ")    
for ri in range(len(consum[0])):
    print (f'|{col_labels[ri]:>12}|',end="")
print()
for ci in range(len(consum)):
    print(raw_labels[ci],end="")
    for ri in range(len(consum[0])):
        print(f'|{consum[ci][ri]:12.1f}|',end="")

    print()     