import streamlit as st
conversion_dict = {
    "cm to inches": 0.393701,
    "kg to lbs": 2.20462,
    "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
    "mm to inches": 0.0393701,
    "meters to feet": 3.28084,
    "km to miles": 0.621371,
    "cm to feet": 0.0328084,
    "grams to ounces": 0.035274,
    "inches to feet": 0.0833333,
    "liters to gallons": 0.264172,
    "pounds to ounces": 16,
    "mph to kph": 1.60934,
    "acres to square feet": 43560,
    "radians to degrees": 57.2958,
    "hp to kw": 0.7355,
    "meters to yards": 1.09361,
    "mL to cups": 0.00422675,
    "inches to cm": 2.54,
    "lbs to kg": 0.453592,
    "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9,
    "inches to mm": 25.4,
    "Feet to Meters": 0.3048,
    "miles to km": 1.60934,
    "feet to cm": 30.48,
    "ounces to grams": 28.3495,
    "feet to inches": 12,
    "gallons to liters": 3.78541,
    "ounces to pounds": 0.0625,
    "kph to mph": 0.621371,
    "square feet to acres": 0.0000229568,
    "degrees to radians": 0.0174533,
    "kw to hp": 1.34102,
    "yards to meters": 0.9144,
    "cups to mL": 236.588,
}

st.title("🔢 Common Conversions")

conversion_options = list(conversion_dict.keys())
conversion_type = st.selectbox("Select Conversion:", conversion_options)

value = st.number_input(f"Enter value in {conversion_type.split(' to ')[0]}:", min_value=0.0, format="%.2f")

if st.button("Convert"):
    factor = conversion_dict[conversion_type]
    result = factor(value) if callable(factor) else value * factor
    st.success(f"✅ {value} {conversion_type.split(' to ')[0]} = {result:.4f} {conversion_type.split(' to ')[1]}")
