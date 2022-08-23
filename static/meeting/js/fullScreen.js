const fullscreenOffWarning = document.querySelector("#fullscreen-off-warning");
const fullscreenOnBtn = document.querySelector("#fullscreenOn");
const fullscreenOffBtn = document.querySelector("#fullscreenOff");
const test_end_btn = document.querySelector("#test-end");
const test_cont_btn = document.querySelector("#test-cont");
const countdown = document.querySelector("#countdown");

const main_link = "https://catchcunning.site";

function startCountDown(timer) {
  let secondsRemaining = timer;

  let countInterval = setInterval(function () {
    countdown.textContent = `${secondsRemaining}초 남았습니다`;
    secondsRemaining = secondsRemaining - 1;
    if (secondsRemaining < 0) {
      clearInterval(countInterval);
      document.exitFullscreen();
      alert("시간 초과로 인하여 시험이 자동 종료되었습니다.");
      document.removeEventListener("fullscreenchange", testModOff);
      document.removeEventListener("visibilitychange", testModOff);
      window.location.replace(main_link);
    }
  }, 1000);

  return countInterval;
}

let timer = 3;
function testModOff() {
  if (!getFullscreenElement() || document.visibilityState != "visible") {
    fullscreenOffWarning.classList.remove("hidden");
    let countInterval = startCountDown(timer--);

    test_end_btn.addEventListener("click", () => {
      console.log("시험 모드(전체화면 모드) 종료됨.");
      fullscreenOffWarning.classList.add("hidden");
      clearInterval(countInterval);
      alert("시험이 종료되었습니다.");
      document.removeEventListener("fullscreenchange", testModOff);
      document.removeEventListener("visibilitychange", testModOff);
      window.location.replace(main_link);
    });

    test_cont_btn.addEventListener("click", () => {
      document.documentElement
        .requestFullscreen({ navigationUI: "hide" })
        .catch(console.log);
      fullscreenOffWarning.classList.add("hidden");
      clearInterval(countInterval);
      timer = 3;
    });
  }
}

fullscreenOnBtn.addEventListener("click", () => {
  document.documentElement
    .requestFullscreen({ navigationUI: "hide" })
    .catch(console.log);
  document.addEventListener("fullscreenchange", testModOff);
  document.addEventListener("visibilitychange", testModOff);
  document.getElementById("exampage").style.display = "";
});

fullscreenOffBtn.addEventListener("click", () => {
  console.log("시험 모드(전체화면 모드) 종료됨.");
  document.exitFullscreen();
  alert("시험이 종료되었습니다.");
  document.removeEventListener("fullscreenchange", testModOff);
  document.removeEventListener("visibilitychange", testModOff);
  window.location.replace(main_link);
});

function getFullscreenElement() {
  return (
    document.fullscreenElement ||
    document.webkitFullscreenElement ||
    document.mozFullscreenElement ||
    document.msFullscreenElemtn
  );
}

document.addEventListener("keydown", function (e) {
  const keyCode = e.keyCode;
  console.log("pushed key " + e.key);
  console.log("keycode : " + keyCode);
});

setInterval(function () {
  if (document.hasFocus() == false) {
    alert("탭 변경이 감지되었습니다. 시험이 종료되었습니다.");
    window.location.replace(main_link);
  }
});
