$(document).ready(function() {
    function fetchFlightStatus() {
        $.get('/api/flight-status', function(data) {
            $('#flight-status').html(JSON.stringify(data));
        });
    }
    fetchFlightStatus();
    setInterval(fetchFlightStatus, 60000); // Update every minute
});
