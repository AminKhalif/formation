def simulate_carousel(apps: list[str], commands: list[str]) -> list[str]:
    current_index = 0
    opened_apps = []
    max_index, min_index = len(apps) , -(len(apps) )
    
    for command in commands:
    
        #if we reach out of bounds then reset index
        if current_index > max_index or (current_index < min_index  ):
            current_index = 0

        if command == 'tap':
            opened_apps.append(apps[current_index]) 
            
        if command == 'scroll up':
            current_index +=1
        
        elif command == 'scroll down':
            current_index -=1
        
            
    
    return opened_apps

apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["tap", "scroll down", "scroll up", "scroll up", "scroll down", "scroll down", "tap"]
result = simulate_carousel(apps, commands)
print(result == ["Maps", "Settings"])

# Test Case 1: No commands
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = []
print(simulate_carousel(apps, commands) == [])

# Test Case 2: Single "tap" command
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["tap"]
print(simulate_carousel(apps, commands) == ["Maps"])

# Test Case 3: Single "scroll up" command
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["scroll up", "tap"]
print(simulate_carousel(apps, commands) == ["Music"])

# Test Case 4: Single "scroll down" command
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["scroll down", "tap"]
print(simulate_carousel(apps, commands) == ["Settings"])

# Test Case 5: Multiple "scroll up" and "scroll down" commands
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["scroll down", "scroll up", "scroll up", "scroll up", "scroll up", "tap"]
print(simulate_carousel(apps, commands) == ["Messages"])

# Test Case 6: Mix of "tap", "scroll up", and "scroll down" commands
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["tap", "scroll up", "tap", "scroll down", "tap", "scroll down", "tap"]
print(simulate_carousel(apps, commands) == ["Maps", "Music", "Maps", "Settings"])

# Test Case 7: Carousel with only one app
apps = ["Maps"]
commands = ["tap", "scroll up", "scroll down", "tap"]
print(simulate_carousel(apps, commands) == ["Maps", "Maps"])

# Test Case 8: Carousel with only one app & scroll spam
apps = ["Maps"]
commands = ["scroll up", "scroll up", "tap", "scroll up", "scroll up", "scroll up", "scroll up", "tap"]
print(simulate_carousel(apps, commands) == ["Maps", "Maps"])