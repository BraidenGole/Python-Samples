"""
    [DESCRIPTION]: Python 3 Strong password generator.

    Examples of generated passwords:
        1. AD947n3wjfaweHaMkdmw
        2. O1o87ltor37zZcKS2GsK
        3. N9nQIYEgTKkXPUE91Dml
        4. EdUruGdcp3Cgse9PQaW9
        5. rqcOphesfemKKh0t66xN
"""

import random
import string

class PasswordGenerator:
    """
    Name        :   PasswordGenerator
    Purpose     :   This class will hold methods that will help
                    generate a very strong password.
    """

    def __init__(self, plain_text_pass):
        self.password = plain_text_pass

    def build_password(self):
        lower_case_alpha = string.ascii_lowercase
        upper_case_alpha = string.ascii_uppercase
        digits = string.digits

        self.password += lower_case_alpha
        self.password += upper_case_alpha
        self.password += digits

    def scramble_password(self):
        index = 0
        new_password = []
        for i in range(len(self.password)):
            index = random.randrange(0, len(self.password))
            new_password.append(self.password[index])
        return new_password

    @staticmethod
    def format_password(password):
        new_password = ""
        for letters in password:
            new_password += letters
        return new_password


if __name__ == "__main__":

    _word_to_scramble = "Braiden"
    generator = PasswordGenerator(_word_to_scramble)
    built_password = generator.build_password()
    scramble_password = generator.scramble_password()
    generated_password = generator.format_password(scramble_password)

    length_of_generated_password = len(generated_password)
    if length_of_generated_password > 20:
        generated_password = generated_password[0:20]

    print("\n -- Generated password --")
    print("\t" + generated_password)