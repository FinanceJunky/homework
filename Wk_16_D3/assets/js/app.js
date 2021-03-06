// @TODO: YOUR CODE HERE!
var svgWidth = 960;
var svgHeight = 500;

var margin = {
    top: 20,
    right: 40,
    bottom: 80,
    left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Initial Params
var chosenXAxis = "poverty";

// function used for updating x-scale var upon click on axis label
function xScale(povData, chosenXAxis) {
  // create scales
  var xLinearScale = d3.scaleLinear()
    .domain([d3.min(povData, d => d[chosenXAxis]) * 0.8,
      d3.max(povData, d => d[chosenXAxis]) * 1.2
    ])
    .range([0, width]);

  return xLinearScale;

}

// function used for updating xAxis var upon click on axis label
function renderAxes(newXScale, xAxis) {
  var bottomAxis = d3.axisBottom(newXScale);

  xAxis.transition()
    .duration(1000)
    .call(bottomAxis);

  return xAxis;
}

// function used for updating circles group with a transition to
// new circles
function renderCircles(circlesGroup, newXScale, chosenXaxis) {

    chartGroup.transition()
    .duration(1000)
    .attr("cx", d => newXScale(d[chosenXAxis]));

  return circlesGroup;
}

// Import Data
d3.csv("assets/data/data.csv").then(function(povData, err) {
    if (err) throw err;

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    povData.forEach(function(data) {
        data.poverty = parseFloat(data.poverty);
        data.healthcare = parseFloat(data.healthcare)
        data.obesity = parseFloat(data.obesity);
    });

    // Step 2: Create scale functions
    // ==============================
    var xLinearScale = xScale(povData, chosenXAxis)
        .domain([0, d3.max(povData, d => d[chosenXAxis])])
        .range([0, width]);

    var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(povData, d => d.healthcare) + 5])
        .range([height, 0]);

    // Step 3: Create axis functions
    // ==============================
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Step 4: Append Axes to the chart
    // ==============================
    var xAxis = chartGroup.append("g")
        .classed("x-axis", true)
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis);

    // append y axis    
    chartGroup.append("g")
        .call(leftAxis);

    // Step 5: Create Circles
    // ==============================
    // var nodes = svg.append("g")
    //     .attr("class", "nodes")
    //     .selectAll("circle")
    //     .data(povData)
    //     .enter()
    //     // Add one g element for each data node here.
    //     .append("g")
    //     // Position the g element like the circle element used to be.
    //     .attr("transform", function(d, i) {
    //         return "translate(" + xLinearScale(d.poverty) + "," +
    //             yLinearScale(d.healthcare) + ")";
    //     });

    // nodes.append("circle")
    //     .attr("r", "15")
    //     .attr("fill", "pink")
    //     .attr("opacity", ".5");

    // nodes.append("text")
    //     .attr("text-anchor", "middle")
    //     .text(function(d) {
    //         return d.abbr;
    //     })
    //     .attr('color', 'black')
    //     .attr('font-size', 15);


    var circlesGroup = chartGroup.selectAll("circle")
        .data(povData)
        .enter()
        .append("circle")
        .attr("cx", d => xLinearScale(d[chosenXAxis]))
        .attr("cy", d => yLinearScale(d.healthcare))
        .attr("r", "15")
        .attr("fill", "pink")
        .attr("opacity", ".5");

    // Create group for  2 x- axis labels
    var labelsGroup = chartGroup.append("g")
        .attr("transform", `translate(${width / 2}, ${height + 30})`);
        
    var povertyLabel = labelsGroup.append("text")
        .attr("x", 0)
        .attr("y", 20)
        .attr("value", "poverty") // value to grab for event listener
        .attr("class", "axisText")
        .classed("active", true)
        .text("Sample % in Poverty");

    var obesityLabel = labelsGroup.append("text")
        .attr("x", 0)
        .attr("y", 40)
        .attr("value", "obesity") // value to grab for event listener
        .attr("class", "axisText")
        .classed("inactive", true)
        .text("Sample Obesity %");

    //Step 5.5 add text in circles
    let texts = svg.selectAll(null)
        .data(povData)
        .enter()
        .append('text')
        .text(d => d.abbr)
        .attr('color', 'black')
        .attr('font-size', 15) //BELOW IS A HACK
        .attr("x", d => xLinearScale(d[chosenXAxis]) + 90)
        .attr("y", d => yLinearScale(d.healthcare) + 25);


    // Step 6: Initialize tool tip
    // ==============================
    var toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([80, -60])
        .html(function(d) {
            return (`${d.state}<br>labelsGroup: ${d[chosenXAxis]}%<br>Healthcare: ${d.healthcare}%`);
        });

    // Step 7: Create tooltip in the chart
    // ==============================
    chartGroup.call(toolTip);

    // Step 8: Create event listeners to display and hide the tooltip
    // ==============================
    circlesGroup.on("click", function(data) {
            toolTip.show(data, this);
        })
        // onmouseout event
        .on("mouseout", function(data, index) {
            toolTip.hide(data);
        });
    texts.on("click", function(data) {
            toolTip.show(data, this);
        })
        // onmouseout event
        .on("mouseout", function(data, index) {
            toolTip.hide(data);
        });

    // Create axes labels
    chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left + 40)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .classed("axis-text", true)
        .text("Healthcare %");

    // chartGroup.append("text")
    //     .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    //     .attr("class", "axisText")
    //     .text("Poverty %");

    // updateToolTip function above csv import
    // var circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

      // x axis labels event listener
  labelsGroup.selectAll("text")
  .on("click", function() {
    // get value of selection
    var value = d3.select(this).attr("value");
    if (value !== chosenXAxis) {

      // replaces chosenXAxis with value
      chosenXAxis = value;

      // console.log(chosenXAxis)

      // functions here found above csv import
      // updates x scale for new data
      xLinearScale = xScale(povData, chosenXAxis);

      // updates x axis with transition
      xAxis = renderAxes(xLinearScale, xAxis);

      // updates circles with new x values
      circlesGroup = renderCircles(circlesGroup, xLinearScale, chosenXAxis);

      // updates tooltips with new info
      circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

      // changes classes to change bold text
      if (chosenXAxis === "poverty") {
        povertyLabel
          .classed("active", true)
          .classed("inactive", false);
          obesityLabel
          .classed("active", false)
          .classed("inactive", true);
      }
      else {
        povertyLabel
          .classed("active", false)
          .classed("inactive", true);
          obesityLabel
          .classed("active", true)
          .classed("inactive", false);
      }
    }
  });
}).catch(function(error) {
    console.log(error);
});