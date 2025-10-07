import numpy as np


class Dog:
    """
    A simple class to represent a dog. This is a classic example.

    Parameters
    ----------
    name : str
        The name of the dog.
    age : int
        The age of the dog in years.

    Attributes
    ----------
    name : str
        The dog's name.
    age : int
        The dog's age.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        """
        Print a barking sound.

        Returns
        -------
        None
        """
        print(f"{self.name} says: Woof!")

    def have_birthday(self):
        """
        Increase the dog's age by one year.

        Returns
        -------
        None
        """
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age}.")


class LargeNumbers:
    """
    This class will demonstrate the very most basic functionality of python
    classes by splitting a list of numbers into small, large, very large and
    super large attributes. It aims to mirror our get_large_arguments function.

    Parameters
    ----------
    number_list : list
        A list of numbers to sort out.

    Attributes
    ----------
    small : list
        A list of small numbers (<50) from the `number_list`.
    large: list
        A list of large numbers (>50 and <100)
    very_large: list
        A list of VERY large numbers (>100 and <1000)
    super_large: list
        A list of SUPER LARGE numbers (>1000)
    """
    def __init__(self, number_list: list):
        self.small = []
        self.large = []
        self.very_large = []
        self.super_large = []
        for i in number_list:
            if i < 50:
                self.small.append(i)
            elif 50 < i < 100:
                self.large.append(i)
            elif 100 < i < 1000:
                self.very_large.append(i)
            else:
                self.super_large.append(i)

    def get_counts(self):
        """
        Gets the counts for each list attribute.

        Parameters
        ----------
        None

        Returns
        -------
        dict
            The keys to this dictionary are ["small", "large", "very_large",
            "super_large"]. The values for these keys are the list counts.
        """
        counts = {}
        counts["small"] = len(self.small)
        counts["large"] = len(self.large)
        counts["very_large"] = len(self.very_large)
        counts["super_large"] = len(self.super_large)

        print(counts)

        return counts


class MajorElementChemistry:
    """
    Tells about the major element geochemistry of a rock.

    Parameters
    ----------
    filepath: str

    Attributes
    ----------
    sio2 : float
        Amount of sio2 in the rock
    """
    def __init__(self, filepath):
        pass


if __name__ == "__main__":
    rng = np.random.default_rng()
    mynums = list(rng.uniform(0, 1200, 1000))
    large_nums_object = LargeNumbers(mynums)
    print(large_nums_object.small)
    counts = large_nums_object.get_counts()

    # Time to make a dog, hear it bark and celebrate its birthday!

    # Now, how would you turn the function we wrote to read geochemical data
    # into a class? Would it work better?
    # Under what situations are classes better than functions? Ask chatgpt lol
