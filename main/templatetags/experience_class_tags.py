from django import template

register = template.Library()

# This Template tag is specifically used only for objects in the Experience class in models.py.
# It cannot be used by any other class or anywhere else.
# A template tag for this class is necessary because Django cannot pass dictionary keys or function parameters
# to html templates

@register.filter(name = "dict_parser")
def dict_parser(date_dictionary, key):
    """
        A Function that is used to parse the date_parser method in Experience class and
        return the value of the key specified: any one of these options: {'start_month',
        'start_year', 'end_month', 'end_year'}

        Parameters:
        -----------
            date_dictionary: dict
                The dictionary that was returned from the date_parser method in the Experience class

            key: str
                The actual key that refers to the date value in the date_dictionary that I want to return
    """
    return date_dictionary[key]

@register.filter(name = "list_preprocessor")
def list_preprocessor(experience_object, section):
    """
    A Function that converts each experience's section that contains an ordered list (Tasks, Results) input to
    a readable output that the user can see in the view, and returns a list with unecessary bullet points removed, and only
    contains the essential content of that section

    Parameters:
    -----------
    experience_object: Experience
        An Experience object that was created from the class Experience in models.py

    section: str
        Values can only be from {'Tasks', 'Results'}
    """
    # Code block to split the content of each section into a list containing each sentence as the elements
    if section.lower() == "tasks":
        ordered_list = experience_object.tasks.split('\r\n')
    else:
        ordered_list = experience_object.results.split('\r\n')

    # Code block to remove the unnecessary ordered list bullets (e.g: 1), 2), 3)) from each sentence
    for i in range(len(ordered_list)):
        ordered_list[i] = ordered_list[i][3:] # This only works if the input is in the form 1) Loren ipsum, and not 1)Loren ipsum
        if ordered_list[i][0] == " ": # This captures ordered list items more than 9)
            ordered_list[i] = ordered_list[i][1:]

    return ordered_list
