def spr_list(filename):
    new_list = []
    coord_str = []
    with open(filename, 'r+') as f:
        list_ = f.readlines()
        for index in range(len(list_)):
            new_list.append(list_[index].replace('\n', ''))
    range1 = new_list.index('{level}') +1
    range2 = new_list.index(new_list[-1])-1
    for i in range(range1,range2):
        coord_str.append(new_list[i])
    return coord_str
def make_coord(sprite_list):
    thee_list = []
    type_a = ''
    xcoords = ''
    ycoords = ''
    for i in sprite_list:
        for nums in range(0,3):
            type_a +=i[nums]
        type_of = int(type_a)
        x_index = i.index('(')+1
        x1_index = i.index(',')
        y_index = i.index(',')+1
        y1_index = i.index(')')
        for pos_lst1 in range(x_index,x1_index):
            xcoords +=i[pos_lst1]
            real_xcord = int(xcoords)
        for pos_lst2 in range(y_index,y1_index):
            ycoords +=i[pos_lst2]
            real_ycord = int(ycoords)
        dek_cord_x = real_xcord * 8
        dek_cord_y = real_ycord * 8
        thee_list.append(type_of)
        thee_list.append((dek_cord_x,dek_cord_y))
        type_a = ''
        xcoords = ''
        ycoords = ''      
    return thee_list
def write_to_file(type_of_block,coordinates,filename):
    with open(filename, 'a') as f:
        f.write(f'{type_of_block} ({coordinates[0]//8},{coordinates[1]//8})\n')
def close_out(filename):
    with open(filename, 'a') as f:
        f.write('{end}')
def start_out(filename):
    with open(filename, 'w') as f:
        f.write('{level}\n')
    
    
if __name__ == '__main__':
    x = spr_list('bruhsmth.txt')
    the_ultimate_list = make_coord(x)
    print(the_ultimate_list)
    write_to_file(100,(512,39),'anewlevel.txt')
