GOALS_FILE_PATH = r"PutPathHere" #Change to your specific file path
GOALS_SHINE_FILE_PATH = r"PutPathHere" #Change to your specific file path

def main():
    print("Welcome to the Clichereich's Focus GFX Automator!")
    
    file_name = input("Please insert the .png file name: ")

    if not file_name.endswith(".png"): #This puts the .png in the end in case user forgot
        print("You did not insert .png to the end of the file name, inserting it for you.")
        file_name += ".png"

    fileChange(file_name) #call method

    print("Changes made successfully!")

def fileChange(file_name):
    no_png = file_name.removesuffix(".png") #This is needed so the GFX_goal string has no .png in the end

    new_content = f"""
        SpriteType = {{
            name = "GFX_goal_{no_png}"
            texturefile = "gfx/interface/goals/{file_name}"
        }}\n
    """

    with open(GOALS_FILE_PATH, "r") as file: #Read all the current contents and memorize
        lines = file.readlines()
    
    lines.insert(-1, new_content) #Add new line

    with open(GOALS_FILE_PATH, "w") as file: #Add old contents + new line
        file.writelines(lines)
    
    shine_content = f"""
    SpriteType = {{
        name = "GFX_goal_{no_png}_shine"
        texturefile = "gfx/interface/goals/{file_name}"			
        effectFile = "gfx/FX/buttonstate.lua"
        animation = {{
            animationmaskfile = "gfx/interface/goals/{file_name}"			
            animationtexturefile = "gfx/interface/goals/shine_overlay.dds" 	# <- the animated file
            animationrotation = -90.0		# -90 clockwise 90 counterclockwise(by default)
            animationlooping = no			# yes or no ;)
            animationtime = 0.75				# in seconds
            animationdelay = 0			# in seconds
            animationblendmode = "add"       #add, multiply, overlay
            animationtype = "scrolling"      #scrolling, rotating, pulsing
            animationrotationoffset = {{ x = 0.0 y = 0.0 }}
            animationtexturescale = {{ x = 1.0 y = 1.0 }} 
        }}

        animation = {{
            animationmaskfile = "gfx/interface/goals/{file_name}"			
            animationtexturefile = "gfx/interface/goals/shine_overlay.dds" 	# <- the animated file
            animationrotation = 90.0		# -90 clockwise 90 counterclockwise(by default)
            animationlooping = no			# yes or no ;)
            animationtime = 0.75				# in seconds
            animationdelay = 0			# in seconds
            animationblendmode = "add"       #add, multiply, overlay
            animationtype = "scrolling"      #scrolling, rotating, pulsing
            animationrotationoffset = {{ x = 0.0 y = 0.0 }}
            animationtexturescale = {{ x = 1.0 y = 1.0 }} 
        }}
        legacy_lazy_load = no
    }}\n
    """

    with open(GOALS_SHINE_FILE_PATH, "r") as file: #Read all the current contents and memorize
        lines_shine = file.readlines()
    
    lines_shine.insert(-1, shine_content) #Add new line

    with open(GOALS_SHINE_FILE_PATH, "w") as file: #Add old contents + new line
        file.writelines(lines_shine)
        
if __name__ == "__main__":
    main()