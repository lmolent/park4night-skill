import argparse
from client import Park4nightClient

# Mapping of place codes to their descriptive name and icon
PLACE_INFO = {
    "P": ("Parking", "🅿️"),
    "PJ": ("Day Parking Only", "☀️"),
    "C": ("Campsite", "⛺"),
    "AC": ("Motorhome Area", "🚐"),
    "OR": ("Nature Spot (Wild)", "🌲"),
    "DS": ("Service Point", "💧"),
    "PH": ("Private Host", "🏠"),
    "F": ("Farm", "🚜"),
    "Fp": ("France Passion (Farm)", "🍇"),
}

def display_place(place):
    name = place.name if place.name else "Unnamed Spot"
    info = PLACE_INFO.get(place.code, (f"Unknown ({place.code})", "❓"))
    type_name, icon = info
    
    print(f"\n{icon} {name} ({place.ville}, {place.pays})")
    print(f"   Type: {type_name}")
    print(f"   ID: {place.id}")
    print(f"   Rating: {place.note_moyenne or 'N/A'}/5 ⭐ | Reviews: {place.nb_commentaires or '0'}")
    print(f"   Amenities: Water: {'✅' if place.point_eau == '1' else '❌'}, "
          f"Power: {'✅' if place.electricite == '1' else '❌'}, "
          f"WiFi: {'✅' if place.wifi == '1' else '❌'}")
    if place.site_internet:
        print(f"   Web: {place.site_internet}")

def main():
    parser = argparse.ArgumentParser(description="Explore Park4night spots near a location.")
    parser.add_argument("lat", type=float, help="Latitude of the center point")
    parser.add_argument("lon", type=float, help="Longitude of the center point")
    # Generate type list for help message
    type_help = "Filter by location type code. Available types: " + ", ".join(
        [f"{k} ({v[0]})" for k, v in PLACE_INFO.items()]
    )
    
    parser.add_argument("--limit", type=int, default=5, help="Number of spots to display (default: 5)")
    parser.add_argument("--sort", choices=["rating", "reviews", "reviews-rating", "rating-reviews"], help="Sort results by rating or number of reviews")
    parser.add_argument("--type", help=type_help)
    parser.add_argument("--comments", type=int, default=0, help="Number of latest comments to show for each spot")
    
    args = parser.parse_args()
    
    client = Park4nightClient()
    
    print("=== Park4night Travel Explorer ===")
    print(f"Searching for spots near {args.lat}, {args.lon}...")
    
    try:
        places = client.get_places_by_coords(args.lat, args.lon)
        
        # Filtering logic
        if args.type:
            requested_type = args.type.upper()
            places = [p for p in places if p.code == requested_type]
            print(f"Filtered for type: {requested_type}")

        # Sorting logic
        if args.sort == "rating":
            places.sort(key=lambda x: float(x.note_moyenne) if x.note_moyenne else 0.0, reverse=True)
        elif args.sort == "reviews":
            places.sort(key=lambda x: int(x.nb_commentaires) if x.nb_commentaires else 0, reverse=True)
        elif args.sort == "reviews-rating":
            places.sort(key=lambda x: (int(x.nb_commentaires or 0), float(x.note_moyenne or 0.0)), reverse=True)
        elif args.sort == "rating-reviews":
            places.sort(key=lambda x: (float(x.note_moyenne or 0.0), int(x.nb_commentaires or 0)), reverse=True)

        print(f"Found {len(places)} locations nearby (showing top {args.limit}).\n")
        
        for i, place in enumerate(places[:args.limit]):
            print(f"{i+1}.", end="")
            display_place(place)
            
            # Show comments if requested
            if args.comments > 0:
                try:
                    reviews = client.get_reviews(place.id)
                    if reviews:
                        print(f"   Latest {min(len(reviews), args.comments)} reviews:")
                        for rev in reviews[:args.comments]:
                            print(f"     💬 {rev.uuid}: \"{rev.commentaire[:200]}...\"")
                except:
                    pass
        
    except Exception as e:
        print(f"Error exploring spots: {e}")

if __name__ == "__main__":
    main()
