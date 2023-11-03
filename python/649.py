class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if len(senate) == 1:
            return "Radiant" if senate == "R" else "Dire"
        if senate.count(senate[0]) == len(senate):
            return "Radiant" if senate[0] == "R" else "Dire"
        can_vote = senate
        for i in range(len(can_vote)):
            if senate[i] == "D":
                if can_vote.find("R") != -1:
                    print("removing rad")
                    can_vote = can_vote.replace("R", "X", 1)
                    print(can_vote)
                    if can_vote.find("R") == -1:
                        return "Dire"
            elif senate[i] == "R":
                if can_vote.find("D") != -1:
                    print("removing dire")
                    can_vote = can_vote.replace("D", "X", 1)
                    print(can_vote)
                    if can_vote.find("D") == -1:
                        return "Radiant"


print(Solution.predictPartyVictory(None, "DDRRR"))
