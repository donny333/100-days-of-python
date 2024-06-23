#Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title version of the name"""
    if f_name == "" or l_name == "":
        return "Please enter a valid input."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("doNNy", "donateLLo")
print(formated_string)