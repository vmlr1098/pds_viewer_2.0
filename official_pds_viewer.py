import pandas as pd
import plotly.express as px
import streamlit as st

st.title("""
Official PDS Viewer
""")

directory = st.file_uploader("Drag and drop a file", type=['csv', 'xlsx'])
try:
    data = (pd.read_csv(directory, na_values=[-9999])).dropna()
except:
    st.error("Please import proper csv file from your local computer")
    st.stop()

raw_df = data[0:5]
var_names = list(raw_df.columns)
st.sidebar.title("Make a Selection")
x_axis = st.sidebar.selectbox("Select X-Variable", var_names, index=5)
y_axis1 = st.sidebar.selectbox("Select Y-Variable 1", var_names, index=6)
y_axis2 = st.sidebar.selectbox("Select Y-Variable 2", var_names, index=7)
y_axis3 = st.sidebar.selectbox("Select Y-Variable 3", var_names, index=6)
y_axis4 = st.sidebar.selectbox("Select Y-Variable 4", var_names, index=7)
y_axis5 = st.sidebar.selectbox("Select Y-Variable 5", var_names, index=6)
y_axis6 = st.sidebar.selectbox("Select Y-Variable 6", var_names, index=7)
################################################################################
data['yyyy'] = data['yyyy'].astype('integer')
yyyy_min = data['yyyy'].min()
yyyy_max = data['yyyy'].max()
y = list(range(yyyy_min, yyyy_max + 1))

mm_min = data['mm'].min()
mm_max = data['mm'].max()
m = list(range(mm_min, mm_max + 1))

dd_min = data['dd'].min()
dd_max = data['dd'].max()
d = list(range(dd_min, dd_max + 1))

hh_min = data['hh'].min()
hh_max = data['hh'].max()
h = list(range(hh_min, hh_max + 1))

year = st.sidebar.selectbox("Select Year", y)
month = st.sidebar.selectbox("Select Month", m)
day = st.sidebar.selectbox("Select Day", d)
hour = st.sidebar.selectbox("Select Hour", h)


################################################################################

raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis, y_axis1, y_axis2,
                y_axis3, y_axis4, y_axis5, y_axis6]]


subset = data[
    (raw_df2['yyyy'] == year) &
    (raw_df2['mm'] == month) &
    (raw_df2['dd'] == day) &
    (raw_df2['hh'] == hour)
    ]

if y_axis1 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis1 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))

if y_axis2 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis2 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))

if y_axis3 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis3 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))

if y_axis4 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis4 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))

if y_axis5 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis5 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))

if y_axis6 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis6 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))

title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour) + "h")
fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2,
                                   y_axis3, y_axis4,
                                   y_axis5, y_axis6],
              title=title_var)
st.plotly_chart(fig)
