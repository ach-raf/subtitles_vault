from typing import List, Optional, Union
from pydantic import BaseModel, Field


class Uploader(BaseModel):
    uploader_id: int
    name: str
    rank: str


class FeatureDetails(BaseModel):
    feature_id: int
    feature_type: str
    year: int
    title: str
    movie_name: str
    imdb_id: int
    tmdb_id: int
    season_number: int
    episode_number: int
    parent_imdb_id: int
    parent_title: str
    parent_tmdb_id: int
    parent_feature_id: int


class RelatedLink(BaseModel):
    label: str
    url: str
    img_url: Optional[str] = None


class File(BaseModel):
    file_id: int
    cd_number: int
    file_name: str


class Attributes(BaseModel):
    subtitle_id: str
    language: str
    download_count: int
    new_download_count: int
    hearing_impaired: bool
    hd: bool
    fps: float
    votes: int
    ratings: float
    from_trusted: bool
    foreign_parts_only: bool
    upload_date: str
    ai_translated: bool
    nb_cd: int
    machine_translated: bool
    release: str
    comments: str
    legacy_subtitle_id: int
    legacy_uploader_id: int
    uploader: Uploader
    feature_details: FeatureDetails
    url: str
    related_links: List[RelatedLink]
    files: List[File]
    moviehash_match: bool


class Subtitle(BaseModel):
    id: str
    type: str
    attributes: Attributes
