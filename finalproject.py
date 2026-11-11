#!/usr/bin/python
print('Content-type: text/html\n')

#http://homer.stuy.edu/~csimi80/final/finalproject.py

import cgitb
cgitb.enable()
import cgi
import matplotlib.pyplot as plt
import numpy as np
import io
import base64


#SETUP

rosemary_DNA = open('rosemary_sequence.txt').read().upper()
rosemary_DNA = rosemary_DNA.replace('\n', '')
rosemary_DNA = rosemary_DNA.replace(' ', '')
lavender_DNA = open('lavender_sequence.txt').read().upper()
lavender_DNA = lavender_DNA.replace('\n', '')
lavender_DNA = lavender_DNA.replace(' ', '')
basil_DNA = open('basil_sequence.txt').read().upper()
basil_DNA = basil_DNA.replace('\n', '')
basil_DNA = basil_DNA.replace(' ', '')
mint_DNA = open('mint_sequence.txt').read().upper()
mint_DNA = mint_DNA.replace('\n', '')
mint_DNA = mint_DNA.replace(' ', '')
sage_DNA = open('sage_sequence.txt').read().upper()
sage_DNA = sage_DNA.replace('\n', '')
sage_DNA = sage_DNA.replace(' ', '')
lemonbalm_DNA = open('lemonbalm_sequence.txt').read().upper()
lemonbalm_DNA = lemonbalm_DNA.replace('\n', '')
lemonbalm_DNA = lemonbalm_DNA.replace(' ', '')
catnip_DNA = open('catnip_sequence.txt').read().upper()
catnip_DNA = catnip_DNA.replace('\n', '')
catnip_DNA = catnip_DNA.replace(' ', '')
oregano_DNA = open('oregano_sequence.txt').read().upper()
oregano_DNA = oregano_DNA.replace('\n', '')
oregano_DNA = oregano_DNA.replace(' ', '')
bergamot_DNA = open('bergamot_sequence.txt').read().upper()
bergamot_DNA = bergamot_DNA.replace('\n', '')
bergamot_DNA = bergamot_DNA.replace(' ', '')




plants = {"Spearmint": {"scientific_name": "Mentha spicata",
        "family": "Lamiaceae",
        "sequence": mint_DNA},
   "Lavender": {"scientific_name": "Lavandula angustifolia",
        "family": "Lamiaceae",
        "sequence": lavender_DNA},
    "Rosemary": {"scientific_name": "Salvia rosmarinus",
        "family": "Lamiaceae",
        "sequence": rosemary_DNA},
    "Sage": {"scientific_name": "Salvia officinalis",
        "family": "Lamiaceae",
        "sequence": sage_DNA},
    "Lemon Balm": {"scientific_name": "Melissa officinalis",
        "family": "Lamiaceae",
        "sequence": lemonbalm_DNA},
    "Basil": {"scientific_name": "Ocimum basilicum",
        "family": "Lamiaceae",
        "sequence": basil_DNA},
    "Catnip": {"scientific_name": "Nepeta cataria",
        "family": "Lamiaceae",
        "sequence": catnip_DNA},
    "Oregano": {"scientific_name": "Origanum vulgare",
        "family": "Lamiaceae",
        "sequence": oregano_DNA},
    "Bergamot": {"scientific_name": "Monarda didyma",
        "family": "Lamiaceae",
        "sequence": bergamot_DNA}}


#ANALYSIS FUNCTIONS

def bp_count(DNA):
    count = 0
    i = 0
    while i < len(DNA):
        count += 1
        i += 1
    return count

def base_freq(DNA):
    nucleotide_dict = {}
    for base in DNA:
        if base not in nucleotide_dict:
            nucleotide_dict[base] = 0
        nucleotide_dict[base] += 1
    return nucleotide_dict

def GC_percentage(DNA):
    nucleotide_dict = base_freq(DNA)
    GC = nucleotide_dict['G'] + nucleotide_dict['C']
    return (GC * 100 / (bp_count(DNA)))


def count_matches(DNA1, DNA2):
    if DNA1 == "" or DNA2 == "":
        return 0
    if DNA1[0] == DNA2[0]:
        return 1 + count_matches(DNA1[1:], DNA2[1:])
    return count_matches(DNA1[1:], DNA2[1:])

def similarity(DNA1, DNA2):
    matches = count_matches(DNA1, DNA2)
    percentage = matches / min(len(DNA1), len(DNA2)) * 100
    return percentage

def codon_signal_analysis(DNA):
    start = 0
    stop = 0
    i = 0
    while i < len(DNA) - 2:
        codon = DNA[i:i+3]
        if codon == "ATG":
            start += 1
        elif codon == "TAA" or codon == "TAG" or codon == "TGA":
            stop += 1
        i += 3
    return start, stop

def DNA_barcode(DNA):
    html = '<div>'
    for base in DNA:
        if base == 'A':
            color = '#6495ED'
        elif base == 'T':
            color = '#483D8B'
        elif base == 'C':
            color = '#7FFF00'
        elif base == 'G':
            color = '#FF4500'
        html += f'<span style="background-color:{color}; display:inline-block; width:1.05px; height:50px;"></span>'
    html += '</div>'
    return html


#HTML

legend = """
<div class="legend">
    <span class="legend-box A"></span> A
    <span class="legend-box T"></span> T
    <span class="legend-box C"></span> C
    <span class="legend-box G"></span> G
</div>
"""

