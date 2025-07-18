let emptyCount = 0;
let emptyPositions = [];
let seatGrid = [];
let names = [];
let row = 0, col = 0;
let fileSelected = false;

window.onload = function() {
  document.getElementById('row').addEventListener('input', updateGrid);
  document.getElementById('col').addEventListener('input', updateGrid);
  document.getElementById('file').addEventListener('change', handleFileSelect);
  document.querySelector('.file-label').onclick = function() {
    document.getElementById('file').click();
  };
  document.getElementById('arrange-btn').disabled = true;
  resizeBubbleCanvas();
  window.addEventListener('resize', resizeBubbleCanvas);
};

function handleFileSelect(e) {
  const fileInput = document.getElementById('file');
  const fileLabelText = document.getElementById('file-label-text');
  if (fileInput.files.length > 0) {
    fileLabelText.textContent = fileInput.files[0].name;
    fileSelected = true;
  } else {
    fileLabelText.textContent = "학생 명단 선택";
    fileSelected = false;
  }
  updateGrid();
}

function updateGrid() {
  row = parseInt(document.getElementById('row').value);
  col = parseInt(document.getElementById('col').value);
  const fileInput = document.getElementById('file');
  const seatArea = document.getElementById('seat-area');
  seatArea.innerHTML = '';
  emptyPositions = [];
  seatGrid = [];
  names = [];

  if (!row || !col || !fileSelected) {
    document.getElementById('countdown').innerText = '';
    document.getElementById('arrange-btn').disabled = true;
    return;
  }

  const reader = new FileReader();
  reader.onload = function(e) {
    names = e.target.result.split('\n').map(x => x.trim()).filter(x => x);
    const totalSeats = row * col;
    emptyCount = totalSeats - names.length;
    if (emptyCount < 0) {
      document.getElementById('countdown').innerText = '모두 앉을 수 없습니다!';
      document.getElementById('arrange-btn').disabled = true;
      return;
    }
    if (emptyCount === 0) {
      document.getElementById('countdown').innerText = '빈 자리가 없습니다!';
      document.getElementById('arrange-btn').disabled = false;
      drawFinalSeats([...(Array(row)).keys()].map(() => Array(col).fill('')));
      return;
    }
    drawEmptySeatGrid(row, col, emptyCount);
  };
  reader.readAsText(fileInput.files[0]);
}

function drawEmptySeatGrid(row, col, emptyCount) {
  const seatArea = document.getElementById('seat-area');
  seatArea.innerHTML = '';

  // 스크린 박스 추가
  const screenDiv = document.createElement('div');
  screenDiv.style.textAlign = 'center';
  screenDiv.style.marginBottom = '18px';
  screenDiv.innerHTML = `<span style="
    display:inline-block;
    background:#e3f2fd;
    color:#1976d2;
    font-weight:bold;
    font-size:1.4rem;
    border-radius:12px;
    padding:10px 60px;
    box-shadow:0 2px 8px #b3e5fc;
    border:2px solid #90caf9;
    ">스크린</span>`;
  seatArea.appendChild(screenDiv);

  document.getElementById('countdown').innerText = `빈 자리 ${emptyPositions.length}/${emptyCount} 선택`;
  seatGrid = [];
  emptyPositions = [];
  document.getElementById('arrange-btn').disabled = true;
  for (let r = 0; r < row; r++) {
    let rowArr = [];
    const rowDiv = document.createElement('div');
    rowDiv.className = 'seat-row';
    for (let c = 0; c < col; c++) {
      const seatDiv = document.createElement('div');
      seatDiv.className = 'seat';
      seatDiv.innerText = '';
      seatDiv.onclick = function() {
        if (seatDiv.classList.contains('empty')) {
          seatDiv.classList.remove('empty');
          emptyPositions = emptyPositions.filter(pos => !(pos[0] === r && pos[1] === c));
        } else if (emptyPositions.length < emptyCount) {
          seatDiv.classList.add('empty');
          emptyPositions.push([r, c]);
        }
        document.getElementById('countdown').innerText = `빈 자리 ${emptyPositions.length}/${emptyCount} 선택`;
        document.getElementById('arrange-btn').disabled = (emptyPositions.length !== emptyCount);
      };
      rowArr.push(seatDiv);
      rowDiv.appendChild(seatDiv);
    }
    seatGrid.push(rowArr);
    seatArea.appendChild(rowDiv);
  }
}

