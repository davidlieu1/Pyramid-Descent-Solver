
#reads input file
def read_txt(filename):
    data = 'EMPTY INPUT'
    with open(filename, 'r') as f:
        data = f.read().split()
    return data

#writes output file
def write_txt(filename, txt):
    with open(filename,'w') as f:
        f.write(txt)
    
#returns tuple (target, [pyramid])
#(720, [[2], [4, 3], [3, 2, 6], [2, 9, 5, 2], [10, 5, 2, 15, 5]])
def parse(data):
    target = int(data[1])
    parsed_data = []
    for i in range(2,len(data)):
        parsed_data.append([int(num) for num in data[i].split(',')])

    return (target, parsed_data)

#solving algorithm
def solve(target, data, index, level):
    cur = target/data[level][index]
    if level == len(data)-1 :
        if cur == 1:
            return ' '
        
    if level < len(data)-1:
        if cur != 0:
            left = 'L'+solve(cur, data, index, level+1)
            right = 'R'+solve(cur, data, index+1, level+1)
        if len(left) > len(right): 
            return left
        else:
            return right
    return ''
        

#main
if __name__ == '__main__':
    data = read_txt('pyramid_sample_input.txt')
    ds = parse(data)
    path = solve(ds[0],ds[1],0,0)
    write_txt('pyramid_sample_output.txt', path[:-1])