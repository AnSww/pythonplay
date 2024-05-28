 // Initialize Ace code editor
var editor = ace.edit("editor");
editor.setTheme("ace/theme/dracula");
editor.getSession().setMode("ace/mode/python");
editor.setFontSize("16px");

// Function to run the code in the Ace editor
function runCode() {
    var code = editor.getValue();
    var input = document.getElementById("input").value; // Get input value

    // Make an AJAX request to the Django server for code execution
    $.ajax({
        type: "POST",
        url: "/run_code/", // URL of your Django view
        headers: {
            'X-CSRFToken': csrftoken // Include CSRF token in the request header
        },
        data: {
            code: code,
            input: input, // Include input data
            language: 'python' // Fixed to Python
        },
        success: function(data) {
            if (data.result) {
                document.getElementById("output").innerText = data.result;
            } else {
                document.getElementById("output").innerText = data.error;
            }
        },
        error: function() {
            document.getElementById("output").innerText = "Error communicating with the server.";
        }
    });
}
