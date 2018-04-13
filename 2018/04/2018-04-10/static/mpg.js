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
        console.log(response);

        // d3 demo - show when data is being requestd
        d3.selectAll("li").style("color", function () {
            return "hsl(" + Math.random() * 360 + ",100%,50%)";
        });

        // d3 scatter plot
        d3.select("#graph")
            .selectAll('p')
            .data([Math.random(), Math.random(), Math.random()])
            .enter().append("p")
            .text(function (d) {
                return "I’m number " + d + "!";
            });
    }, 1000);
});