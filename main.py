#!/usr/bin/python
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from prompts import generate_description
from prompts import generate_description1,generate_description_fine_tune
from models.property_types import (
    ResidentialListingData,
    LandListingData,
    OfficeSpaceListingData,
    CommercialListingData,
    PayingGuestListingData
)

from utils import logger
from fine_tune import request_body

app = FastAPI(
    title="Minite GPT3",
    description="Generates description for real estate listings from the listing parameters",
    version="2.0.0"
)


@app.get("/")
async def root():
    return "Hello World!!!"

@app.post('/payingguest_descriptions')
async def generate_payingguest_description(payingguest_listing_data: PayingGuestListingData, format: bool = False):
    """
    Generates descriptions for residential property types
    """
    return await generate_description(payingguest_listing_data, format=format)

'''
@app.post('/residential_descriptions')
async def generate_apartment_description(residential_listing_data: ResidentialListingData, format: bool = False):
    """
    Generates descriptions for residential property types
    """
    return await generate_description(residential_listing_data, format=format)


@app.post('/land_descriptions')
async def land_description(land_listing_data: LandListingData, format: bool = False):
    """
    Generates descriptions for land property types
    """
    return await generate_description(land_listing_data, format=format)


@app.post('/office_space_descriptions')
async def office_space_description(office_space_data: OfficeSpaceListingData, format: bool = False):
    """
    Generates descriptions for office space property types
    """
    return await generate_description(office_space_data, format=format)


@app.post('/commercial_descriptions')
async def generate_land_description(commercial_listing_data: CommercialListingData, format: bool = False):
    """
    Generates descriptions for commercial property types
    """
    return await generate_description(commercial_listing_data, format=format)
'''
'''
@app.post('/residential_descriptions')
async def generate_apartment_description(residential_listing_data: ResidentialListingData, format: bool = False):
    """
    Generates descriptions for residential property types
    """
    
    if len(residential_listing_data.locality) and len(residential_listing_data.city) >= 2:
        return await generate_description(residential_listing_data, format=format)
    else:
        return("Error please fill city and locality")
'''

#fine tune model

@app.post("/residential_descriptions")
async def generate_apartment_des_finetune1(fine_tune_apartment: request_body, format: bool = False):
    """
    Generates descriptions for Apartment property types
    """
    if len(fine_tune_apartment.locality) and len(fine_tune_apartment.city) >= 2 and fine_tune_apartment.price != 0:
        return await generate_description_fine_tune(fine_tune_apartment, format = format)

    else:
        return("Error please fill city and locality and price") 

@app.post('/land_descriptions')
async def land_description(land_listing_data: LandListingData, format: bool = False):
    """
    Generates descriptions for land property types
    """
    
    if len(land_listing_data.locality) and len(land_listing_data.city) >= 2 and land_listing_data.price != 0:
        return await generate_description(land_listing_data, format=format)
    else:
        return("Error please fill city and locality")


@app.post('/office_space_descriptions')
async def office_space_description(office_space_data: OfficeSpaceListingData, format: bool = False):
    """
    Generates descriptions for office space property types
    """

    if len(office_space_data.locality) and len(office_space_data.city) >=2 and office_space_data.price != 0:
        return await generate_description(office_space_data, format=format)
    else:
        return("Error please fill city and locality")


@app.post('/commercial_descriptions')
async def generate_land_description(commercial_listing_data: CommercialListingData, format: bool = False):
    """
    Generates descriptions for commercial property types
    """   
    if len(commercial_listing_data.locality) and len(commercial_listing_data.city) >=2 and commercial_listing_data.price != 0:
        return await generate_description(commercial_listing_data, format=format)
    else:
        return("Error please fill city and locality")
        
        
#for dubai

@app.post('/residential_descriptions_dubai')
async def generate_apartment_description_dubai(residential_listing_data: ResidentialListingData, format: bool = False):
    """
    Generates descriptions for residential property types
    """

    if len(residential_listing_data.locality) and len(residential_listing_data.city) >= 2 and residential_listing_data.price != 0:
        return await generate_description1(residential_listing_data, format=format)
    else:
        return("Error please fill city and locality")


@app.post('/land_descriptions_dubai')
async def land_description_dubai(land_listing_data: LandListingData, format: bool = False):
    """
    Generates descriptions for land property types
    """
    if len(land_listing_data.locality) and len(land_listing_data.city) >= 2 and land_listing_data.price != 0:
        return await generate_description1(land_listing_data, format=format)
    else:
        return("Error please fill city and locality")

    


@app.post('/office_space_descriptions_dubai')
async def office_space_description_dubai(office_space_data: OfficeSpaceListingData, format: bool = False):
    """
    Generates descriptions for office space property types
    """
    if len(office_space_data.locality) and len(office_space_data.city) >=2 and office_space_data.price != 0:
        return await generate_description1(office_space_data, format=format)
    else:
        return("Error please fill city and locality")

    


@app.post('/commercial_descriptions_dubai')
async def generate_land_description_dubai(commercial_listing_data: CommercialListingData, format: bool = False):
    """
    Generates descriptions for commercial property types
    """
    if len(commercial_listing_data.locality) and len(commercial_listing_data.city) >=2 and commercial_listing_data.price != 0:
        return await generate_description1(commercial_listing_data, format=format)
    else:
        return("Error please fill city and locality")
    



@app.get('/access_logs')
async def get_gunicorn_access_logs():
    path = os.path.join(os.getcwd(), 'gunicorn-access.log')
    log_path = os.environ.get("ACCESS_LOGFILE", path)
    data = ""
    try:
        with open(log_path, 'r') as f:
            data += "<ul>"
            for s in f.readlines():
                data += "<li>" + str(s) + "</li>"
            data += "</ul>"

    except:
        pass
    return HTMLResponse(content=data)

@app.get('/error_logs')
async def get_gunicorn_error_logs():
    path = os.path.join(os.getcwd(), 'gunicorn-error.log')
    log_path = os.environ.get("ERROR_LOGFILE", path)
    data = ""
    try:
        with open(log_path, 'r') as f:
            data += "<ul>"
            for s in f.readlines():
                data += "<li>" + str(s) + "</li>"
            data += "</ul>"
    except:
        pass
    return HTMLResponse(content=data)