function startArrangement() {
  if (emptyCount > 0 && emptyPositions.length !== emptyCount) {
    alert('빈 자리를 모두 선택하세요!');
    return;
  }
  // 오버레이 및 카운트다운
  const overlay = document.getElementById('overlay');
  const overlayCount = document.getElementById('overlay-count');
  overlay.classList.add('active');
  startBubbleAnimation();

  let count = 3;
  showCount(count);
  const timer = setInterval(() => {
    count--;
    if (count > 0) {
      showCount(count);
    } else {
      clearInterval(timer);
      overlay.classList.remove('active');
      overlayCount.innerHTML = '';
      stopBubbleAnimation();
      eel.arrange_seats(names, row, col, emptyPositions)(function(seats) {
        drawFinalSeats(seats);
      });
    }
  }, 900);
}

function showCount(count) {
  const overlayCount = document.getElementById('overlay-count');
  overlayCount.innerHTML = count;
  overlayCount.style.animation = 'none';
  // 강제로 리플로우
  void overlayCount.offsetWidth;
  overlayCount.style.animation = null;
}

function drawFinalSeats(seats) {
  const seatArea = document.getElementById('seat-area');
  seatArea.innerHTML = '';
  seats.forEach(rowArr => {
    const rowDiv = document.createElement('div');
    rowDiv.className = 'seat-row';
    rowArr.forEach(name => {
      const seatDiv = document.createElement('div');
      seatDiv.className = 'seat' + (name === "(빈 자리)" ? " empty" : "");
      seatDiv.innerText = name;
      rowDiv.appendChild(seatDiv);
    });
    seatArea.appendChild(rowDiv);
  });
}

// --- Bubble Animation ---
let bubbleAnimationId = null;
let bubbles = [];

function resizeBubbleCanvas() {
  const canvas = document.getElementById('bubble-canvas');
  if (canvas) {
    canvas.width = overlayWidth();
    canvas.height = overlayHeight();
  }
}

function overlayWidth() {
  const overlay = document.getElementById('overlay');
  return overlay ? overlay.offsetWidth : 1280;
}
function overlayHeight() {
  const overlay = document.getElementById('overlay');
  return overlay ? overlay.offsetHeight : 900;
}

function startBubbleAnimation() {
  const canvas = document.getElementById('bubble-canvas');
  resizeBubbleCanvas();
  bubbles = [];
  for (let i = 0; i < 18; i++) {
    bubbles.push({
      x: Math.random() * canvas.width,
      y: -Math.random() * 200,
      r: 24 + Math.random() * 32,
      speed: 2 + Math.random() * 2,
      alpha: 0.5 + Math.random() * 0.5
    });
  }
  function animate() {
    canvas.width = overlayWidth();
    canvas.height = overlayHeight();
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let b of bubbles) {
      ctx.globalAlpha = b.alpha;
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
      ctx.fillStyle = "#b3e5fc";
      ctx.fill();
      b.y += b.speed;
      if (b.y - b.r > canvas.height) {
        b.x = Math.random() * canvas.width;
        b.y = -b.r;
        b.r = 24 + Math.random() * 32;
        b.speed = 2 + Math.random() * 2;
        b.alpha = 0.5 + Math.random() * 0.5;
      }
    }
    ctx.globalAlpha = 1.0;
    bubbleAnimationId = requestAnimationFrame(animate);
  }
  animate();
}

