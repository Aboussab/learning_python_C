class SecurePlant:
    """
    A Plant class that uses encapsulation to protect its data.
    Direct access to height and age is discouraged;
    setters aresudo apt install flake8 used for validation.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

# ---------------GETTERS------------------
    def set_age(self, new_age: int) -> None:
        """
        Updates age only if the value is non-negative.
        """
        if (new_age >= 0):
            self.__age = new_age
        else:
            print("Invalid operation attempted: age", new_age, end="")
            print("days [REJECTED]")
            print("Security: Negative age rejected")

# ---------------SETTERS------------------
    def set_height(self, new_height: int) -> None:
        """
        Updates height only if the value is non-negative.
        """
        if (new_height >= 0):
            self.__height = new_height
        else:
            print("Invalid operation attempted: height", new_height, end="")
            print("days [REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self) -> int:
        """Returns the current height."""
        return (self.__height)

    def get_age(self) -> int:
        """Returns the current age."""
        return (self.__age)


if __name__ == "__main__":
    rose = SecurePlant("Rose", 25, 30)
    print("Plant created: ", rose.name)
    print("Height updated: ", rose.get_height())
    print(f"Age updated: {rose.get_age()} days")
    print("\n")
    rose.set_age(-22)
