import pandas as pd
import plotly.express as px
import streamlit as st

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

try:
    x_axis = st.sidebar.selectbox("Select X-Variable", var_names, index=0)
    y_ax = st.sidebar.multiselect("Select up to 6 Y-variable(s)", var_names)
    year = st.sidebar.selectbox("Select Year", y, index=0)
    month = st.sidebar.selectbox("Select Month", m, index=0)
    day = st.sidebar.selectbox("Select Day", d, index=0)
    hours = st.sidebar.multiselect("Select up to 6 hours", h)
    hours.sort()
    len_y_ax = len(y_ax)
    len_hour = len(hours)
except:
    st.error("Please select variables from drop-down menu")
    st.stop()


if len_y_ax == 1:
    y_axis1 = y_ax[0]
    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis,
                    y_axis1]]
elif len_y_ax == 2:
    y_axis1 = y_ax[0]
    y_axis2 = y_ax[1]

    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis,
                    y_axis1, y_axis2]]
elif len_y_ax == 3:
    y_axis1 = y_ax[0]
    y_axis2 = y_ax[1]
    y_axis3 = y_ax[2]

    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis,
                    y_axis1, y_axis2, y_axis3]]
elif len_y_ax == 4:
    y_axis1 = y_ax[0]
    y_axis2 = y_ax[1]
    y_axis3 = y_ax[2]
    y_axis4 = y_ax[3]

    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis,
                    y_axis1, y_axis2, y_axis3, y_axis4]]
elif len_y_ax == 5:
    y_axis1 = y_ax[0]
    y_axis2 = y_ax[1]
    y_axis3 = y_ax[2]
    y_axis4 = y_ax[3]
    y_axis5 = y_ax[4]

    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis,
                    y_axis1, y_axis2, y_axis3, y_axis4, y_axis5]]
elif len_y_ax == 6:
    y_axis1 = y_ax[0]
    y_axis2 = y_ax[1]
    y_axis3 = y_ax[2]
    y_axis4 = y_ax[3]
    y_axis5 = y_ax[4]
    y_axis6 = y_ax[5]

    raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis,
                    y_axis1, y_axis2, y_axis3, y_axis4, y_axis5, y_axis6]]
else:
    st.write("choose up to 6 variables")

if len_hour == 1:
    hour_sel1 = hours[0]
    subset = data[
        (raw_df2['yyyy'] == year) &
        (raw_df2['mm'] == month) &
        (raw_df2['dd'] == day) &
        (raw_df2['hh'] == hour_sel1)
        ]
    title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " +
                 "hrs: " + str(hour_sel1))
elif len_hour == 2:
    hour_sel1 = hours[0]
    hour_sel2 = hours[1]
    subset_h1 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel1)]
    subset_h2 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel2)]
    subset_h2['mn'] = subset_h2['mn'] + 60
    subset = pd.concat([subset_h1, subset_h2])
    title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " +
                 "hrs: " + str(hour_sel1) + ", " + str(hour_sel2))
elif len_hour == 3:
    hour_sel1 = hours[0]
    hour_sel2 = hours[1]
    hour_sel3 = hours[2]
    subset_h1 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel1)]
    subset_h2 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel2)]
    subset_h3 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel3)]
    subset_h2['mn'] = subset_h2['mn'] + 60
    subset_h3['mn'] = subset_h3['mn'] + 120
    subset = pd.concat([subset_h1, subset_h2, subset_h3])
    title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " +
                 "hrs: " + str(hour_sel1) + ", " + str(hour_sel2) + ", " + str(hour_sel3))
