# memory_game.html 개발 히스토리 및 코드 변화 정리

## 1. 요구사항 및 주요 프롬프트

- 3x3 구조의 기억력 게임, 가운데는 '14기 파이팅', 나머지 8칸에 목표카드 랜덤 배치
- 목표카드는 4가지(각 2장씩): 목표 기업 설정하기, 서류/면접 컨설팅, 포트폴리오 수정, 데이터 기반 프로젝트 경험
- 카드 짝 맞추기, 두 장이 일치하면 유지, 다르면 다시 가려짐
- 모든 카드 매칭 시 폭죽 효과와 클리어 시간 표시, 시간 제한(20초) 기능
- 파스텔톤 배경 및 카드, 외부 라이브러리 사용 금지

## 2. 코드 변화 및 시행착오

### (1) 카드 클릭 이벤트 및 상태 관리

- 클릭 가능 조건: center가 아니고, matched가 아니고, flipped가 아니고, lock이 아니고, gameEnded가 아니어야 함
- 카드 클릭 시 onCardClick에서 상태를 변경하고, render()로 화면 갱신
- 두 번째 카드 선택 시 lock을 걸고, setTimeout으로 checkMatch 실행

```javascript
function render() {
    grid.innerHTML = '';
    cards.forEach((card, idx) => {
        const div = document.createElement('div');
        div.className = 'card' + (card.center ? ' center' : '') + (card.flipped ? ' flipped' : '') + (card.matched ? ' matched' : '');
        div.textContent = card.flipped || card.center || card.matched ? card.text : '';
        if (!card.center && !card.flipped && !card.matched && !gameEnded && !lock) {
            div.addEventListener('click', () => onCardClick(idx));
        }
        grid.appendChild(div);
    });
}

function onCardClick(idx) {
    if (lock || cards[idx].flipped || cards[idx].matched || gameEnded) return;
    cards[idx].flipped = true;
    if (firstCard === null) {
        firstCard = idx;
        render();
    } else {
        secondCard = idx;
        lock = true;
        render();
        setTimeout(checkMatch, 700);
    }
}
```

### (2) checkMatch 함수 동작
- 두 카드의 text가 같으면 matched 처리, 다르면 다시 뒤집음
- matchedCount가 8이 되면 게임 종료 및 축하 메시지/폭죽 효과/클리어 시간 표시

```javascript
function checkMatch() {
    if (cards[firstCard].text === cards[secondCard].text) {
        cards[firstCard].matched = true;
        cards[secondCard].matched = true;
        matchedCount += 2;
    } else {
        cards[firstCard].flipped = false;
        cards[secondCard].flipped = false;
    }
    firstCard = null;
    secondCard = null;
    lock = false;
    if (matchedCount === 8) {
        showFireworks();
        document.getElementById('timer').textContent = '축하합니다!';
        // 클리어 시간 표시
    }
    render();
}
```

### (3) 게임 시작/초기화 및 타이머
- 게임 시작 시 카드 생성, 상태 초기화, 3초간 전체 공개 후 lock 해제
- 20초 타이머, 시간 종료 시 게임 종료 처리

```javascript
function startGame() {
    cards = createCards();
    firstCard = null;
    secondCard = null;
    lock = true;
    matchedCount = 0;
    gameEnded = false;
    messageDiv.textContent = '';
    render();
    showAllCards();
    if (previewTimeout) clearTimeout(previewTimeout);
    previewTimeout = setTimeout(() => {
        hideAllCards();
        lock = false;
        firstCard = null;
        secondCard = null;
    }, 3000);
}
```

### (4) 추가 효과 및 UI
- 폭죽 효과: canvas를 이용해 간단한 fireworks 애니메이션 구현
- 클리어 시간: 게임 종료 시 화면 중앙에 클리어 시간 표시
- 타이머: 상단 중앙에 20초 카운트다운 표시, 시간 종료 시 게임 종료

## 3. 결론 및 교훈

- 카드 클릭 이벤트와 상태 관리를 명확히 분리하고, render/lock/gameEnded 등 상태 플래그를 꼼꼼히 관리해야 함
- UI 효과(폭죽, 타이머, 메시지 등)는 게임 로직과 분리하여 구현하면 유지보수가 쉬움
- JS 기반 인터랙션은 이벤트 부여와 상태 관리가 꼬이면 정상 동작하지 않으니, 항상 조건을 명확히 할 것

---

이 문서는 memory_game.html 개발 과정의 시행착오와 최종 해결 방법을 기록한 문서입니다.
