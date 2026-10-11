def priority_num_to_str(priority) -> str:
    if priority == 1:
        return "Important"
    if priority == 0:
        return "Simple"

def priority_str_to_num(priority) -> int:
    if priority == "important":
        return 1
    if priority == "simple":
        return 0
