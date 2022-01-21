import pandas as pd
import plotly.express as px
import streamlit as st
#from plotly.subplots import make_subplots
#import plotly.graph_objects as go

st.title("""
Recreating Ben's Slides
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

x_axis = st.sidebar.selectbox("Select X-Variable", var_names, index=5)
y_ax = st.sidebar.multiselect("Select up to 6 Y-variable(s)", var_names)
year = st.sidebar.selectbox("Select Year", y)
month = st.sidebar.selectbox("Select Month", m)
day = st.sidebar.selectbox("Select Day", d)
hours = st.sidebar.multiselect("Select up to 2 hours", h)
len_hour = len(hours)
if len_hour > 1:
    hour_sel1 = hours[0]
    hour_sel2 = hours[1]
else:
    hour = hours[0]
############
# st.write('u selected:', y_ax[0])--> was the 1st answer #len(y_ax))--> was 2

len_y_ax = len(y_ax)
if len_y_ax == 1:
    y_axis1 = y_ax[0]
    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis, y_axis1]]
    if len_hour == 1:
        subset = data[
            (raw_df2['yyyy'] == year) &
            (raw_df2['mm'] == month) &
            (raw_df2['dd'] == day) &
            (raw_df2['hh'] == hour)
            ]
        title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour) + "h")

    if len_hour == 2:
        #st.write("h1", hour_sel1, "h2", hour_sel2)
        if hour_sel1 < hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel1) + "/" +
                         str(hour_sel2) + "h")

        if hour_sel1 > hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel2) + "/" +
                         str(hour_sel1) + "h")

        subset = pd.concat([subset_h1, subset_h2])
    if y_axis1 == 'last_az_cmd':
        subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
    elif y_axis1 == 'last_el_cmd':
        subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))
    fig = px.line(subset, x=x_axis, y=y_axis1,
                  title=title_var)
    st.plotly_chart(fig)
elif len_y_ax == 2:
    y_axis1 = y_ax[0]
    y_axis2 = y_ax[1]
    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis, y_axis1, y_axis2]]

    if len_hour == 1:
        subset = data[
            (raw_df2['yyyy'] == year) &
            (raw_df2['mm'] == month) &
            (raw_df2['dd'] == day) &
            (raw_df2['hh'] == hour)
        ]
        title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour) + "h")

    if len_hour == 2:
        #st.write("h1", hour_sel1, "h2", hour_sel2)
        if hour_sel1 < hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel1) + "/" +
                         str(hour_sel2) + "h")

        if hour_sel1 > hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel2) + "/" +
                         str(hour_sel1) + "h")

        subset = pd.concat([subset_h1, subset_h2])

    if y_axis1 == 'last_az_cmd':
        subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
    elif y_axis1 == 'last_el_cmd':
        subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))
    if y_axis2 == 'last_az_cmd':
        subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
    elif y_axis2 == 'last_el_cmd':
        subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))
    #title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour) + "h")
    fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2],
                  title=title_var)
    st.plotly_chart(fig)
elif len_y_ax == 3:
    y_axis1 = y_ax[0]
    y_axis2 = y_ax[1]
    y_axis3 = y_ax[2]
    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis, y_axis1, y_axis2, y_axis3]]

    if len_hour == 1:
        subset = data[
            (raw_df2['yyyy'] == year) &
            (raw_df2['mm'] == month) &
            (raw_df2['dd'] == day) &
            (raw_df2['hh'] == hour)
        ]
        title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour) + "h")

    if len_hour == 2:
        if hour_sel1 < hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel1) + "/" +
                         str(hour_sel2) + "h")

        if hour_sel1 > hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel2) + "/" +
                         str(hour_sel1) + "h")

        subset = pd.concat([subset_h1, subset_h2])

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
    fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2, y_axis3],
                  title=title_var)
    st.plotly_chart(fig)
elif len_y_ax == 4:
    y_axis1 = y_ax[0]
    y_axis2 = y_ax[1]
    y_axis3 = y_ax[2]
    y_axis4 = y_ax[3]
    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis, y_axis1, y_axis2, y_axis3, y_axis4]]
    if len_hour == 1:
        subset = data[
            (raw_df2['yyyy'] == year) &
            (raw_df2['mm'] == month) &
            (raw_df2['dd'] == day) &
            (raw_df2['hh'] == hour)
            ]
        title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour) + "h")

    if len_hour == 2:
        if hour_sel1 < hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel1) + "/" +
                         str(hour_sel2) + "h")

        if hour_sel1 > hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel2) + "/" +
                         str(hour_sel1) + "h")

        subset = pd.concat([subset_h1, subset_h2])
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
    fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2, y_axis3, y_axis4],
                  title=title_var)
    st.plotly_chart(fig)
elif len_y_ax == 5:
    y_axis1 = y_ax[0]
    y_axis2 = y_ax[1]
    y_axis3 = y_ax[2]
    y_axis4 = y_ax[3]
    y_axis5 = y_ax[4]
    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis, y_axis1, y_axis2, y_axis3, y_axis4, y_axis5]]
    if len_hour == 1:
        subset = data[
            (raw_df2['yyyy'] == year) &
            (raw_df2['mm'] == month) &
            (raw_df2['dd'] == day) &
            (raw_df2['hh'] == hour)
            ]
        title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour) + "h")

    if len_hour == 2:
        if hour_sel1 < hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel1) + "/" +
                         str(hour_sel2) + "h")

        if hour_sel1 > hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel2) + "/" +
                         str(hour_sel1) + "h")

        subset = pd.concat([subset_h1, subset_h2])
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
    fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2, y_axis3, y_axis4,
                                       y_axis5],
                  title=title_var)
    st.plotly_chart(fig)
elif len_y_ax == 6:
    y_axis1 = y_ax[0]
    y_axis2 = y_ax[1]
    y_axis3 = y_ax[2]
    y_axis4 = y_ax[3]
    y_axis5 = y_ax[4]
    y_axis6 = y_ax[5]
    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis, y_axis1, y_axis2, y_axis3, y_axis4, y_axis5, y_axis6]]
    if len_hour == 1:
        subset = data[
            (raw_df2['yyyy'] == year) &
            (raw_df2['mm'] == month) &
            (raw_df2['dd'] == day) &
            (raw_df2['hh'] == hour)
            ]
        title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour) + "h")

    if len_hour == 2:
        if hour_sel1 < hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel1) + "/" +
                         str(hour_sel2) + "h")

        if hour_sel1 > hour_sel2:
            subset_h1 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel2)]
            subset_h2 = data[(raw_df2['yyyy'] == year) &
                             (raw_df2['mm'] == month) &
                             (raw_df2['dd'] == day) &
                             (raw_df2['hh'] == hour_sel1)]
            subset_h2['mn'] = subset_h2['mn'] + 60
            title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour_sel2) + "/" +
                         str(hour_sel1) + "h")

        subset = pd.concat([subset_h1, subset_h2])
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
    fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2, y_axis3, y_axis4,
                                       y_axis5, y_axis6],
                  title=title_var)
    st.plotly_chart(fig)
else:
    st.write("Select up to 6 Y-variables!")
