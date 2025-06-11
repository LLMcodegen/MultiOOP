
class NTM:
    def __init__(self, req_skills):
        self.req_skills = req_skills
class SN_NTM(NTM):
    def __init__(self, req_skills, people):
        super().__init__(req_skills)
        self.people = people
    def necessary_team(self):
        req_skills = self.req_skills
        people = self.people
        n = len(req_skills)
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        people_skills = []
        for person in people:
            skill_mask = 0
            for skill in person:
                if skill in skill_index:
                    skill_mask |= 1 << skill_index[skill]
            people_skills.append(skill_mask)
        dp = {0: []}
        for i, person_skill in enumerate(people_skills):
            if person_skill == 0:
                continue
            new_dp = dp.copy()
            for skill_set, team in dp.items():
                new_skill_set = skill_set | person_skill
                if new_skill_set == skill_set:
                    continue
                if new_skill_set not in new_dp or len(new_dp[new_skill_set]) > len(team) + 1:
                    new_dp[new_skill_set] = team + [i]
            dp = new_dp
        full_skill_set = (1 << n) - 1
        return dp[full_skill_set]

#--------------:
print(SN_NTM(["python", "c++", "sql"], [["python", "c++", "sql"]]).necessary_team() == [0])
print(SN_NTM(["python", "c++", "sql"], [["python", "c++"], ["python", "sql"], ["c++", "sql"]]).necessary_team() == [0, 1])
print(SN_NTM(["python", "c++", "sql"], [["python", "c++"], ["python", "sql"], ["c++", "sql"], ["python", "c++", "sql"]]).necessary_team() == [3])
