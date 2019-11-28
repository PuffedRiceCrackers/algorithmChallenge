def isItValid(skill, skills):
    nextSkillIdx = 0
    for s in skill:
        if s in skills:
            if s == skills[nextSkillIdx]:
                nextSkillIdx += 1
            else:
                nextSkillIdx = -1
                break
    return nextSkillIdx == -1 and 0 or 1

def solution(skills, skill_trees):
    count = 0
    for skill in skill_trees:
        count += isItValid(skill, skills)
    return count       

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))