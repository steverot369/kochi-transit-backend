from pydantic import BaseModel


class StopResponse(
    BaseModel
):

    id: int

    uuid: str

    stop_code: str

    stop_name: str

    latitude: float | None

    longitude: float | None

    transport_mode: str

    class Config:

        from_attributes = True