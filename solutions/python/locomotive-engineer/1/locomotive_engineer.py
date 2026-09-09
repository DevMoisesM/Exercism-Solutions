"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_ids):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    *list_wagons, = wagon_ids
    
    return list_wagons


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    first_id, second_id, id_one, *rest = each_wagons_id
    
    list_of_all_wagons = missing_wagons.copy()

    list_of_all_wagons.extend(rest)
    list_of_all_wagons.insert(0, id_one)
    list_of_all_wagons.append(first_id)
    list_of_all_wagons.append(second_id)
    
    return list_of_all_wagons


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    updated_route = route.copy()
    updated_route["stops"] = list(stops.values())

    return updated_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    extended_route_information = {**route, **more_route_information}

    return extended_route_information


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    
    *rows_of_wagons, = zip(*wagons_rows)

    list_rows_of_wagons = []

    for i in rows_of_wagons:
        list_rows_of_wagons.append(list(i))

    return list_rows_of_wagons
