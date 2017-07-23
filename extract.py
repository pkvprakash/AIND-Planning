import re

problemPattern = re.compile("Solving(?P<problem>.*)using(?P<algorithm>.*)\.\.\.")
expansionPattern = re.compile("(?P<exp>\d+)\s+(?P<goal_tests>\d+)\s+(?P<new_nodes>\d+)\s+")
planPattern = re.compile("Plan length:\s+(?P<plan_length>\d+)\s+Time elapsed in seconds:\s+(?P<time_taken>\d+\.\d+)")

results = {}
with open("b.out") as infile:
    for line in infile:
        mo = problemPattern.search(line)
        if 'time_taken' in results:
            res = "{:10},{:45},{:10},{:10},{:10},{:10},{:25}".format(results['problem'], \
                                                      results['algorithm'],\
                                                      results['exp'], \
                                                      results['goal_tests'], \
                                                      results['new_nodes'], \
                                                      results['plan_length'], \
                                                      results['time_taken']
                                                     )
            print (res)
            results = {}
        
        if mo:
            results['problem'] = mo.group("problem")
            results['algorithm'] = mo.group("algorithm")
        else :
            mo = expansionPattern.search(line) 
            if mo:    
                results['exp'] = mo.group("exp")
                results['goal_tests'] = mo.group("goal_tests")
                results['new_nodes'] = mo.group("new_nodes")
            else:
                mo = planPattern.search(line)
                if mo:
                    results["plan_length"] = mo.group("plan_length")
                    results["time_taken"] = mo.group("time_taken")


