/**
 * mywebscript.js
 * Calls the /emotionDetector endpoint and displays the result.
 */
function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            document.getElementById("output").innerHTML = this.responseText;
        }
    };
    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
        true
    );
    xhttp.send();
}
