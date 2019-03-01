from collections import OrderedDict

def open_and_parse():
    f = open('b_lovely_landscapes.txt', 'r')
    first_line = f.readline()
    
    #Get the first information from the file 
    row_count = int(first_line)
    
    #Create grid
    grid = []
    for _ in range(row_count):
        grid.append(f.readline().rstrip())
    f.close()
    return grid

def number_of_slides(grid):
    slidenum = 0
    for k in grid:
        if k[0] == "H":
            slidenum += 1
        elif k[0] == "V":
            slidenum += 0.5
            
    if slidenum%1:
        slidenum = int(slidenum) + 1
    return str(int(slidenum))

def write_out(slidenum, grid):
    output = open("output.txt","w")
    output.writelines(str(slidenum) + "\n")
    for i in range(len(grid)):
        output.writelines(grid[i])
    
    output.close()


def main():
    #Parse all elements of the file
    grid = open_and_parse()
   
    #Arrange the grid
    arranged_grid = []
    for idx, j in enumerate(grid):
        lista = j.split()
        orientation = lista[0]
        tag_number = int(lista[1])
        tags = lista[2:tag_number+2]
        tags.sort()
        arranged_grid += [(orientation, tag_number, tags, str(idx)),]                            
    
    arranged_grid.sort(key=lambda x: x[2])
    
    #Number of slides    
    slidenum = number_of_slides(arranged_grid)
    
    #Convert 2 Vert to Horizontal
    vert = []
    for i in arranged_grid:
        if i[0] == "V":
            vert.append(i)
    
    
    vert_parsed = []
    for i in range(0, len(vert), 2):
        tags = vert[i][2] + vert[i+1][2]
        tags = sorted(tags)
        vert_parsed += [("H", len(vert[i][2]+ vert[i+1][2]),tags,vert[i][3] + " " +vert[i+1][3]),]
            
    #sort vertical photos  
    arranged_grid.sort(key=lambda x: x[2])
    
    #Put H and 2 V's all together
    final_grid = []
    for i in arranged_grid:
        if i[0] == "H":
            final_grid.append(i)
    final_grid += vert_parsed
    
    final_grid.sort(key=lambda x: x[2])
    
    tup = []        
    for i in range(0, len(final_grid)):
        tup += [str(final_grid[i][3]) + "\n",]
        
    write_out(slidenum, tup)

if __name__ == "__main__":
    main()