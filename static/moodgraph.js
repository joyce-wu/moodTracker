import * d3 from "d3";

var i;
var dates = [];
var moods = [];
for(i = 0; i < d.length; i++){
  dates.push(d[i][0]);
  moods.push(d[i][1]);
}

const margin = 60;
const width = 1000 - 2 * margin;
const height = 600 - 2 * margin;

const svg = d3.select('svg');
const chart = svg.append('g');
  .attr('transform', 'translate(${margin}, ${margin})');

const yScale = d3.scaleLiner()
  .range([height, 0])
  .domain([0, 100]);
chart.append('g')
  .call(d3.axisLeft(yScale));

const xScale = d3.scaleBand()
  .range([0, width])
  .domain(dates)
  .padding(0.2)
chart.append('g')
  .attr('transform', 'translate(0, ${height})')
  .call(d3.axisBottom(xScale));

chart.selectAll()
  .data(d)
  .enter()
  .append('rect')
  .attr('x', dates)
  .attr('y', moods)
  .attr('height', height - yScale(moods))
  .attr('width', xScale.bandwidth());
