add_button = 10
from copy import *

class microwave_iteration:
    def __init__(self, val):
        if val >= add_button:
            self.best_scores = [len(str(val))]
            self.attempts = [list(str(val))]
            val -= add_button
            i=1
            while val>=0:
#                print(self.attempts)
                if val != 0:
                    self.attempts.append(["ADD"]*i + (microwave_iteration(val).best_path))
                    self.best_scores.append(i+microwave_iteration(val).best_try)
                else:
                    self.attempts.append(["ADD"]*i)
                    self.best_scores.append(i)
                i+=1
                val -= add_button
            self.best_try = min(self.best_scores)
            candidate_paths = []
            for attempt in range(len(self.attempts)):
                if self.best_scores[attempt]==self.best_try:
                    candidate_paths.append(self.attempts[attempt])
            if len(candidate_paths) != 0:
                self.best_path = get_best_path(candidate_paths)
            else:
                raise TypeError
        elif val == 0:
            raise(TypeError)
        else:
            self.best_try = len(str(val))
            self.best_path = list(str(val))

def get_best_path(val):
    candidates = []
    minval = min([len(x) for x in val])
    for x in val:
        if len(x) == minval:
            candidates.append(x)
    if len(candidates)>1:
        temp = copy.deepcopy(val)
        return ([10 if x=="ADD" else x for x in temp].sort())[0]
    else:
        return candidates[0]




if __name__ == '__main__':
    print(microwave_iteration(20).best_path)
