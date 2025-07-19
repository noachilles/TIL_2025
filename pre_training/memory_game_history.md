# SSAFY 기억력 게임 개발 히스토리 및 코드 변화 정리

## 1. 요구사항 및 주요 프롬프트

- 3x3 구조의 기억력 게임, 가운데는 '14기 파이팅❤️‍🔥', 나머지 8칸에 목표카드 랜덤 배치
- 시작 버튼 클릭 시 3초간 전체 공개 후 뒤집힘
- 두 장 선택 후 일치하면 유지, 다르면 다시 가려짐
- 모든 카드 매칭 시 응원 메시지 출력
- 클릭 잠금(매칭 판정 중에는 다른 카드 클릭 불가)
- 파스텔톤 민트 배경, 카드도 파스텔톤
- 외부 라이브러리 사용 금지

## 2. 코드 변화 및 시행착오

### (1) 카드 클릭 이벤트 조건의 변화

#### 초기 시도
- 클릭 가능 조건을 너무 엄격하게 설정(`!card.center && !card.matched && !lock && !gameEnded && !card.flipped`)
- 이미 뒤집힌 카드에는 클릭 이벤트가 아예 부여되지 않아, 카드가 다시 뒤집히지 않음

#### 문제점
- 카드가 한 번 뒤집힌 후에는 클릭 이벤트가 없어져서, 정상적인 게임 진행이 불가

#### 개선 시도
- robust하게 조건을 바꿔도, 여전히 카드가 뒤집힌 상태에서는 클릭 이벤트가 부여되지 않아, 동작이 불안정함

### (2) 최종 해결
- center(가운데) 카드를 제외한 모든 카드에 클릭 이벤트를 항상 부여
- 실제 동작은 onCardClick 함수 내부에서 조건(`lock`, `flipped`, `matched`, `gameEnded`)을 체크하여 처리

```javascript
// render 함수 내
cards.forEach((card, idx) => {
    const div = document.createElement('div');
    div.className = 'card' + (card.center ? ' center' : '') + (card.flipped ? ' flipped' : '') + (card.matched ? ' matched' : '');
    div.textContent = card.flipped || card.center || card.matched ? card.text : '';
    // center만 제외하고 모든 카드에 클릭 이벤트 부여
    if (!card.center) {
        div.addEventListener('click', () => onCardClick(idx));
    }
    grid.appendChild(div);
});

// onCardClick 함수 내
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
        setTimeout(() => {
            checkMatch();
        }, 700);
    }
}
```

### (3) checkMatch 함수 동작
- 두 카드의 text가 같으면 matched 처리, 다르면 다시 뒤집음
- matchedCount가 8이 되면 게임 종료 및 응원 메시지 출력

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
        messageDiv.textContent = 'SSAFY가 목표를 이룰 수 있도록 항상 응원하겠습니다.❤️';
        gameEnded = true;
    }
    render();
}
```

## 3. 결론 및 교훈

- 카드 클릭 이벤트는 항상 부여하고, 실제 동작은 onCardClick 내부에서 제어하는 것이 가장 견고함
- 렌더링/상태관리/이벤트 부여의 책임을 명확히 분리해야 JS 기반 인터랙션이 안정적으로 동작함
- 게임 로직은 단순하지만, 이벤트 부여와 상태 관리가 꼬이면 정상 동작하지 않으니 주의해야 함

---

이 문서는 SSAFY 기억력 게임 개발 과정의 시행착오와 최종 해결 방법을 기록한 문서입니다.
