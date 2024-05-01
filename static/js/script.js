
document.addEventListener("DOMContentLoaded", function() {
    //event listener for submission
    document.getElementById("ppt-form").addEventListener("submit", function(event) {
        //check for empty topic
        var topic = document.getElementById("topic").value.trim();
        if (topic === "") {
            //do not submit if empty
            event.preventDefault();
            //warning
            alert("Please enter a topic for the presentation.");
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('ppt-form');
    const submitButton = document.getElementById('submit-button');
    const loadingSpinner = document.getElementById('loading-spinner');
    //to load loading spinner
    function showLoadingSpinner() {
        loadingSpinner.style.display = 'block';
        submitButton.disabled = true; // Disable submit button
    }

    form.addEventListener('submit', function(event) {
        showLoadingSpinner(); // Show the loading spinner
    });
    
    //hiding spinner for download button
    if (document.querySelector('form[action^="/download/"]')) {
        loadingSpinner.style.display = 'none';
    }
});
