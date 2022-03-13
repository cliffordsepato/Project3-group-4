console.log(data);

// Create a custom function to return Roman gods with more than 1 million search results
function highcases(cases) {
  return cases.Cumulative_cases > 6200000;
}
// Call the custom function with filter()
let highestcases = data.filter(highcases);
// Trace for the Roman Data
let trace1 = {
    y: highestcases.map(row => row.Cumulative_cases),
    x: highestcases.map(row => row.Country),
    type: "bar"
};
// Data trace array
let traceData = [trace1];
// Apply title to the layout
let layout = {
  title: "Highest number of cases"
};
// Render the plot
Plotly.newPlot("topcases", traceData, layout);




// Create a custom function to return Roman gods with more than 1 million search results
function highdeaths(deaths) {
  return deaths.Cumulative_deaths > 130000;
}
// Call the custom function with filter()
let highestdeaths = data.filter(highdeaths);
// Trace for the Roman Data
let trace2 = {
    y: highestdeaths.map(row => row.Cumulative_deaths),
    x: highestdeaths.map(row => row.Country),
    type: "bar"
};
// Data trace array
let traceData2 = [trace2];
// Apply title to the layout
let layout2 = {
  title: "Highest number of deaths"
};
// Render the plot
Plotly.newPlot("topdeaths", traceData2, layout2);




// Create a custom function to return Roman gods with more than 1 million search results
function highvaccines(vaccines) {
  return vaccines.TOTAL_VACCINATIONS > 170000000;
}
// Call the custom function with filter()
let highestvaccines = data.filter(highvaccines);
// Trace for the Roman Data
let trace3 = {
    y: highestvaccines.map(row => row.TOTAL_VACCINATIONS),
    x: highestvaccines.map(row => row.Country),
    type: "bar"
};
// Data trace array
let traceData3 = [trace3];
// Apply title to the layout
let layout3 = {
  title: "Highest number of administered vaccines"
};
// Render the plot
Plotly.newPlot("topvaccines", traceData3, layout3);