const captureBtn = document.getElementById("capture-btn");

function screenshot() {
  html2canvas(document.body)
    .then(function (canvas) {
      let data = canvas.toDataURL("image/png");
      //data = data.replace("data:image/png;base64,", "");
      console.log(data);
      $.ajax({
        type: "POST",
        url: "/sendmail",
        data: { imgSrc: data },
        dataType: "text",
        success: function (result) {
          let filename = result["filename"];
        },
        error: function (e) {
          alert("에러발생");
        },
      });
    })
    .catch(function (err) {
      console.log(err);
    });
}

// function saveAs(uri, filename) {
//     var link = document.createElement('a');
//     if (typeof link.download === 'string') {
//         link.href = uri;
//         link.download = filename;
//         document.body.appendChild(link);
//         link.click();
//         document.body.removeChild(link);
//     } else {
//         window.open(uri);
//     }
// }

captureBtn.addEventListener("click", screenshot);
