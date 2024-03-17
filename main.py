import Login
import Register


def main():
    user = input("""
    1. Login
    2. Register
        >>> """)

    if user == "1":
        return Login.login()
    if user == "2":
        return Register.register_user()
    else:
        print("Invalid")
        return main()


if __name__ == "__main__":
    main()