from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random
from ast import literal_eval



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file =  "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

back_track = {"n": "s", "s": "n", "e": "w", "w": "e"}

def visit_rooms(starting_room, visited=None):
    # print(player.current_room)
    #init visited properly
    if visited is None:
        visited = set()
    #start at cur room
    cur = player.current_room
    
    #create path taken list   
    my_path = []
   
    #get exits for cur room      
    for cur_move in cur.get_exits():
        #move to room
        player.travel(cur_move)
        # make this room the cur room
        cur = player.current_room
        
        if cur not in visited:
        #check if not been visited, add to visited
            visited.add(cur)
                   
        #put in my path
            my_path.append(cur_move)
        #call itself 
            my_path = my_path + visit_rooms(cur, visited)
        #backtrack and append in my path
            player.travel(back_track[cur_move])
            my_path.append(back_track[cur_move])
            
            # print(my_path)
        # it has been visited so back track   
        else:
            player.travel(back_track[cur_move])
            
    return my_path  



  

traversal_path = visit_rooms(player.current_room)
    
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
