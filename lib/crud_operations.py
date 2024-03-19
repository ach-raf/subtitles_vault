from typing import List, Optional
from sqlalchemy.orm import Session
from lib.db_utils import DatabaseManager
from lib.models import Attributes, Subtitle
from lib.database_models import SubtitleModel, AttributesModel


def map_attributes(attributes: Attributes, db: Session) -> AttributesModel:
    return AttributesModel(attributes, db)


def map_subtitle(subtitle: Subtitle, db: Session) -> SubtitleModel:
    attributes_model = map_attributes(subtitle.attributes, db)
    return SubtitleModel(
        id=subtitle.id,
        type=subtitle.type,
        attributes=attributes_model,
        moviehash_match=subtitle.attributes.moviehash_match,
    )


def create_subtitle(subtitle: Subtitle, db: Session):
    db_subtitle = map_subtitle(subtitle, db)
    db.add(db_subtitle)
    db.commit()
    db.refresh(db_subtitle)
    return db_subtitle


def get_subtitle(subtitle_id: str, db: Session) -> Optional[SubtitleModel]:
    return db.query(SubtitleModel).filter(SubtitleModel.id == subtitle_id).first()


def update_subtitle(
    subtitle_id: str, updated_subtitle: Subtitle, db: Session
) -> Optional[SubtitleModel]:
    db_subtitle = get_subtitle(subtitle_id, db)
    if db_subtitle:
        updated_db_subtitle = map_subtitle(updated_subtitle, db)
        db_subtitle.type = updated_db_subtitle.type
        db_subtitle.attributes = updated_db_subtitle.attributes
        db_subtitle.moviehash_match = updated_db_subtitle.moviehash_match
        db.commit()
        db.refresh(db_subtitle)
    return db_subtitle


def delete_subtitle(subtitle_id: str, db: Session):
    db_subtitle = get_subtitle(subtitle_id, db)
    if db_subtitle:
        db.delete(db_subtitle)
        db.commit()


def get_all_subtitles(db: Session) -> List[SubtitleModel]:
    return db.query(SubtitleModel).all()


if __name__ == "__main__":
    print("this is the crud_operations module")
