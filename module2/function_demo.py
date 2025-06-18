# function_demo.py

# import pandas as pd


def get_large_arguments(
    argument1: float,
    argument2: int,
    *args,
    kwarg1: str = "large",
    **kwargs
) -> list:
    """
    Demonstrates the capabilities of a function in python by checking for
    which function arguments are over a certain value.

    Parameters
    ----------
    argument1 : float
        The first required argument of the function. It must be a float.
    arugment2 : int
        The second required argument of the function. It must be an integer.
    kwarg1: str, optional
        This is a keyword argument and a default is specified. Default is
        "large". The valid options for the kwarg are:

        - "large": sets the threshold value to 50
        - "very large": sets the threshold value to 100
        - "super large": sets the threshold value to 1000

    *args
        A list of non-keyword arguments of indefinite length. Any argument
        listed after the above specified parameters will be put here.
    **kwargs
        Similarly, any keyword argument that is not kwarg1 will be put here.

    Returns
    -------
    large_arguments: list
        A list of arguments over the threshold.
    """
    print(f"Argument 1 is: {argument1}")
    print(f"Argument 2 is: {argument2}")
    print(f"Keyword Argument 1 is: {kwarg1}")
    print(f"The remaining passed arguments are: {args}")
    print(f"The remaining passed keyword arguments are: {kwargs}")

    # Using kwarg1 to adjust the conditions of the function
    if kwarg1 == "large":
        threshold = 50
    elif kwarg1 == "very large":
        threshold = 100
    elif kwarg1 == "super large":
        threshold = 1000
    else:
        raise ValueError(f"{kwarg1} is an invalid option.")

    # Performing some operation using the arguments
    large_arguments = []
    for i in [argument1, argument2, *args]:
        if i > threshold:
            large_arguments.append(i)

    # Returning the result of the operation.
    return large_arguments


if __name__ == "__main__":
    import pandas as pd
    large_nums = get_large_arguments(
        150.7,
        4,
        13000,
        367,
        0.2,
        kwarg1="very large",
        kwarg2="my second keyword"
    )
    print(f"The large values are: {large_nums}")

    # Now, here is some code for opening a .csv file of geochemical data.
    file_name = "./module2/sample_geochemical_data.csv"

    df = pd.read_csv(file_name, delimiter=',')
    sio2_pct = df["SiO2_%_ME_XRF26"].to_numpy()
    sample_names = df["Sample"].to_list()
    sio2_fraction = sio2_pct/100
    rock_types = []
    for i in sio2_pct:
        if i > 70:
            rock_types.append("Rhyolite")
        elif 50 < i < 70:
            rock_types.append("Dacite")
        elif i < 50:
            rock_types.append("Basalt")

    # In just this short block of code, what, precisely is being done?
    # How many functions could this represent?
    # What would they be called?
    # Wrap the above code in as many functions as you see fit.
