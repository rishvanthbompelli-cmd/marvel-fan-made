// Toggle mobile menu
function toggleMenu() {
  document.querySelector('.nav-links').classList.toggle('active');
}

// Handle logout
function handleLogout() {
  window.location.href = '/logout';
}

// Handle logout (with confirmation)
function logout() {
  if (confirm("Are you sure you want to logout?")) {
    window.location.href = "/logout";
  }
}

// Fire repulsor effect (for hero detail page)
function fireRepulsor() {
  const blast = document.getElementById("blast");
  if (!blast) return;
  
  blast.style.opacity = "1";
  blast.style.width = "20px";
  blast.style.height = "20px";
  blast.style.boxShadow = "0 0 30px cyan";
  let size = 20;
  const blastInterval = setInterval(() => {
    size += 10;
    blast.style.width = size + "px";
    blast.style.height = size + "px";
    blast.style.boxShadow = "0 0 " + size + "px cyan";
  }, 30);
  setTimeout(() => {
    clearInterval(blastInterval);
    blast.style.opacity = "0";
  }, 600);
}

// Set mode (legacy function)
function setMode(mode) {
  console.log("Mode set to:", mode);
}
