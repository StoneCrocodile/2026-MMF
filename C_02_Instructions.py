def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
     at the start and end"""


    print(f"{decoration * 3} {statement} {decoration * 3}")

def string_check(question, valid_answers=('yes', 'no'), num_letters= 1):
    """Checks that users enter the full word
     or the 'n' letter/s of a word from a list of valid responses"""

    if valid_answers is None:
        valid_answers = ['yes', 'no']
    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

        # check if it's the first letter
            elif response == item[ :num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")

# Main routine
payment_list = ('cash', 'credit')

want_instructions = string_check("Do you want to see the instructions? ")
print(f"You chose {want_instructions}")
pay_method = string_check(question="Payment method: ", payment_ans, num_letters=2)
