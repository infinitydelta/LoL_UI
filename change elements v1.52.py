import os

"""
    How to use:
    
    Place this file within the same folder as the .ini's that control UI elements'
    positioning on screen (so far only the target bar and team frames). A new
    "edited" folder will be created where all the files are. Change the x,y offset
    to change how much the UI will move, relative to its original position.

"""

def elementMove(filename, groupname, xOffset, yOffset):

    #create new folder "edited" and recreate all files
    path = os.path.dirname(__file__)+"/edited"
    if not os.path.exists(path):
        os.makedirs(path)
        
    file = open(filename, "r")
    newfile = open(path+"/"+filename, "w")
    
    found = False    

    
    for num, line in enumerate(file, 1):

        #search for group keyword to find corresponding coordinates

        #group keyword line
        if ("Group: " + groupname ) in line:
            
            found = True

        #coordinates line    
        if "Rect:" in line and found:
            try:
                
                #get coordinates only
                numbers = line[line.index(" ") + 1:line.index("/") - 1]
                
                #separate first and second pair of coords            
                firstpair = numbers[:numbers.index(' - ')]
                
                secondpair = numbers[numbers.index(' - ')+3:]
                
                #individual numbers
                x1 = (firstpair[:firstpair.index(',')])
                y1 = (firstpair[firstpair.index(",") +1:])
                
                x2 = (secondpair[:secondpair.index(",")])
                y2 = (secondpair[secondpair.index(',')+1:])

                #new coords
                nx1 = float(x1) + xOffset
                nx2 = float(x2) + xOffset
                ny1 = float(y1) + yOffset
                ny2 = float(y2) + yOffset

                
                found = False
                #manually write new coords
                newfile.write("Rect: " + str(nx1) + ","+ str(ny1) + " - " + str(nx2) +","+str(ny2) + " / 1024x768\n")


            except:
                
                newfile.write(line)
                pass

        else:
            #recreate file
            newfile.write(line)

    print (filename + " done")
    
    file.close()
    newfile.close()


targetbar_xmove = 450
targetbar_ymove = 975
targetbarGroupName = "TargetBar"
targetbarGroup = ["targetbar_buffs.ini","targetbar_frame_portrait.ini","targetbar_healthbar.ini", "targetbar_items.ini",
                  "targetbar_parbar.ini", "targetbar_stats.ini","visionslot_right.ini", "visionslot.ini"]

#change targetbar
for element in targetbarGroup:
    elementMove(element, targetbarGroupName, targetbar_xmove, targetbar_ymove)

teamframe_xmove = 300
teamframe_ymove = 695
teamframe_group_name = "Team"
#change teamframe
elementMove("teamframes.ini",teamframe_group_name, teamframe_xmove, teamframe_ymove)
