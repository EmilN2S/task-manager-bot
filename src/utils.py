def priority_num_to_str(priority) -> str:
    if priority == True:
        return "Important"
    if priority == False:
        return "Simple"

def priority_str_to_num(priority) -> bool:
    if priority == "important":
        return True
    if priority == "simple":
        return False

def completed_num_to_str(completed) -> str:
    if completed == True:
        return "✅ Yes"
    if completed == False:
        return "❌ No"
