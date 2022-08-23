let videos = document.getElementsByClassName("agora_video_player");
// let canvas = document.getElementById("canvas");
// let ctx = canvas.getContext("2d");
// let ctxIdx = 0;
let log = document.getElementById("log");

let peopleNumber;
let peopleIdx = 0;

// let poseNet = [];
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
  /* 시간 남으면 원하는 사람으로 바꿀 수 있게 */
  // setCtx();
  // setInterval(function () {
  //   ctxIdx = (ctxIdx + 1) % peopleNumber;
  // }, 10000);
};

/* 아래는 캔버스에 비디오 및 키포인트,스켈레톤 그리는 함수들 */
function setCtx() {
  canvas.width = "640";
  canvas.height = "480";
  drawCameraIntoCanvas();
}

function drawKeypoints() {
  // Loop through all the poses detected
  for (let i = 0; i < poses.length; i += 1) {
    // For each pose detected, loop through all the keypoints
    for (let j = 0; j < poses[i].pose.keypoints.length; j += 1) {
      let keypoint = poses[i].pose.keypoints[j];
      // Only draw an ellipse is the pose probability is bigger than 0.2
      if (keypoint.score > 0.2) {
        ctx.beginPath();
        ctx.strokeStyle = "red";
        ctx.fillStyle = "white";
        ctx.arc(keypoint.position.x, keypoint.position.y, 10, 0, 20 * Math.PI);
        ctx.fill();
        ctx.stroke();
      }
    }
  }
}

function drawSkeleton() {
  // Loop through all the skeletons detected
  for (let i = 0; i < poses.length; i += 1) {
    // For every skeleton, loop through all body connections
    for (let j = 0; j < poses[i].skeleton.length; j += 1) {
      let partA = poses[i].skeleton[j][0];
      let partB = poses[i].skeleton[j][1];
      // console.log("partA : ", partA.position);
      // console.log("partB : ", partB.position);

      ctx.beginPath();
      ctx.moveTo(partA.position.x, partA.position.y);
      ctx.lineTo(partB.position.x, partB.position.y);
      ctx.lineWidth = 5;
      ctx.strokeStyle = "red";
      ctx.stroke();
    }
  }
}

function drawCameraIntoCanvas() {
  // Draw the video element into the canvas
  ctx.drawImage(
    videos[ctxIdx],
    0,
    0,
    videos[ctxIdx].width,
    videos[ctxIdx].height
  );
  // We can call both functions to draw all keypoints and the skeletons
  if (ctxIdx == peopleIdx) {
    drawSkeleton();
    drawKeypoints();
  }
  window.requestAnimationFrame(drawCameraIntoCanvas);
}

document.getElementById("detecting").addEventListener("click", toggleDetect);
