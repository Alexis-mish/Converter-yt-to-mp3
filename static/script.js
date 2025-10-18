document.getElementById("convertBtn").addEventListener("click", async () => {
    const url = document.getElementById("url").value.trim();
    const progress = document.getElementById("progress");
    const result = document.getElementById("result");

    if (!url) {
        result.innerHTML = "<p class='text-red-500'>Please enter a valid URL.</p>";
        return;
    }

    progress.classList.remove("hidden");
    result.innerHTML = "";

    try {
        const response = await fetch("/convert", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url })
        });

        const data = await response.json();
        progress.classList.add("hidden");

        if (data.success) {
            result.innerHTML = `
                <p class="text-green-600 font-semibold mb-2">✅ Conversion complete!</p>
                <a href="${data.download}" download="${data.filename}"
                   class="bg-green-500 hover:bg-green-600 text-white py-2 px-4 rounded-lg inline-block">
                   Download MP3
                </a>
            `;
        } else {
            result.innerHTML = `<p class="text-red-500">Error: ${data.error}</p>`;
        }
    } catch (err) {
        progress.classList.add("hidden");
        result.innerHTML = `<p class="text-red-500">Unexpected error: ${err}</p>`;
    }
});
