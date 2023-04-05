class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:

def sort_by_length(routes: list):
    def get_route(route):
        return route.length
    
    return sorted(routes, key=get_route, reverse=True)

def sort_by_difficulty(routes: list):
    def get_difficulty(route):
        return ( route.grade, route.length)    
    return sorted(routes, key=get_difficulty, reverse=True)

