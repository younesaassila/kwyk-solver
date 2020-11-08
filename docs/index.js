const md = window.markdownit();
const downloadButton = document.getElementById("download-button");
const gitHubButton = document.getElementById("github-button");
const main = document.getElementById("main");

//#region Download button

const dlUrlRequest = new XMLHttpRequest();
dlUrlRequest.onreadystatechange = () => {
  if (dlUrlRequest.readyState == 4 && dlUrlRequest.status == 200) {
    const url = JSON.parse(dlUrlRequest.responseText).url;
    downloadButton.addEventListener("click", () => {
      location.href = url;
    });
  }
};
dlUrlRequest.open("GET", "update_info.json", true);
dlUrlRequest.send();

//#endregion

//#region Main, README

const readMeRequest = new XMLHttpRequest();
readMeRequest.onreadystatechange = () => {
  if (readMeRequest.readyState == 4 && readMeRequest.status == 200) {
    const html = md.render(readMeRequest.responseText);
    main.innerHTML = html;
  }
};
readMeRequest.open(
  "GET",
  "https://raw.githubusercontent.com/younesaassila/Kwyk-Solver/main/README.md",
  true
);
readMeRequest.send();

//#endregion

//#region GitHub button

gitHubButton.addEventListener("click", () => {
  location.href = "https://github.com/younesaassila/Kwyk-Solver";
});

//#endregion
