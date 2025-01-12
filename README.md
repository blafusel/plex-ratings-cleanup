# Plex Library User Ratings Management

This Python script allows you to manage user ratings for items in a Plex Media Server library. You can view, clear, or analyze user ratings and stats for your Plex libraries. You can also apply filters to only show or modify unwatched media.

## Features

- **Clear User Ratings**: Remove user ratings from items in a specific library or from all libraries.
- **Show User Ratings**: Display all user ratings for items in a specific library or from all libraries.
- **Library Stats**: Display stats for a specific library, such as the number of total files, rated files, and unrated files.
- **Filtering**: Apply filters to only process unwatched media files.

## Prerequisites

- **Plex Token**: See https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
- **Python 3.x**: This script requires Python 3.
- **plexapi**: Install the `plexapi` library to interact with your Plex server.

You can install the required dependencies using `pip`:

```bash
pip install plexapi