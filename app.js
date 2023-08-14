(async function () {
  // Fetch download link of the latest version.
  const { url: downloadLink } = await fetch("update.json")
    .then((response) => response.json())
    .catch(console.error);
  document.querySelector("#download-link").setAttribute("href", downloadLink);
})();
