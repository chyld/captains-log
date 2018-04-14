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

    (async function plotter() {
        // fetch data
        const response = await $.ajax('/plotly');
        mpg = response.data.map(a => a[0]);
        weight = response.data.map(a => a[1]);

        // PLOT 1 -------------------------------------------------------------------- //
        // PLOT 1 -------------------------------------------------------------------- //
        // PLOT 1 -------------------------------------------------------------------- //
        // format data
        const trace1 = [{
            x: weight,
            y: mpg,
            mode: 'markers',
            type: 'scatter'
        }];

        // set layout
        const layout1 = {
            xaxis: {
                title: 'Weight'
            },
            yaxis: {
                title: 'MPG'
            },
            title: 'MPG by Weight',
            autosize: false,
            width: 700,
            height: 300,
            margin: {
                l: 50,
                b: 50,
                r: 0,
                t: 40,
                pad: 5
            }
        };

        // plot scatter plot
        Plotly.plot($('#graph1')[0], trace1, layout1);

        // PLOT 2 -------------------------------------------------------------------- //
        // PLOT 2 -------------------------------------------------------------------- //
        // PLOT 2 -------------------------------------------------------------------- //

        var trace2 = [{
            x: mpg,
            type: 'histogram',
        }];

        const layout2 = {
            xaxis: {
                title: 'MPG'
            },
            yaxis: {
                title: 'Count'
            },
            title: 'MPG Histogram'
        };

        // plot histogram
        Plotly.plot($('#graph2')[0], trace2, layout2);
    })();

});