#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import pathlib

import xmltodict as xml

path = ""


def read_xml():
    json_list = []
    for filename in os.listdir(path):
        if not filename.endswith('.xml'):
            continue
        name = os.path.join(path, filename)
        with open(name) as xml_file:
            data_dict = xml.parse(xml_file.read())
            xml_file.close()
            json_data = json.dumps(data_dict, indent=2)
        json_list.append(json_data)
    return json_list

def parse_file(file_name):
    with open(file_name) as xml_file:
        data_dict = xml.parse(xml_file.read())
        xml_file.close()
        json_data = json.dumps(data_dict, indent=2)
    return(json_data)

def main():
    read_xml()


if __name__ == "__main__":
    parse_file()
