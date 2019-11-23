In [92]: a = [34,'ted','joe']

In [93]: i = ",".join([str(x) for x in a])

In [94]: i
Out[94]: '34,ted,joe'

In [95]: a = ['Ted', 45]

In [96]: s = f"{a[0]} is really just {a[1]}"

In [97]: s
Out[97]: 'Ted is really just 45'

In [98]: "{name} is 55".format(name="Jeff")
Out[98]: 'Jeff is 55'