elif len_hour == 4:
    hour_sel1 = hours[0]
    hour_sel2 = hours[1]
    hour_sel3 = hours[2]
    hour_sel4 = hours[3]
    subset_h1 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel1)]
    subset_h2 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel2)]
    subset_h3 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel3)]
    subset_h4 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel4)]
    subset_h2['mn'] = subset_h2['mn'] + 60
    subset_h3['mn'] = subset_h3['mn'] + 120
    subset_h4['mn'] = subset_h4['mn'] + 180
    subset = pd.concat([subset_h1, subset_h2, subset_h3, subset_h4])
    title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " +
                 "hrs: " + str(hour_sel1) + ", " + str(hour_sel2) + ", " + str(hour_sel3) +
                 ", " + str(hour_sel4))
elif len_hour == 5:
    hour_sel1 = hours[0]
    hour_sel2 = hours[1]
    hour_sel3 = hours[2]
    hour_sel4 = hours[3]
    hour_sel5 = hours[4]
    subset_h1 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel1)]
    subset_h2 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel2)]
    subset_h3 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel3)]
    subset_h4 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel4)]
    subset_h5 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel5)]
    subset_h2['mn'] = subset_h2['mn'] + 60
    subset_h3['mn'] = subset_h3['mn'] + 120
    subset_h4['mn'] = subset_h4['mn'] + 180
    subset_h5['mn'] = subset_h5['mn'] + 240
    subset = pd.concat([subset_h1, subset_h2, subset_h3, subset_h4, subset_h5])
    title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " +
                 "hrs: " + str(hour_sel1) + ", " + str(hour_sel2) + ", " + str(hour_sel3) +
                 ", " + str(hour_sel4) + ", " + str(hour_sel5))
elif len_hour == 6:
    hour_sel1 = hours[0]
    hour_sel2 = hours[1]
    hour_sel3 = hours[2]
    hour_sel4 = hours[3]
    hour_sel5 = hours[4]
    hour_sel6 = hours[5]
    subset_h1 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel1)]
    subset_h2 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel2)]
    subset_h3 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel3)]
    subset_h4 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel4)]
    subset_h5 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel5)]
    subset_h6 = data[(raw_df2['yyyy'] == year) &
                     (raw_df2['mm'] == month) &
                     (raw_df2['dd'] == day) &
                     (raw_df2['hh'] == hour_sel6)]
    subset_h2['mn'] = subset_h2['mn'] + 60
    subset_h3['mn'] = subset_h3['mn'] + 120
    subset_h4['mn'] = subset_h4['mn'] + 180
    subset_h5['mn'] = subset_h5['mn'] + 240
    subset_h6['mn'] = subset_h6['mn'] + 300
    subset = pd.concat([subset_h1, subset_h2, subset_h3, subset_h4, subset_h5, subset_h6])
    title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " +
                 "hrs: " + str(hour_sel1) + ", " + str(hour_sel2) + ", " + str(hour_sel3) +
                 ", " + str(hour_sel4) + ", " + str(hour_sel5) + ", " + str(hour_sel6))
else:
    st.write("choose up to 6 hours")

if y_axis1 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis2 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis3 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis4 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis5 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis6 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
else:
    st.write("check logic error 1")

if y_axis1 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))
elif y_axis2 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))
elif y_axis3 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))
elif y_axis4 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))
elif y_axis5 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))
elif y_axis6 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))
else:
    st.write("check logic error 2")


if len_y_ax == 1:
    fig = px.line(subset, x=x_axis, y=[y_axis1],
                  title=title_var)
    st.plotly_chart(fig)
elif len_y_ax == 2:
    fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2],
                  title=title_var)
    st.plotly_chart(fig)
elif len_y_ax == 3:
    fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2, y_axis3],
                  title=title_var)
    st.plotly_chart(fig)
elif len_y_ax == 4:
    fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2, y_axis3, y_axis4],
                  title=title_var)
    st.plotly_chart(fig)
elif len_y_ax == 5:
    fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2, y_axis3, y_axis4, y_axis5],
                  title=title_var)
    st.plotly_chart(fig)
elif len_y_ax == 6:
    fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2, y_axis3, y_axis4, y_axis5, y_axis6],
                  title=title_var)
    st.plotly_chart(fig)
else:
    st.write("Make the appropriate selections")