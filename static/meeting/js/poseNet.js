let videos = document.getElementsByClassName("agora_video_player");
let log = document.getElementById("log");

let peopleNumber;
let peopleIdx = 0;

let poses = [];

class setPoseNet {
  constructor(idx) {
    this.idx = idx;
    this.poseNet;
    this.setup(this.idx);
  }

  setup(num) {
    this.poseNet = ml5.poseNet(videos[num], () => {
      console.log(num, "posenet ready");
      let detect_log = document.createElement("h3");
      detect_log.setAttribute("id", "detect" + this.idx);
      log.appendChild(detect_log);
    });
    this.poseNet.on("pose", (results) => {
      // 각 키포인트의 x,y 좌표값 받음
      if (results.length > 0) {
        let leftEar = results[0].pose.leftEar.x;
        let rightEar = results[0].pose.rightEar.x;
        let nose = results[0].pose.nose.x;
        let str = "";
        let border = "";
        if (!(nose < leftEar && nose > rightEar)) {
          // 부정행위 감지 시
          str =
            "<font color=red>[" +
            document.getElementsByClassName("user-name")[this.idx].innerText +
            "]님의 부정행위(고개 돌림)가 감지되었습니다." +
            "</font>";
          border = "solid red";
        }
        document.getElementById("detect" + this.idx).innerHTML = str;
        document.getElementsByClassName("video-container")[
          this.idx
        ].style.border = border;
      }
    });
  }
}

let toggleDetect = async (e) => {
  console.log("TOGGLE DETECT TRIGGERED");
  e.target.style.backgroundColor = "rgb(255, 80, 80, 1)";
  peopleNumber = videos.length;
  for (let i = 0; i < videos.length; i++) {
    videos[i].width = "640";
    videos[i].height = "480";
    new setPoseNet(i);
  }
};

document.getElementById("detecting").addEventListener("click", toggleDetect);
