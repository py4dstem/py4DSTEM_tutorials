from typing_extensions import ParamSpecArgs
import requests 
from typing import Union
import pathlib
import argparse


def parser():

    parser = argparse.ArgumentParser()

    parser.add_argument("--dpc_nanotube", action='store_true')
    parser.add_argument("--make_probe_templates", action='store_true')

    args = parser.parse_args()

    return args


def download_file_from_google_drive(id_:str, 
                                    destination:Union[pathlib.PurePosixPath, pathlib.PureWindowsPath,str]) -> None:
    """
    Downloads a file from google drive to the destination file path
    Args:
        id_ (str): File ID for the desired file, string of letters and numbers e.g.
        for https://drive.google.com/file/d/1bHv3u61Cr-y_GkdWHrJGh1lw2VKmt3UM/
        id='1bHv3u61Cr-y_GkdWHrJGh1lw2VKmt3UM'
        destination (Union[pathlib.PurePosixPath, pathlib.PureWindowsPath,str]): path file will be downloaded
    """
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
    
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id_ }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id_, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

    return None


def __main__():

    args = parser()

    if args.dpc_nanotube:
        download_file_from_google_drive("1bHv3u61Cr-y_GkdWHrJGh1lw2VKmt3UM", "data/carbon_nanotube_data.h5")

    else:
        pass

    if args.make_probe_templates:
        download_file_from_google_drive("1iBSANFQT9eacpn7aAE6PmFdIRYQxenGg", "data/bullseye_probe_scan_edge.dm4")
        download_file_from_google_drive("1QTcSKzZjHZd1fDimSI_q9_WsAU25NIXe", "data/vacuum_probe_20x20.dm4")
        download_file_from_google_drive("1p9GaV0k628_afbdqFW62rHObcjQ09qyl", "data/NiPt_nanoparticle_20x20.dm3")
        download_file_from_google_drive("1sUrPEgM1wWyTh-LJ30lGUhcXklHj6ajC", "data/twinBoundary_ShitengZhao20190115MEA.h5")
    else: 
        pass
    
    return None
