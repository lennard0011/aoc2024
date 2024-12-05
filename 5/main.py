import os


def get_rules_map(rules):
    rules_map = {}

    for rule in rules:
        [first, second] = rule.split("|")
        if second not in rules_map:
            rules_map[second] = []
        rules_map[second].append(first) 
    return rules_map


def procedure_fulfills_rules(procedure, rules_map):
    for index in range(len(procedure)):
        value = procedure[index]
        if value not in rules_map:
            continue
        prereqs = rules_map[value]
        for prereq in prereqs:
            if prereq not in procedure:
                continue
            if prereq not in procedure[:index]:
                return False

    return True


def get_middle_value_of_procedure(procedure):
    length = len(procedure)
    index = int(length / 2)
    return int(procedure[index])

def sortOnOrder(e):
  return e['order']


def fix_procedure(procedure, rules_map):
    sub_rules_len = [{"value": value, "order": len([prereq for prereq in rules_map[value] if prereq in procedure])} for value in procedure]
    sub_rules_len.sort(key = sortOnOrder)
    return [element["value"] for element in sub_rules_len]
    


def main(part, filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename + ".txt")
    puzzle =  open(file_path, 'r').read().split('\n')
    
    split_index = puzzle.index("")
    rules = puzzle[:split_index]
    procedures = [procedure.split(",") for procedure in puzzle[split_index+1:]]

    score = 0

    rules_map = get_rules_map(rules)
    for procedure in procedures:
        if procedure_fulfills_rules(procedure, rules_map):
            if part == 1:
                score += get_middle_value_of_procedure(procedure)
        elif part == 2:
            fixed_procedure = fix_procedure(procedure, rules_map)
            score += get_middle_value_of_procedure(fixed_procedure)
        
    print(score)
   
main(2, "input")