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
});