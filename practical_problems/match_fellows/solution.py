# Approach 2
def canMatchFellows(skillMap: dict) -> bool:
    skill_freq_map = {}
    
    for skill in skillMap.values():
        if skill not in skill_freq_map:
            skill_freq_map[skill] = 1
        else:
            skill_freq_map[skill] +=1
            
    
    for skill in skill_freq_map.values():
        if skill%2 != 0:
            return False
        
    return True
            

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) == True)

skillMap = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5, "paavo" : 1}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3, "tobey": 3}
print(canMatchFellows(skillMap) == True)

print(canMatchFellows({"oliver": 1}) == False)

print(canMatchFellows({}) == True)