import json
from lib.models import Subtitle
from lib.db_utils import DatabaseManager
from lib.crud_operations import (
    create_subtitle,
    get_subtitle,
    update_subtitle,
    delete_subtitle,
    get_all_subtitles,
)

json_data = {
    "id": "6685273",
    "type": "subtitle",
    "attributes": {
        "subtitle_id": "6685273",
        "language": "en",
        "download_count": 21673,
        "new_download_count": 3145,
        "hearing_impaired": "false",
        "hd": "true",
        "fps": 23.976,
        "votes": 0,
        "ratings": 0.0,
        "from_trusted": "true",
        "foreign_parts_only": "false",
        "upload_date": "2022-08-12T03:58:57Z",
        "ai_translated": "false",
        "nb_cd": 1,
        "machine_translated": "false",
        "release": "For.All.Mankind.S03E10.1080p.WEB.H264-GGEZ",
        "comments": "HI Removed\nReleases. 1:22:35m\nFor.All.Mankind.S03E10.HDR.2160p.WEB.H265-GGEZ\nFor.All.Mankind.S03E10.2160p.WEB.H265-GLHF  \nFor.All.Mankind.S03E10.720p.WEB.H264-GGEZ \nFor.All.Mankind.S03E10.1080p.WEB.H264-GGEZ",
        "legacy_subtitle_id": 9203671,
        "legacy_uploader_id": 7650378,
        "uploader": {
            "uploader_id": 216980,
            "name": "oakislandtk",
            "rank": "Trusted member",
        },
        "feature_details": {
            "feature_id": 1266991,
            "feature_type": "Episode",
            "year": 2022,
            "title": "Stranger in a Strange Land",
            "movie_name": "For All Mankind - S03E10  Stranger in a Strange Land",
            "imdb_id": 14883254,
            "tmdb_id": 3658572,
            "season_number": 3,
            "episode_number": 10,
            "parent_imdb_id": 7772588,
            "parent_title": "For All Mankind",
            "parent_tmdb_id": 87917,
            "parent_feature_id": 1028805,
        },
        "url": "https://www.opensubtitles.com/en/subtitles/legacy/9203671",
        "related_links": [
            {
                "label": "All subtitles for Tv Show For All Mankind",
                "url": "https://www.opensubtitles.com/en/features/redirect/1028805",
                "img_url": "https://s9.opensubtitles.com/features/1/9/9/1266991.jpg",
            },
            {
                "label": "All subtitles for Episode stranger in a strange land",
                "url": "https://www.opensubtitles.com/en/features/redirect/1266991",
            },
        ],
        "files": [
            {
                "file_id": 7654627,
                "cd_number": 1,
                "file_name": "For.All.Mankind.S03E10.1080p.WEB.H264-GGEZ",
            }
        ],
        "moviehash_match": "true",
    },
}

# Unpack the JSON data into the Pydantic model
new_subtitle = Subtitle(**json_data)

session = DatabaseManager().get_session()
engine = DatabaseManager().get_engine()
base = DatabaseManager().get_base()

# Create the tables
base.metadata.create_all(engine)

create_subtitle(new_subtitle, session)

# Get a subtitle
subtitle = get_subtitle("6685273", session)
print(subtitle)


# Get all subtitles
all_subtitles = get_all_subtitles(session)

print(all_subtitles)
