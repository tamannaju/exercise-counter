(() => {
  let countInterval = null;
  let isStreaming = false;

  const statusDot = document.getElementById('statusDot');
  const statusText = document.getElementById('statusText');
  const feedBadge = document.getElementById('feedBadge');

  const startBtn = document.getElementById('startBtn');
  const stopBtn = document.getElementById('stopBtn');
  const exerciseSelect = document.getElementById('exerciseSelect');
  const videoFeed = document.getElementById('videoFeed');
  const countDisplay = document.getElementById('countDisplay');

  function setStatus(streaming) {
    if (!statusDot || !statusText || !feedBadge) return;
    if (streaming) {
      statusDot.classList.add('live');
      statusText.textContent = 'Live';
      feedBadge.textContent = 'Streaming';
    } else {
      statusDot.classList.remove('live');
      statusText.textContent = 'Idle';
      feedBadge.textContent = 'Not streaming';
    }
  }

  function updateCount() {
    if (!isStreaming) return;

    fetch('/get_count')
      .then(r => r.json())
      .then(data => {
        if (countDisplay) countDisplay.textContent = data.count;
      })
      .catch(() => {});
  }

  function startFeed() {
    const exercise = exerciseSelect.value;

    videoFeed.src = `/video_feed/${exercise}`;
    videoFeed.style.display = 'block';

    startBtn.disabled = true;
    stopBtn.disabled = false;
    exerciseSelect.disabled = true;

    isStreaming = true;
    setStatus(true);

    if (countDisplay) countDisplay.textContent = '0';
    countInterval = setInterval(updateCount, 500);
  }

  function stopFeed() {
    fetch('/stop_feed').catch(() => {});

    videoFeed.style.display = 'none';
    videoFeed.src = '';

    startBtn.disabled = false;
    stopBtn.disabled = true;
    exerciseSelect.disabled = false;

    isStreaming = false;
    setStatus(false);

    if (countInterval) {
      clearInterval(countInterval);
      countInterval = null;
    }
  }

  // Wire buttons
  if (startBtn) startBtn.addEventListener("click", startFeed);
  if (stopBtn) stopBtn.addEventListener("click", stopFeed);

  // Clean up on page unload
  window.addEventListener('beforeunload', function() {
    if (isStreaming) {
      navigator.sendBeacon('/stop_feed');
    }
  });

  setStatus(false);
})();