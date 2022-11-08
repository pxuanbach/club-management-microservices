from typing import List
import cloudinary
import cloudinary.uploader
import cloudinary.api
from fastapi import UploadFile

from config import settings


cloudinary.config(
    cloud_name = settings.CLOUDINARY_NAME, 
    api_key = settings.CLOUDINARY_API_KEY, 
    api_secret = settings.CLOUDINARY_API_SECRET,
)


async def upload_file(file: UploadFile):
    result = cloudinary.uploader.upload(file.file)
    print(result)
    return result.get("url")