class Password:

    def __init__(self, pw):
        self.pw_split = pw.split(' ')
        self.pw_string = ''
        self.policy_min = 0
        self.policy_max = 0
        self.policy_key = ''

        self.get_data()

    def get_data(self):
        policy_min_max = self.pw_split[0].split('-')
        self.policy_min = int(policy_min_max[0])
        self.policy_max = int(policy_min_max[1])

        self.policy_key = self.pw_split[1][0]
        self.pw_string = self.pw_split[2]

    def check_password_sled(self):
        if self.policy_min <= self.pw_string.count(self.policy_key) <= self.policy_max:
            return True
        else:
            return False

    def check_password_toboggan(self):
        if self.pw_string[(self.policy_min - 1)] == self.policy_key:

            if self.pw_string[(self.policy_max - 1)] == self.policy_key:
                return False
            else:
                return True
        else:
            if self.pw_string[(self.policy_max - 1)] == self.policy_key:
                return True
            else:
                return False


def get_passwords(file):
    with open(file) as password_file:
        passwords = password_file.readlines()

    return passwords


def check_passwords():
    file = "input.txt"
    valid_password_count = 0
    passwords = get_passwords(file)
    for password in passwords:
        current_password = Password(password.strip())
        password_check = current_password.check_password_toboggan()
        if password_check:
            valid_password_count += 1

    print(valid_password_count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_passwords()
