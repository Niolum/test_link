from urllib.parse import quote

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()


class LinkBase(BaseModel):
    link: str


class LinkDecode(LinkBase):
    pass


class LinkEncode(LinkBase):
    pass

@app.post("/link", response_model=LinkEncode)
async def encode_link(link: LinkDecode):
    link = link.link
    encode_link = quote(link, safe="")
    data = {"link": encode_link}
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)