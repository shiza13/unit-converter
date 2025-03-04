import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()

engineering_categories = {
    "Velocity - Angular": [
        "radian/second", "radian/day", "radian/hour", "radian/minute",
        "degree/day", "degree/hour", "degree/minute", "degree/second",
        "revolution/day", "revolution/hour", "revolution/minute", "revolution/second"
    ],
    "Acceleration": [
        "meter/square second", "decimeter/square second", "kilometer/square second", 
        "hectometer/square second", "dekameter/square second", "centimeter/square second",
        "millimeter/square second", "micrometer/square second", "nanometer/square second",
        "picometer/square second", "femtometer/square second", "attometer/square second",
        "gal", "galileo", "mile/square second", "yard/square second", "foot/square second",
        "inch/square second", "Acceleration of gravity"
    ],
    "Acceleration - Angular": [
        "radian/square second", "radian/square minute", "revolution/square second", 
        "revolution/minute/second", "revolution/square minute"
    ],
    "Density": [
        "kilogram/cubic meter", "gram/cubic centimeter", "kilogram/cubic centimeter",
        "gram/cubic meter", "gram/cubic millimeter", "milligram/cubic meter",
        "milligram/cubic centimeter", "milligram/cubic millimeter", "exagram/liter",
        "petagram/liter", "teragram/liter", "gigagram/liter", "megagram/liter",
        "kilogram/liter", "hectogram/liter"
    ],
    "Torque": [
        "newton meter", "newton centimeter", "newton millimeter", "kilonewton meter", 
        "dyne meter", "dyne centimeter", "dyne millimeter", "kilogram-force meter", 
        "kilogram-force centimeter", "kilogram-force millimeter", "gram-force meter",
        "gram-force centimeter", "gram-force millimeter", "ounce-force foot", "ounce-force inch", 
        "pound-force foot", "pound-force inch"
    ]
}

st.title("Engineering Unit Converter")


category = st.selectbox("Select an engineering category:", list(engineering_categories.keys()))


from_unit = st.selectbox("Convert from:", engineering_categories[category])
to_unit = st.selectbox("Convert to:", engineering_categories[category])


value = st.number_input("Enter value:", min_value=0.0, format="%.4f")


if st.button("Convert"):
    try:

        result = (value * ureg(from_unit)).to(to_unit).magnitude
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Invalid conversion: {e}")