function stopBubbleAnimation() {
  if (bubbleAnimationId) {
    cancelAnimationFrame(bubbleAnimationId);
    bubbleAnimationId = null;
  }
  const canvas = document.getElementById('bubble-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }
}

// ... 기존 코드 위에 추가 ...
let fireworkAnimationId = null;
let fireworks = [];

// 폭죽 파티클 생성 함수
function startFirework(callback) {
  const canvas = document.getElementById('bubble-canvas');
  resizeBubbleCanvas();
  fireworks = [];
  for (let i = 0; i < 7; i++) {
    const angle = (Math.PI * 2 * i) / 7;
    fireworks.push({
      x: canvas.width / 2,
      y: canvas.height / 2,
      vx: Math.cos(angle) * (6 + Math.random() * 2),
      vy: Math.sin(angle) * (6 + Math.random() * 2),
      color: `hsl(${Math.floor(Math.random() * 360)},90%,60%)`,
      alpha: 1,
      r: 8 + Math.random() * 8
    });
  }
  let frame = 0;
  function animate() {
    canvas.width = overlayWidth();
    canvas.height = overlayHeight();
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let f of fireworks) {
      ctx.save();
      ctx.globalAlpha = f.alpha;
      ctx.beginPath();
      ctx.arc(f.x, f.y, f.r, 0, Math.PI * 2);
      ctx.fillStyle = f.color;
      ctx.shadowColor = f.color;
      ctx.shadowBlur = 18;
      ctx.fill();
      ctx.restore();
      f.x += f.vx;
      f.y += f.vy;
      f.vy += 0.2; // gravity
      f.alpha -= 0.025;
    }
    fireworks = fireworks.filter(f => f.alpha > 0);
    fireworkAnimationId = requestAnimationFrame(animate);
    frame++;
    if (frame > 40) { // 약 1초 후 종료
      stopFirework();
      if (callback) callback();
    }
  }
  animate();
}

function stopFirework() {
  if (fireworkAnimationId) {
    cancelAnimationFrame(fireworkAnimationId);
    fireworkAnimationId = null;
  }
  const canvas = document.getElementById('bubble-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }
}

// ... startArrangement 함수 수정 ...
function startArrangement() {
  if (emptyCount > 0 && emptyPositions.length !== emptyCount) {
    alert('빈 자리를 모두 선택하세요!');
    return;
  }
  // 오버레이 및 카운트다운
  const overlay = document.getElementById('overlay');
  const overlayCount = document.getElementById('overlay-count');
  overlay.classList.add('active');
  startBubbleAnimation();

  let count = 3;
  showCount(count);
  const timer = setInterval(() => {
    count--;
    if (count > 0) {
      showCount(count);
    } else {
      clearInterval(timer);
      overlayCount.innerHTML = '';
      stopBubbleAnimation();
      // 폭죽 애니메이션 후 좌석 배치
      startFirework(() => {
        overlay.classList.remove('active');
        eel.arrange_seats(names, row, col, emptyPositions)(function(seats) {
          drawFinalSeats(seats);
        });
      });
    }
  }, 900);
}

// ... drawFinalSeats 함수 수정 ...
function drawFinalSeats(seats) {
  const seatArea = document.getElementById('seat-area');
  seatArea.innerHTML = '';
  // 스크린 박스 추가
  const screenDiv = document.createElement('div');
  screenDiv.style.textAlign = 'center';
  screenDiv.style.marginBottom = '18px';
  screenDiv.innerHTML = `<span style="
    display:inline-block;
    background:#e3f2fd;
    color:#1976d2;
    font-weight:bold;
    font-size:1.4rem;
    border-radius:12px;
    padding:10px 60px;
    box-shadow:0 2px 8px #b3e5fc;
    border:2px solid #90caf9;
    ">스크린</span>`;
  seatArea.appendChild(screenDiv);

  seats.forEach(rowArr => {
    const rowDiv = document.createElement('div');
    rowDiv.className = 'seat-row';
    rowArr.forEach(name => {
      const seatDiv = document.createElement('div');
      seatDiv.className = 'seat' + (name === "(빈 자리)" ? " empty" : "");
      seatDiv.innerText = name;
      rowDiv.appendChild(seatDiv);
    });
    seatArea.appendChild(rowDiv);
  });
}