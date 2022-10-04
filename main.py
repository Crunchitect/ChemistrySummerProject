import streamlit as st
from PIL import Image
import pandas as pd
import easyocr
import cv2


st.set_page_config(page_title="Test Webpage", page_icon=":microscope:", layout='centered')


with st.container():
    st.header("Chemistry Cards")
    st.subheader("By Prem")
    st.title("A project for the midterm camp")
    st.write("Available Compounds: H2O, CO2, OgTs3, CCCCBr")
    st.write("...")

picture = st.camera_input("Chemical Combination")

if picture:
    st.image(picture)
    img = Image.open(picture)
    img.save('photo.png')
    img = cv2.imread('photo.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    noise = cv2.medianBlur(gray, 3)
    thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img, paragraph="False")
    df = pd.DataFrame(result)
    df = df.to_dict()
    for i in df[1]:
        if df[1][i] == 'H':
            st.write("Hydrogen")
        if df[1][i] == 'He':
            st.write("Helium")
        if df[1][i] == 'Li':
            st.write("Lithium")
        if df[1][i] == 'Be':
            st.write("Beryllium")
        if df[1][i] == 'B':
            st.write("Boron")
        if df[1][i] == 'C':
            st.write("Carbon")
        if df[1][i] == 'N':
            st.write("Nitrogen")
        if df[1][i] == 'O':
            st.write("Oxygen")
        if df[1][i] == 'F':
            st.write("Fluorine")
        if df[1][i] == 'Ne':
            st.write("Neon")
        if df[1][i] == 'Na':
            st.write("Sodium")
        if df[1][i] == 'Mg':
            st.write("Magnesium")
        if df[1][i] == 'Al':
            st.write("Aluminium")
        if df[1][i] == 'Si':
            st.write("Silicon")
        if df[1][i] == 'P':
            st.write("Phosphorus")
        if df[1][i] == 'S':
            st.write("Sulfur")
        if df[1][i] == 'Cl':
            st.write("Chlorine")
        if df[1][i] == 'Ar':
            st.write("Argon")
        if df[1][i] == 'K':
            st.write("Potassium")
        if df[1][i] == 'Ca':
            st.write("Calcium")
        if df[1][i] == 'Sc':
            st.write("Scandium")
        if df[1][i] == 'Ti':
            st.write("Titanium")
        if df[1][i] == 'V':
            st.write("Vanadium")
        if df[1][i] == 'Cr':
            st.write("Chromium")
        if df[1][i] == 'Mn':
            st.write("Manganese")
        if df[1][i] == 'Fe':
            st.write("Iron")
        if df[1][i] == 'Co':
            st.write("Cobalt")
        if df[1][i] == 'Ni':
            st.write("Nickel")
        if df[1][i] == 'Cu':
            st.write("Copper")
        if df[1][i] == 'Zn':
            st.write("Zinc")
        if df[1][i] == 'Ga':
            st.write("Gallium")
        if df[1][i] == 'Ge':
            st.write("Germanium")
        if df[1][i] == 'As':
            st.write("Arsenic")
        if df[1][i] == 'Se':
            st.write("Selenium")
        if df[1][i] == 'Br':
            st.write("Bromine")
        if df[1][i] == 'Kr':
            st.write("Krypton")
        if df[1][i] == 'Rb':
            st.write("Rubidium")
        if df[1][i] == 'Sr':
            st.write("Strontium")
        if df[1][i] == 'Y':
            st.write("Yttrium")
        if df[1][i] == 'Zr':
            st.write("Zirconium")
        if df[1][i] == 'Nb':
            st.write("Niobium")
        if df[1][i] == 'Mo':
            st.write("Molybdenum")
        if df[1][i] == 'Tc':
            st.write("Technetium")
        if df[1][i] == 'Ru':
            st.write("Ruthenium")
        if df[1][i] == 'Rh':
            st.write("Rhodium")
        if df[1][i] == 'Pd':
            st.write("Palladium")
        if df[1][i] == 'Ag':
            st.write("Silver")
        if df[1][i] == 'Cd':
            st.write("Cadmium")
        if df[1][i] == 'In':
            st.write("Indium")
        if df[1][i] == 'Sn':
            st.write("Tin")
        if df[1][i] == 'Sb':
            st.write("Antimony")
        if df[1][i] == 'Te':
            st.write("Tellurium")
        if df[1][i] == 'I':
            st.write("Iodine")
        if df[1][i] == 'Xe':
            st.write("Xenon")
        if df[1][i] == 'Cs':
            st.write("Caesium")
        if df[1][i] == 'Ba':
            st.write("Barium")
        if df[1][i] == 'La':
            st.write("Lanthanum")
        if df[1][i] == 'Ce':
            st.write("Cerium")
        if df[1][i] == 'Pr':
            st.write("Praseodymium")
        if df[1][i] == 'Nd':
            st.write("Neodymium")
        if df[1][i] == 'Pm':
            st.write("Promethium")
        if df[1][i] == 'Sm':
            st.write("Samarium")
        if df[1][i] == 'Eu':
            st.write("Europium")
        if df[1][i] == 'Gd':
            st.write("Gadolinium")
        if df[1][i] == 'Tb':
            st.write("Terbium")
        if df[1][i] == 'Dy':
            st.write("Dysprosium")
        if df[1][i] == 'Ho':
            st.write("Holmium")
        if df[1][i] == 'Er':
            st.write("Erbium")
        if df[1][i] == 'Tm':
            st.write("Thulium")
        if df[1][i] == 'Yb':
            st.write("Ytterbium")
        if df[1][i] == 'Lu':
            st.write("Lutetium")
        if df[1][i] == 'Hf':
            st.write("Hafnium")
        if df[1][i] == 'Ta':
            st.write("Tantalum")
        if df[1][i] == 'W':
            st.write("Tungsten")
        if df[1][i] == 'Re':
            st.write("Rhenium")
        if df[1][i] == 'Os':
            st.write("Osmium")
        if df[1][i] == 'Ir':
            st.write("Iridium")
        if df[1][i] == 'Pt':
            st.write("Platinum")
        if df[1][i] == 'Au':
            st.write("Gold")
        if df[1][i] == 'Hg':
            st.write("Mercury")
        if df[1][i] == 'Tl':
            st.write("Thallium")
        if df[1][i] == 'Pb':
            st.write("Lead")
        if df[1][i] == 'Bi':
            st.write("Bismuth")
        if df[1][i] == 'Po':
            st.write("Polonium")
        if df[1][i] == 'At':
            st.write("Astatine")
        if df[1][i] == 'Rn':
            st.write("Radon")
        if df[1][i] == 'Fr':
            st.write("Francium")
        if df[1][i] == 'Ra':
            st.write("Radium")
        if df[1][i] == 'Ac':
            st.write("Actinium")
        if df[1][i] == 'Th':
            st.write("Thorium")
        if df[1][i] == 'Pa':
            st.write("Protactinium")
        if df[1][i] == 'U':
            st.write("Uranium")
        if df[1][i] == 'Np':
            st.write("Neptunium")
        if df[1][i] == 'Pu':
            st.write("Plutonium")
        if df[1][i] == 'Am':
            st.write("Americium")
        if df[1][i] == 'Cm':
            st.write("Curium")
        if df[1][i] == 'Bk':
            st.write("Berkelium")
        if df[1][i] == 'Cf':
            st.write("Californium")
        if df[1][i] == 'Es':
            st.write("Einsteinium")
        if df[1][i] == 'Fm':
            st.write("Fermium")
        if df[1][i] == 'Md':
            st.write("Mendelevium")
        if df[1][i] == 'No':
            st.write("Nobelium")
        if df[1][i] == 'Lr':
            st.write("Lawrencium")
        if df[1][i] == 'Rf':
            st.write("Rutherfordium")
        if df[1][i] == 'Db':
            st.write("Dubnium")
        if df[1][i] == 'Sg':
            st.write("Seaborgium")
        if df[1][i] == 'Bh':
            st.write("Bohrium")
        if df[1][i] == 'Hs':
            st.write("Hassium")
        if df[1][i] == 'Mt':
            st.write("Meitnerium")
        if df[1][i] == 'Ds':
            st.write("Darmstadtium")
        if df[1][i] == 'Rg':
            st.write("Roentgenium")
        if df[1][i] == 'Cn':
            st.write("Copernicium")
        if df[1][i] == 'Nh':
            st.write("Nihonium")
        if df[1][i] == 'Fl':
            st.write("Flerovium")
        if df[1][i] == 'Mc':
            st.write("Moscovium")
        if df[1][i] == 'Lv':
            st.write("Helium")
        if df[1][i] == 'Ts':
            st.write("Lithium")
        if df[1][i] == 'Og':
            st.write("Oganesson")
