class Solution(object):
    def islandPerimeter(self, grid):
        count = 0
        for i in grid:
            for k in i:
                if k == 1:
                    count+=4              
        for k in range(0,len(grid[0])):
            i=1
            while i<len(grid):
                if grid[i][k]==1 and grid[i-1][k]==1:
                    count -= 2
                i+=1
        for i in range(0,len(grid)):
            k=1
            while k<len(grid[0]):
                if grid[i][k]==1 and grid[i][k-1]==1:
                    count -=2
                k+=1    
        return count 