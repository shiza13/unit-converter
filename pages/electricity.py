import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()

units = {
    "Charge Converter": {
        "coulomb [C]": ureg.coulomb,
        "megacoulomb [MC]": ureg.megacoulomb,
        "kilocoulomb [kC]": ureg.kilocoulomb,
        "millicoulomb [mC]": ureg.millicoulomb,
        "microcoulomb [µC]": ureg.microcoulomb,
        "nanocoulomb [nC]": ureg.nanocoulomb,
        "picocoulomb [pC]": ureg.picocoulomb,
        "ampere-hour [A*h]": ureg.ampere * ureg.hour,
        "ampere-minute [A*min]": ureg.ampere * ureg.minute,
        "ampere-second [A*s]": ureg.ampere * ureg.second,  
    },
    "Linear Charge Density Converter": {
        "coulomb/meter [C/m]": ureg.coulomb / ureg.meter,
        "coulomb/centimeter [C/cm]": ureg.coulomb / ureg.centimeter,
        "coulomb/inch [C/in]": ureg.coulomb / ureg.inch,
    },
    "Surface Charge Density Converter": {
        "coulomb/square meter": ureg.coulomb / ureg.meter**2,
        "coulomb/square centimeter": ureg.coulomb / ureg.centimeter**2,
        "coulomb/square inch [C/in^2]": ureg.coulomb / ureg.inch**2,
    },
    "Volume Charge Density Converter": {
        "coulomb/cubic meter [C/m^3]": ureg.coulomb / ureg.meter**3,
        "coulomb/cubic centimeter": ureg.coulomb / ureg.centimeter**3,
        "coulomb/cubic inch [C/in^3]": ureg.coulomb / ureg.inch**3,
    },
    "Current Converter": {
        "ampere [A]": ureg.ampere,
        "kiloampere [kA]": ureg.kiloampere,
        "milliampere [mA]": ureg.milliampere,
    },
    "Electric Field Strength Converter": {
        "volt/meter [V/m]": ureg.volt / ureg.meter,
        "kilovolt/meter [kV/m]": ureg.kilovolt / ureg.meter,
        "volt/centimeter [V/cm]": ureg.volt / ureg.centimeter,
    },
    "Electrostatic Capacitance Converter": {
        "farad [F]": ureg.farad,
        "microfarad [µF]": ureg.microfarad,
        "nanofarad [nF]": ureg.nanofarad,
        "picofarad [pF]": ureg.picofarad,
    },
    "Inductance Converter": {
        "henry [H]": ureg.henry,
        "microhenry [µH]": ureg.microhenry,
        "nanohenry [nH]": ureg.nanohenry,
        "picohenry [pH]": ureg.picohenry,
    },
}

st.title("Electricity Conversion Tool")

category = st.selectbox("Select a conversion category", list(units.keys()))

if category:
    unit_options = units[category]
    from_unit = st.selectbox("Select the from unit", list(unit_options.keys()))
    to_unit = st.selectbox("Select the to unit", list(unit_options.keys()))
    value = st.number_input("Enter the value to convert", min_value=0.0, format="%.6f")

    if st.button("Convert"):
        try:
            result = (value * unit_options[from_unit]).to(unit_options[to_unit])
            st.success(f"{value} {from_unit} = {result.magnitude:.6f} {to_unit}")
        except Exception as e:
            st.error(f"Conversion error: {e}")
