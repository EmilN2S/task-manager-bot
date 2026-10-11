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

def completed_num_to_str(completed) -> str:
    if completed == 1:
        return "✅ Yes"
    if completed == 0:
        return "❌ No"
