console.log(data);

// Trace for the Roman Data
let trace1 = {
    y: data.map(row => row.New_cases),
    x: data.map(row => row.Date_reported),
    type: "scatter"
};
// Data trace array
let traceData = [trace1];
// Apply title to the layout
let layout = {
  title: "Daily Case Information"
};
// Render the plot
Plotly.newPlot("dailycases", traceData, layout);



// Trace for the Roman Data
let trace2 = {
  y: data.map(row => row.New_deaths),
  x: data.map(row => row.Date_reported),
  type: "scatter"
};
// Data trace array
let traceData2 = [trace2];
// Apply title to the layout
let layout2 = {
title: "Daily Death Information"
};
// Render the plot
Plotly.newPlot("dailydeaths", traceData2, layout2);