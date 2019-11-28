def solution(record):

    id_nickname_pair = dict()
    who = []
    what = []
    for i in range(len(record)):
        r = record[i].split()
        if r[0] == "Enter":
            who.append(r[1])
            what.append("님이 들어왔습니다.")
            id_nickname_pair[r[1]] = r[2]
        elif r[0] == "Leave":
            who.append(r[1])
            what.append("님이 나갔습니다.")
        elif r[0] == "Change":
            id_nickname_pair[r[1]] = r[2]

    for i in range(len(who)):
        what[i] = id_nickname_pair[who[i]] + what[i]
    
    return what

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
solution(record)
