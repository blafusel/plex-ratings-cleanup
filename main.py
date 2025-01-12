import argparse
from plexapi.server import PlexServer

# Plex server connection details
PLEX_URL = 'YOUR_PLEX_SERVER_IP'  # Replace with your Plex server's IP and port
PLEX_TOKEN = 'YOUR_PLEX_TOKEN'    # See https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/

def clear_user_ratings(library_name=None, filter_type=None):
    try:
        # Connect to the Plex server
        plex = PlexServer(PLEX_URL, PLEX_TOKEN)
        print("Connected to Plex server:", plex.friendlyName)

        # Get the specified library or all libraries
        libraries = plex.library.sections()
        if library_name:
            library = next((lib for lib in libraries if lib.title.lower() == library_name.lower()), None)
            if not library:
                print(f"Library '{library_name}' not found.")
                return
            libraries = [library]

        # Iterate over the specified library or all libraries
        for library in libraries:
            print(f"Processing library: {library.title}")
            # Get all items in the library with an optional filter
            items = library.all()
            if filter_type == "unwatched":
                items = [item for item in items if not item.isPlayed]

            # Iterate over each item
            for item in items:
                # Check if the item has a user rating
                if item.userRating:
                    print(f"Clearing rating for: {item.title} (Current Rating: {item.userRating})")
                    item.rate(None)  # Clear the user rating
                    item.reload()  # Refresh item to confirm changes
        print("All user ratings have been cleared.")
    except Exception as e:
        print("An error occurred:", e)

def show_user_ratings(library_name=None, filter_type=None):
    try:
        # Connect to the Plex server
        plex = PlexServer(PLEX_URL, PLEX_TOKEN)
        print("Connected to Plex server:", plex.friendlyName)

        # Get the specified library or all libraries
        libraries = plex.library.sections()
        if library_name:
            library = next((lib for lib in libraries if lib.title.lower() == library_name.lower()), None)
            if not library:
                print(f"Library '{library_name}' not found.")
                return
            libraries = [library]

        # Iterate over the specified library or all libraries
        for library in libraries:
            print(f"Showing user ratings for library: {library.title}")
            # Get all items in the library with an optional filter
            items = library.all()
            if filter_type == "unwatched":
                items = [item for item in items if not item.isPlayed]

            # Display items with user ratings
            for item in items:
                if item.userRating:
                    print(f"{item.title}: User Rating = {item.userRating}")
    except Exception as e:
        print("An error occurred:", e)

def show_library_stats(library_name=None, filter_type=None):
    try:
        # Connect to the Plex server
        plex = PlexServer(PLEX_URL, PLEX_TOKEN)
        print("Connected to Plex server:", plex.friendlyName)

        # Get the specified library or all libraries
        libraries = plex.library.sections()
        if library_name:
            library = next((lib for lib in libraries if lib.title.lower() == library_name.lower()), None)
            if not library:
                print(f"Library '{library_name}' not found.")
                return
            libraries = [library]

        # Iterate over the specified library or all libraries
        for library in libraries:
            print(f"Calculating stats for library: {library.title}")
            # Get all items in the library with an optional filter
            items = library.all()
            if filter_type == "unwatched":
                items = [item for item in items if not item.isPlayed]

            # Calculate stats
            total_files = len(items)
            rated_files = sum(1 for item in items if item.userRating)
            unrated_files = total_files - rated_files

            # Display stats
            print(f"Total files: {total_files}")
            print(f"Rated files: {rated_files}")
            print(f"Unrated files: {unrated_files}")
    except Exception as e:
        print("An error occurred:", e)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Clear, view, or analyze user ratings from a Plex Media Server library.")
    parser.add_argument(
        "-l", "--library",
        type=str,
        help="Specify the name of the Plex library to process. If not provided, all libraries will be processed."
    )
    parser.add_argument(
        "--clear", 
        action="store_true", 
        help="Clear all user ratings from the specified library or all libraries."
    )
    parser.add_argument(
        "--showratings", 
        action="store_true", 
        help="Show all user ratings for items in the specified library or all libraries."
    )
    parser.add_argument(
        "--stats", 
        action="store_true", 
        help="Show stats (number of files, rated files, unrated files) for the specified library or all libraries."
    )
    parser.add_argument(
        "--filter", 
        type=str, 
        choices=["unwatched"],
        help="Apply a filter to the results. Currently supported: 'unwatched' (only show unwatched media files)."
    )

    # Parse arguments
    args = parser.parse_args()

    # Show help if no arguments are provided
    if not any(vars(args).values()):
        parser.print_help()
        return

    # Decide action based on the arguments
    filter_type = args.filter
    if args.clear:
        clear_user_ratings(library_name=args.library, filter_type=filter_type)
    elif args.showratings:
        show_user_ratings(library_name=args.library, filter_type=filter_type)
    elif args.stats:
        show_library_stats(library_name=args.library, filter_type=filter_type)

if __name__ == "__main__":
    main()
