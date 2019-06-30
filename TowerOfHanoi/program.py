def TowerOfHanoi(n , from_rod, to_rod, aux_rod):

    if n > 0:
        TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
        print ("Moving {} disk from rod {} to rod {}".format(n, from_rod, to_rod))
        TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


TowerOfHanoi(4, 'A', 'C', 'B')

'''
Move disk 2 from rod A to rod C
Move disk 1 from rod B to rod C
Move disk 3 from rod A to rod B
Move disk 1 from rod C to rod A
Move disk 2 from rod C to rod B
Move disk 1 from rod A to rod B
Move disk 4 from rod A to rod C
Move disk 1 from rod B to rod C
Move disk 2 from rod B to rod A
Move disk 1 from rod C to rod A
Move disk 3 from rod B to rod C
Move disk 1 from rod A to rod B
Move disk 2 from rod A to rod C
Move disk 1 from rod B to rod C

'''