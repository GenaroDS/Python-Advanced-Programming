# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def get_seasons(show):
        return show['rating']
    
    return sorted(items, key=get_seasons, reverse=True)

