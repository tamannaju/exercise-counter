(() => {
  const MAX_MB = Number(window.MAX_UPLOAD_MB || 50);
  const MAX_BYTES = MAX_MB * 1024 * 1024;

  const videoInput = document.getElementById("video");
  const clientAlert = document.getElementById("clientAlert");
  const submitBtn = document.getElementById("submitBtn");
  const fileInfo = document.getElementById("fileInfo");
  const uploadForm = document.getElementById("uploadForm");
  const loaderOverlay = document.getElementById("loaderOverlay");

  if (!videoInput || !uploadForm) return;

  function showAlert(msg) {
    if (!clientAlert) return;
    clientAlert.textContent = msg;
    clientAlert.style.display = "block";
  }

  function hideAlert() {
    if (!clientAlert) return;
    clientAlert.textContent = "";
    clientAlert.style.display = "none";
  }

  function bytesToMB(bytes) {
    return (bytes / (1024 * 1024)).toFixed(2);
  }

  videoInput.addEventListener("change", () => {
    hideAlert();
    if (submitBtn) submitBtn.disabled = false;
    if (fileInfo) fileInfo.textContent = "";

    const file = videoInput.files && videoInput.files[0];
    if (!file) return;

    if (fileInfo) fileInfo.textContent = `${file.name} • ${bytesToMB(file.size)} MB`;

    if (file.size > MAX_BYTES) {
      showAlert(`File is too large (${bytesToMB(file.size)} MB). Max allowed is ${MAX_MB} MB.`);
      if (submitBtn) submitBtn.disabled = true;
    }
  });

  uploadForm.addEventListener("submit", (e) => {
    const file = videoInput.files && videoInput.files[0];

    if (file && file.size > MAX_BYTES) {
      e.preventDefault();
      showAlert(`File is too large (${bytesToMB(file.size)} MB). Max allowed is ${MAX_MB} MB.`);
      if (submitBtn) submitBtn.disabled = true;
      return;
    }

    // show loader
    if (loaderOverlay && (!submitBtn || !submitBtn.disabled)) {
      loaderOverlay.style.display = "flex";
    }
  });
})();