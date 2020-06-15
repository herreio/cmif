#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
access data in CMI format through correspSearch webservices
"""

import requests
from lxml import etree

TEI_JSON = "http://correspSearch.bbaw.de/api/v1.1/tei-json.xql"
TEI_XML = "http://correspSearch.bbaw.de/api/v1.1/tei-xml.xql"

ENTITIES = {
  "HALLE": "http://www.geonames.org/2911522",
  "FORSTER": "http://d-nb.info/gnd/118534432",
  "HEMMERDE": "http://d-nb.info/gnd/1037496973"
}


def correspsearch(correspondent="", sender="", addressee="",
                  startdate=None, enddate=None, place=None,
                  placeSender=None, placeAddressee=None,
                  available=None, strictDate=False, endpoint=TEI_XML):
    """
    | query data in CMI format via correspSearch API by given parameters
    | available endpoints: TEI_XML (default) / TEI_JSON
    | see https://correspsearch.net/index.xql?id=api for details
    """
    if correspondent == "" and sender == "" and addressee == "":
        print("need to specify correspondent!")
        return None
    if correspondent != "":
        params = {
          "correspondent": correspondent
        }
    if sender != "":
        params = {
          "sender": sender
        }
    if addressee != "":
        params = {
          "addressee": addressee
        }
    if startdate is not None:
        params["startdate"] = startdate
    if enddate is not None:
        params["enddate"] = enddate
    if strictDate:
        params["strictDate"] = strictDate
    if place is not None:
        params["place"] = place
    if placeSender is not None:
        params["placeSender"] = placeSender
    if placeAddressee is not None:
        params["placeAddressee"] = placeAddressee
    if available is not None:
        params["available"] = available
    try:
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            if endpoint == TEI_JSON:
                if type(response.json()) == dict:
                    return response.json()
                else:
                    print("Invalid query!")
                    return {}
            else:
                tei = etree.fromstring(response.content)
                if not tei.text == "Invalid query.":
                    return tei
                else:
                    print("Invalid query!")
                    return None
        else:
            print("cmif.service.correspsearch:")
            print("request is not ok!")
            print("url of request:")
            print(response.url)
            print("http status code: ",
                  str(response.status_code))
    except requests.exceptions.ConnectionError:
        print("cmif.service.correspsearch:")
        print("request failed! connection error...")
    except requests.exceptions.Timeout:
        print("cmif.service.correspsearch:")
        print("request failed! timeout... try later?")
    except requests.exceptions.TooManyRedirects:
        print("cmif.service.correspsearch:")
        print("request failed! bad url, try another one!")
    except requests.exceptions.RequestException:
        print("cmif.service.correspsearch:")
        print("request failed! don't know why...")
    return None
