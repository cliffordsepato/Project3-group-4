console.log(data);

// Greek god names
names = data.map(function (row){
  return row.WHO_REGION
});

// Trace for the Greek Data
let trace1 = {
    x: data.map(row => row.WHO_REGION),
    y: data.map(row => row.TOTAL_VACCINATIONS),
    type: "bar"
  };

// Data trace array
let traceData = [trace1];

// Apply the group barmode to the layout
let layout = {
  title: "Greek gods search results"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", traceData, layout);
