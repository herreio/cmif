#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test creation of file in CMI format

Creator:          D. Herre
GitHub:       herreio/cmif

Created:        2020-05-03
Modified:       2020-05-04
"""

from cmif import build, local
from datetime import datetime

test_dir = local.os.path.dirname(__file__)
test_out = local.os.path.join(test_dir, "output")

root = build.tei_root()

# ~~ <teiHeader> ~~ #

header = build.tei_header()

# ~~ <fileDesc> ~~ #

# create <titleStmt>
title = build.tei_title("Test output in CMI format from Python library cmif")
editor = build.tei_editor("Donatus Herre ")
email = build.tei_email("pypi@herre.io")
editor.append(email)
title_stmt = build.tei_title_stmt([title, editor])

# create <publicationStmt>
publisher = build.tei_publisher(
    build.tei_ref("herreio",
                  "https://github.com/herreio"))
url = "https://raw.githubusercontent.com/herreio/cmif/master/" + \
    "test/output/cmif.xml"
idno = build.tei_idno(url)
pub_date = build.tei_date(attrib_when=datetime.today().strftime("%Y-%m-%d"))
availability = build.tei_availability(build.tei_license())
pub_stmt = build.tei_publication_stmt([publisher, idno,
                                       pub_date, availability])

# create <sourceDesc>
ref_url = "https://github.com/herreio/benann/tree/master/data/de_lttr"
bibl = build.tei_bibl("Benjamin Briefe aus dem Exil. URL: ",
                      "online", domain=ref_url)
ref = build.tei_ref(ref_url, ref_url)
bibl.append(ref)
source_desc = build.tei_source_desc([bibl])

# create <fileDesc> with child nodes
#   <titleStmt>, <publicationStmt> and <sourceDesc>
file_desc = build.tei_file_desc([title_stmt, pub_stmt, source_desc])

# add <fileDesc> to <teiHeader>
header.append(file_desc)

# ~~ <profileDesc> ~~ #

profile_desc = build.tei_profile_desc()

# create <correspAction> with @type="sent"
author = build.tei_pers_name("Walter Benjamin",
                             "http://d-nb.info/gnd/118509039")
sent_date = build.tei_date(attrib_when="1933-01-15")
senders_place = build.tei_place_name("Berlin",
                                     "https://www.geonames.org/2950159")
sent = build.tei_corresp_action("sent",
                                children=[author, sent_date, senders_place])

# create <correspAction> with @type="received"
addressee = build.tei_pers_name("Gershom Scholem",
                                "http://d-nb.info/gnd/118610295")
recieved = build.tei_corresp_action("received", children=[addressee])

# create <correspDesc> with @ref and child nodes
letter_ref = "https://raw.githubusercontent.com/herreio/benann/master/data/" \
    "de_lttr/Benjamin_Briefe_330115_Scholem.txt"
corresp_desc = build.tei_corresp_desc(attrib_ref=letter_ref,
                                      children=[sent, recieved])

# add <correspDesc> to <profileDesc>
profile_desc.append(corresp_desc)

# add <profileDesc> to <teiHeader>
header.append(profile_desc)

# ~~ <teiHeader> (done) ~~ #
# add header to root element
root.append(header)

# ~~ <text> ~~ #
text = build.tei_text_empty()

# ~~ <text> (done) ~~ #
root.append(text)

tree = build.etree.ElementTree(root)
tree = build.add_pi(tree)

local.writer(root, file="cmif.xml", path=test_out)
