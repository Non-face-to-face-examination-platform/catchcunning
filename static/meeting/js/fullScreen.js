const testModOffWarning = document.querySelector("#fullscreen-off-warning");
const testModOnBtn = document.querySelector("#fullscreenOn");
const testModOffBtn = document.querySelector("#fullscreenOff");
const testEndBtn = document.querySelector("#test-end");
const testContBtn = document.querySelector("#test-cont");
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
    testModOffWarning.classList.remove("hidden");
    let countInterval = startCountDown(timer--);

    testEndBtn.addEventListener("click", () => {
      console.log("시험 모드(전체화면 모드) 종료됨.");
      testModOffWarning.classList.add("hidden");
      clearInterval(countInterval);
      alert("시험이 종료되었습니다.");
      document.removeEventListener("fullscreenchange", testModOff);
      document.removeEventListener("visibilitychange", testModOff);
      window.location.replace(main_link);
    });

    testContBtn.addEventListener("click", () => {
      document.documentElement
        .requestFullscreen({ navigationUI: "hide" })
        .catch(console.log);
      testModOffWarning.classList.add("hidden");
      clearInterval(countInterval);
      timer = 3;
    });
  }
}

testModOnBtn.addEventListener("click", () => {
  document.documentElement
    .requestFullscreen({ navigationUI: "hide" })
    .catch(console.log);
  document.addEventListener("fullscreenchange", testModOff);
  document.addEventListener("visibilitychange", testModOff);
  setInterval(function () {
    if (document.hasFocus() == false) {
      alert("탭 변경이 감지되었습니다. 시험이 종료되었습니다.");
      window.location.replace(main_link);
    }
  });
  document.getElementById("exampage").style.display = "";
});

testModOffBtn.addEventListener("click", () => {
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
