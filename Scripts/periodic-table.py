import requests

url = "https://elements-table-api.herokuapp.com/"


def get_data_by_name(name: str) -> str:
    """
    Function get data from api by name of elements
    """
    
    return requests.get(url + "name/" + name).json()


def get_data_by_number(num: str) -> str:
    """
    Function get data from api by atomic number of elements
    """
    
    return requests.get(url + num).json()


if __name__ == "__main__":
    a = input("Enter the Name/Atomic number of elements: ")
    if a.isdigit():
        data = get_data_by_number(a)[0]
    else:
        data = get_data_by_name(a)[0]

    for i in data:
        print(f"{i}: {data[i]}")
