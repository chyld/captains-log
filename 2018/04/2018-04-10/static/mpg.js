$(document).ready(function () {
    $('#inference').click(async function () {
        const cylinders = parseFloat($('#cylinders').val());
        const horsepower = parseFloat($('#horsepower').val());
        const weight = parseFloat($('#weight').val());
        const data = {
            cylinders,
            horsepower,
            weight
        }
        const response = await $.ajax('/inference', {
            data: JSON.stringify(data),
            method: 'post',
            contentType: 'application/json'
        });
        $('#mpg').val(response);
    });

    setTimeout(async function () {
        // fetch data
        const response = await $.ajax('/d3');
        data = response.data.map(a => ({
            mpg: a[0],
            weight: a[1]
        }));
        console.log(data);

        // d3 demo - show when data is being requestd
        d3.selectAll("li").style("color", function () {
            return "hsl(" + Math.random() * 360 + ",100%,50%)";
        });

        [svgWidth, svgHeight] = [725, 325];
        const svg = d3.select('#graph')
            .attr("width", svgWidth)
            .attr("height", svgHeight);

        const maxMpg = 50;
        const [minWeight, maxWeight] = [1500, 4500];
        // const scaleY = svgHeight / maxMpg;
        // const scaleX = svgWidth / (maxWeight - minWeight);

        const circleGroup = svg.append('g')
            .attr('fill', '#ffcc33')
            .attr('stroke', '#005500')
            .attr('stroke-width', '1px');

        // circleGroup.selectAll('circle')
        //     .data(data)
        //     .enter()
        //     .append('circle')
        //     .attr('cx', d => (d.weight - minWeight) * scaleX)
        //     .attr('cy', d => svgHeight - (d.mpg * scaleY))
        //     .attr('r', d => 5);

        // -------------------------------------------------------------------------------- //
        // -------------------------------------------------------------------------------- //
        // -------------------------------------------------------------------------------- //

        var xScale = d3.scaleLinear()
            .domain([minWeight, maxWeight])
            .range([25, svgWidth]);
        var xAxis = d3.axisBottom()
            .scale(xScale);
        svg.append("g")
            .attr("transform", "translate(0, " + (svgHeight - 25) + ")")
            .call(xAxis);

        var yScale = d3.scaleLinear()
            .domain([0, maxMpg])
            .range([0, svgHeight - 25]);
        var yAxis = d3.axisLeft()
            .scale(yScale);
        svg.append("g")
            .attr("transform", "translate(25, 0)")
            .call(yAxis);

        // -------------------------------------------------------------------------------- //
        // -------------------------------------------------------------------------------- //
        // -------------------------------------------------------------------------------- //

    }, 1000);
});