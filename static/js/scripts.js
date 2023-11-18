$(document).ready(function () {
    
      // Function to disable weekends
      function disableWeekends(date) {
        var day = date.getDay();
        // Disable weekends (0: Sunday, 6: Saturday)
        return [(day != 0 && day != 6), ''];
      }
    
    $( "#id_demo_date" ).datepicker({
        minDate: 1, // Set the minimum date to today
        dateFormat: 'yy-mm-dd', // Set the date format if needed
        beforeShowDay: disableWeekends, // Call the function to disable weekends,
    });
    $('#id_demo_date').on('click', function(e) {
        e.preventDefault();
        $(this).attr("autocomplete", "off");  
     });
});