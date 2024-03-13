document.getElementById("checkButton").addEventListener("click", async () => {
  const videoUrl = document.getElementById("videoUrl").value.trim();
  const summaryLength = document.getElementById("summaryLength").value;
  if (!videoUrl) {
    alert("Please enter a YouTube video URL.");
    return;
  }

  try {
    const response = await fetch("http://localhost:8000/get_detailed_notes/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ link: videoUrl, length: summaryLength })
    });
    const data = await response.json();
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = `<h5 class="summary-title">Summary:</h5><p class="summary-content">${data.detailed_notes}</p>`;
    resultDiv.style.display = "block";
  } catch (error) {
    console.error("Error:", error);
    alert("An error occurred while summarizing the video.");
  }
});


