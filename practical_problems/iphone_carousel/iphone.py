'''
❓ PROMPT
You are designing an iPhone carousel widget that displays a list of apps in a vertical scrolling carousel. The apps array contains the names of the apps in the carousel from bottom to the top (index 0 for the bottom). 
The commands array contains the list of commands to navigate the vertical carousel, in all lowercase: "scroll up", "scroll down", and "tap".

The carousel works as follows:
* Initially, the first app in the apps array is selected.
* If the user taps on an app, it opens the app.
* If the user scrolls up, the carousel moves one app up. If the user scrolls down, the carousel moves one app down.
* If the user scrolls past the top of the carousel, the carousel wraps around to the bottom, and vice versa.
* Your task is to simulate the behavior of the carousel and return an array of strings representing the names of the opened apps.

Assume with every subsequent command, the user is already back on the home page, scrolling through the carousel again.

Example(s)
let apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
let commands = ["tap", "scroll down", "scroll up", "scroll up", "scroll down", "scroll down", "tap"]

In this example, we first tap on "Maps" in the carousel (Index 0)
Scrolling down takes you to "Settings" (Index 4)
Scrolling up takes you back to "Maps" (Index 0)
Scrolling up takes you to "Music" (Index 1)
Scrolling down takes you to "Maps" (index 0)
Scrolling down again takes you to "Settings" (index 4)
Tap to open "Settings" (index 4)

Output: ["Maps", "Settings"]
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function simulateCarousel(apps, commands){} // returns list of str
def simulate_carousel(apps: list[str], commands: list[str]) -> list[str]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

scroll up => (current_index + 1)   {if current_index==max_index  current_index = max_index , current_index = 0}
scroll down => (current_index - 1) { if current_index==0 go to index[-1] }

carousel.tap() => (append value to array)

for command in commands:
    if command == 'scroll up':
        
        
Example(s)
let apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
let commands = ["tap", "scroll down", "scroll up", "scroll up", "scroll down", "scroll down", "tap"]
'''
'''
commands = ["scroll up", "scroll up", "tap", "scroll up", "scroll up", "scroll up", "scroll up", "tap"]
apps = ["Maps"]



'''
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