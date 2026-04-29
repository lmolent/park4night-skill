from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional, Any

class Photo(BaseModel):
    id: str
    link_large: str
    link_thumb: str
    numero: str
    p4n_user_id: str
    pn_lieu_id: str

class Place(BaseModel):
    id: str
    latitude: str
    longitude: str
    titre: str
    name: Optional[str] = None
    description_fr: Optional[str] = ""
    description_en: Optional[str] = ""
    description_de: Optional[str] = ""
    description_es: Optional[str] = ""
    description_it: Optional[str] = ""
    description_nl: Optional[str] = ""
    date_creation: str
    ville: Optional[str] = ""
    code_postal: Optional[str] = ""
    pays: Optional[str] = ""
    pays_iso: Optional[str] = ""
    note_moyenne: Optional[str] = None
    nb_commentaires: Optional[str] = None
    nb_visites: Optional[str] = None
    nb_photos: Optional[str] = None
    site_internet: Optional[str] = None
    tel: Optional[str] = None
    mail: Optional[str] = None
    photos: List[Photo] = []
    
    # Amenities/Features
    point_eau: Optional[str] = "0"
    electricite: Optional[str] = "0"
    poubelle: Optional[str] = "0"
    douche: Optional[str] = "0"
    wifi: Optional[str] = "0"
    eau_noire: Optional[str] = "0"
    eau_usee: Optional[str] = "0"
    wc_public: Optional[str] = "0"
    
    # Distance and other metadata
    distance: Optional[str] = None
    code: Optional[str] = None
    
    # Catch-all for other fields we might not have explicitly mapped
    model_config = {"extra": "allow"}

class Review(BaseModel):
    id: str
    pn_lieu_id: str
    note: str
    commentaire: str
    user_id: str
    uuid: str
    date_creation: str
    type_vehicule: Optional[str] = "NC"
    
    model_config = {"extra": "allow"}
