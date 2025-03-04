import streamlit as st
from pint import UnitRegistry
st.set_page_config(page_title="Unit Converter", layout="wide")

st.title("🔄 Unit Converter")

st.write("Welcome to my **Unit Converter**! Select a conversion category from the list.")

ureg = UnitRegistry()

conversion_categories = {
    "Length": [
        "meter", "kilometer", "centimeter", "millimeter", "micrometer", "nanometer", "mile",
        "yard", "foot", "inch", "light_year"
    ],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Area": [
        "square_meter", "square_kilometer", "square_centimeter", "square_millimeter", "square_micrometer",
        "hectare", "square_mile", "square_yard", "square_foot", "square_inch", "acre"
    ],
    "Volume": [
        "cubic_meter", "cubic_kilometer", "cubic_centimeter", "cubic_millimeter", "liter", "milliliter",
        "gallon", "quart", "pint", "cup", "fluid_ounce", "tablespoon", "teaspoon", "cubic_mile",
        "cubic_yard", "cubic_foot", "cubic_inch"
    ],
    "Weight": [
        "kilogram", "gram", "milligram", "metric_ton", "long_ton", "short_ton",
        "pound", "ounce", "carat", "atomic_mass_unit"
    ],
    "Time": [
        "second", "millisecond", "microsecond", "nanosecond", "picosecond",
        "minute", "hour", "day", "week", "month", "year"
    ]
}

category = st.selectbox("Select a category:", list(conversion_categories.keys()))

from_unit = st.selectbox("Convert from:", conversion_categories[category])
to_unit = st.selectbox("Convert to:", conversion_categories[category])

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

if st.button("Convert"):
    try:
        if category == "Temperature":
            
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value  
        else:
           
            result = (value * ureg(from_unit)).to(to_unit).magnitude

        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

    except Exception as e:
        st.error(f"Invalid conversion: {e}")
st.markdown(
    """
    <style>
    .fixed-name {
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 16px;
        color: gray;
    }
    </style>
    <div class="fixed-name">Created by Shiza Tariq</div>
    """,
    unsafe_allow_html=True,
)
