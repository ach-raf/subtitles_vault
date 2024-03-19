from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float, DateTime
from sqlalchemy.orm import relationship, Session
from lib.db_utils import DatabaseManager
from lib.models import Uploader, Attributes
import datetime

Base = DatabaseManager().get_base()


class UploaderModel(Base):
    __tablename__ = "uploaders"

    uploader_id = Column(Integer, primary_key=True)
    name = Column(String)
    rank = Column(String)

    def __init__(self, uploader: Uploader):
        self.uploader_id = uploader.uploader_id
        self.name = uploader.name
        self.rank = uploader.rank


class FeatureDetailsModel(Base):
    __tablename__ = "feature_details"

    feature_id = Column(Integer, primary_key=True)
    feature_type = Column(String)
    year = Column(Integer)
    title = Column(String)
    movie_name = Column(String)
    imdb_id = Column(Integer)
    tmdb_id = Column(Integer)
    season_number = Column(Integer)
    episode_number = Column(Integer)
    parent_imdb_id = Column(Integer)
    parent_title = Column(String)
    parent_tmdb_id = Column(Integer)
    parent_feature_id = Column(Integer)

    def __init__(
        self,
        feature_id,
        feature_type,
        year,
        title,
        movie_name,
        imdb_id,
        tmdb_id,
        season_number,
        episode_number,
        parent_imdb_id,
        parent_title,
        parent_tmdb_id,
        parent_feature_id,
    ):
        self.feature_id = feature_id
        self.feature_type = feature_type
        self.year = year
        self.title = title
        self.movie_name = movie_name
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id
        self.season_number = season_number
        self.episode_number = episode_number
        self.parent_imdb_id = parent_imdb_id
        self.parent_title = parent_title
        self.parent_tmdb_id = parent_tmdb_id
        self.parent_feature_id = parent_feature_id


class RelatedLinkModel(Base):
    __tablename__ = "related_links"

    id = Column(Integer, primary_key=True)
    label = Column(String)
    url = Column(String)
    img_url = Column(String)
    subtitle_id = Column(Integer, ForeignKey("subtitles.id"))

    def __init__(self, label, url, img_url=None):
        self.label = label
        self.url = url
        self.img_url = img_url


class FileModel(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    file_id = Column(Integer)
    cd_number = Column(Integer)
    file_name = Column(String)
    subtitle_id = Column(Integer, ForeignKey("subtitles.id"))

    def __init__(self, file_id, cd_number, file_name):
        self.file_id = file_id
        self.cd_number = cd_number
        self.file_name = file_name


class AttributesModel(Base):
    __tablename__ = "attributes"

    id = Column(Integer, primary_key=True)
    subtitle_id = Column(String)
    language = Column(String)
    download_count = Column(Integer)
    new_download_count = Column(Integer)
    hearing_impaired = Column(Boolean)
    hd = Column(Boolean)
    fps = Column(Float)
    votes = Column(Integer)
    ratings = Column(Float)
    from_trusted = Column(Boolean)
    foreign_parts_only = Column(Boolean)
    upload_date = Column(DateTime)
    ai_translated = Column(Boolean)
    nb_cd = Column(Integer)
    machine_translated = Column(Boolean)
    release = Column(String)
    comments = Column(String)
    legacy_subtitle_id = Column(Integer)
    legacy_uploader_id = Column(Integer)
    uploader_id = Column(Integer, ForeignKey("uploaders.uploader_id"))
    feature_details_id = Column(Integer, ForeignKey("feature_details.feature_id"))
    url = Column(String)

    uploader = relationship("UploaderModel", backref="attributes")
    feature_details = relationship("FeatureDetailsModel", backref="attributes")

    def __init__(self, attributes: Attributes, db: Session):
        self.subtitle_id = attributes.subtitle_id
        self.language = attributes.language
        self.download_count = attributes.download_count
        self.new_download_count = attributes.new_download_count
        self.hearing_impaired = attributes.hearing_impaired
        self.hd = attributes.hd
        self.fps = attributes.fps
        self.votes = attributes.votes
        self.ratings = attributes.ratings
        self.from_trusted = attributes.from_trusted
        self.foreign_parts_only = attributes.foreign_parts_only
        self.upload_date = datetime.datetime.strptime(
            attributes.upload_date, "%Y-%m-%dT%H:%M:%SZ"
        )

        self.ai_translated = attributes.ai_translated
        self.nb_cd = attributes.nb_cd
        self.machine_translated = attributes.machine_translated
        self.release = attributes.release
        self.comments = attributes.comments
        self.legacy_subtitle_id = attributes.legacy_subtitle_id
        self.legacy_uploader_id = attributes.legacy_uploader_id
        self.uploader = UploaderModel(attributes.uploader)
        self.feature_details = FeatureDetailsModel(
            feature_id=attributes.feature_details.feature_id,
            feature_type=attributes.feature_details.feature_type,
            year=attributes.feature_details.year,
            title=attributes.feature_details.title,
            movie_name=attributes.feature_details.movie_name,
            imdb_id=attributes.feature_details.imdb_id,
            tmdb_id=attributes.feature_details.tmdb_id,
            season_number=attributes.feature_details.season_number,
            episode_number=attributes.feature_details.episode_number,
            parent_imdb_id=attributes.feature_details.parent_imdb_id,
            parent_title=attributes.feature_details.parent_title,
            parent_tmdb_id=attributes.feature_details.parent_tmdb_id,
            parent_feature_id=attributes.feature_details.parent_feature_id,
        )
        self.url = attributes.url
        self.related_links = [
            RelatedLinkModel(link.label, link.url, link.img_url)
            for link in attributes.related_links
        ]
        self.files = [
            FileModel(file.file_id, file.cd_number, file.file_name)
            for file in attributes.files
        ]


class SubtitleModel(Base):
    __tablename__ = "subtitles"

    id = Column(String, primary_key=True)
    type = Column(String)
    attributes_id = Column(Integer, ForeignKey("attributes.id"))

    attributes = relationship("AttributesModel", backref="subtitle")
    related_links = relationship("RelatedLinkModel", backref="subtitle")
    files = relationship("FileModel", backref="subtitle")
    moviehash_match = Column(Boolean)


if __name__ == "__main__":
    print("this is the database_models module")
