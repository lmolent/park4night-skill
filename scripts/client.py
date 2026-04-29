import requests
from typing import List, Optional
from models import Place, Review

class Park4nightClient:
    BASE_URL = "https://guest.park4night.com/services/V4.1"

    def get_places_by_coords(self, latitude: float, longitude: float) -> List[Place]:
        """
        Fetches places from GPS coordinates.
        """
        endpoint = f"{self.BASE_URL}/lieuxGetFilter.php"
        params = {"latitude": latitude, "longitude": longitude}
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        
        # The API returns a dict with a 'lieux' key containing the list
        if isinstance(data, dict) and "lieux" in data:
            return [Place(**p) for p in data["lieux"]]
        elif isinstance(data, list):
            return [Place(**p) for p in data]
        else:
            return []

    def get_reviews(self, place_id: str) -> List[Review]:
        """
        Fetches reviews for a specific place ID.
        """
        endpoint = f"{self.BASE_URL}/commGet.php"
        params = {"lieu_id": place_id}
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        
        # The API returns a dict with a 'commentaires' key
        if isinstance(data, dict):
            if "commentaires" in data and isinstance(data["commentaires"], list):
                return [Review(**r) for r in data["commentaires"]]
            # Fallback if the dict itself contains review-like fields
            elif "id" in data and "commentaire" in data:
                return [Review(**data)]
        
        if isinstance(data, list):
            return [Review(**r) for r in data]
            
        return []

    def get_user_places(self, username: str) -> List[Place]:
        """
        Get places created by a user.
        """
        endpoint = f"{self.BASE_URL}/lieuGetUser.php"
        params = {"uuid": username}
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, dict) and "lieux" in data:
            return [Place(**p) for p in data["lieux"]]
        return [Place(**p) for p in data] if isinstance(data, list) else []

    def get_user_reviewed_places(self, user_id: str) -> List[Place]:
        """
        Get places reviewed by a user.
        """
        endpoint = f"{self.BASE_URL}/lieuGetCommUser.php"
        params = {"user_id": user_id}
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, dict) and "lieux" in data:
            return [Place(**p) for p in data["lieux"]]
        return [Place(**p) for p in data] if isinstance(data, list) else []

if __name__ == "__main__":
    client = Park4nightClient()
    print("Testing client...")
    try:
        places = client.get_places_by_coords(42.3383, 9.5367)
        print(f"Fetched {len(places)} places successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
