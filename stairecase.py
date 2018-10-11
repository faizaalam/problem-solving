n = int(input())

for i in range(1,n+1):
    space = ' ';
    hash = '#'
    no_of_space = n -i ;
    no_of_hash = n- no_of_space;
    print(space*no_of_space + no_of_hash*hash)