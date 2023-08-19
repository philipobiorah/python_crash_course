# This function checks a given schedule entry for an old date and, if 
# found, the function replaces it with a new date. 

def replace_date(schedule, old_date, new_date):
    # Check if the given "old_date" appears at the end of the given 
    # string variable "schedule". 
    if schedule.endswith(old_date):

        # If True, the body of the if-block will run. The variable "n" is
        # used to hold the slicing index position. The len() function
        # is used to measure the length of the string "new_date".
        p = len(old_date)

        # The "new_schedule" string holds the updated string with the 
        # old date replaced by the new date. The schedule[:-p] part of 
        # the code trims the "old_date" substring from "schedule" 
        # starting at the final index position (or right-side) counting
        # towards the left the same number of index positions as 
        # calculated from len(old_date). Then, the code schedule[-p:]
        # starts the indexing position at the slot where the first
        # character of the "old_date" used to be positioned. The 
        # .replace(old_date, new_date) code inserts the "new_date" into
        # the position where the "old_date" used to exist. 

        print("(schedule[:-p]".format(schedule[:-p]))


