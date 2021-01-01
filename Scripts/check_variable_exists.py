def check_variable_exists(variable: str) -> bool:
    """ Function check variable is exist or not """

    if variable in globals():
        return True
    
    elif variable in locals():
        return True

    return False