def make_image_element():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_code = base64.b64encode(buffer.read()).decode('utf-8')
    src = "data:image/png;base64,"
    src+= image_code
    html = '<img src="' + src
    html+= '" alt="pie chart">'
    return html


def make_graph(DNA):
    freq = base_freq(DNA)
    data = [freq['A'], freq['T'], freq['C'], freq['G']]
    labels = ['A', 'T', 'C', 'G']
    colors = ['#6495ED', '#483D8B', '#7FFF00', '#FF4500']
    plt.figure(figsize=(4,4))
    plt.pie(data, labels=labels, autopct='%1.2f%%', colors=colors)
    plt.title(" ")

def make_html_header(title, css):
    html = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
    <link href="{css}" rel="stylesheet">
  </head>
  <body>
  <nav>
    <ul class="navigation">
    <li><a href="index.html" class="navlink">Home</a></li>
    <li><a href="finalproject.py" id="current" class="navlink">DNA Analysis</a></li>
    </ul>
    </nav>'''
    return html

def make_html_footer():
    html = """
    </body>
    </html>
    """
    return html

def make_form(plants):
    html = """
    <h1>Plant DNA Analysis Tool</h1>
    <form method="GET" action="finalproject.py">
    <h2>Select plant to analyze:</h2>
    <select name="plant1">
    """
    for plant in plants:
        html += '<option value="' + plant + '">' + plant + '</option>'
    html += """
    </select>
    <h2>Select plant to compare with:</h2>
    <select name="plant2">
    """
    for plant in plants:
        html += '<option value="' + plant + '">' + plant + '</option>'
    html += """
    </select>
    <input type="submit" value="Compare">
    </form>
    """
    return html


def make_full_html(title, css, body):
    html = make_html_header(title, css)
    html += body
    html += make_html_footer()
    return html

for plant in plants:
    DNA = plants[plant]["sequence"]
    plants[plant]["base_pairs"] = bp_count(DNA)
    plants[plant]["GC_Content"] = GC_percentage(DNA)
    plants[plant]["codon_stats"] = codon_signal_analysis(DNA)


data = cgi.FieldStorage()

if len(data) == 0:
    body = make_form(plants)
    html = make_full_html("Plant DNA Analysis Tool", "finalproject.css", body)
    print(html)
else:
    plant1 = data.getvalue("plant1")
    plant2 = data.getvalue("plant2")
    DNA1 = plants[plant1]["sequence"]
    starts1, stops1 = plants[plant1]["codon_stats"]
    if stops1 == 0:
        stop_text1 = "No stop codons were detected in the selected reading frame."
    else:
        stop_text1 = f"Stop codons (TAA / TAG / TGA): {stops1}"
    DNA2 = plants[plant2]["sequence"]
    starts2, stops2 = plants[plant2]["codon_stats"]
    if stops2 == 0:
        stop_text2 = "No stop codons were detected in the selected reading frame."
    else:
        stop_text2 = f"Stop codons (TAA / TAG / TGA): {stops2}"
    similarity1 = similarity(DNA1, DNA2)
    GC1 = plants[plant1]["GC_Content"]
    GC2 = plants[plant2]["GC_Content"]
    make_graph(DNA1)
    img = make_image_element()
    barcode1 = DNA_barcode(DNA1)
    barcode2 = DNA_barcode(DNA2)
    body = f"""
    <h1>Plant DNA Analysis Tool</h1>
    
    <div class="container">
    
    <div class="left">

    <h2>{plant1}</h2>
    
    <p>Scientific name: <i>{plants[plant1]["scientific_name"]}</i></p>
    <p>Family: <i>{plants[plant1]["family"]}</i></p>
    <p>Base pairs: {plants[plant1]["base_pairs"]}</p>
    <p>GC content: {GC1:.2f}%</p>
    
    <h3>Codon Signal Analysis</h3>
    
    <p>Start codons (ATG): {starts1}</p>
    <p>{stop_text1}</p>
    <p>This analysis scanned DNA in reading frames of three bases to detect codon signals.</p>
    
    <h3>Nucleotide Composition</h3>
    {img}
    
    <h3>DNA Barcode</h3>
    {barcode1}
    {legend}
    
    </div>
    
    <div class="right">
    
    <h2>Similarity Percentage</h2>
   
    <p>{similarity1:.2f}% similarity between {plant1} and {plant2}</p>
    
    <h2>{plant2}</h2>
    
    <p>Scientific name: <i>{plants[plant2]["scientific_name"]}</i></p>
    <p>Family: <i>{plants[plant2]["family"]}</i></p>
    <p>Base pairs: {plants[plant2]["base_pairs"]}</p>
    <p>GC content: {GC2:.2f}%</p>
    
    <h3>Codon Signal Analysis</h3>
    
    <p>Start codons (ATG): {starts2}</p>
    <p>{stop_text2}</p>
    <p>This analysis scanned DNA in reading frames of three bases to detect codon signals.</p>

    
    <h3>DNA Barcode</h3>
    {barcode2}
    {legend}
    
    <a href="finalproject.py" class="again">Conduct another analysis</a>
    
    </div>

    </div>
    
    """
    html = make_full_html("Plant DNA Analysis Tool", "finalproject.css", body)
    print(html)
