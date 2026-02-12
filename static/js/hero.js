function selectHero(hero) {
  const modal = document.getElementById("heroModal");
  const title = document.getElementById("modalTitle");
  const desc = document.getElementById("modalDesc");
  const heroText = document.getElementById("hero-text");

  modal.style.display = "block";

  if (hero === "ironman") {
    title.innerHTML = "IRON MAN";
    desc.innerHTML = "Genius. Billionaire. Hero. Powered by Arc Reactor. Tony Stark uses his intelligence and technology to fight for justice.";
    heroText.innerHTML = "I AM IRON MAN 🔥";
    fireRepulsor();
  }

  if (hero === "thor") {
    title.innerHTML = "THOR";
    desc.innerHTML = "God of Thunder. Wielder of Mjölnir. The Asgardian prince fights to protect Earth and the Nine Realms.";
    heroText.innerHTML = "GOD OF THUNDER ⚡";
  }

  if (hero === "hulk") {
    title.innerHTML = "HULK";
    desc.innerHTML = "Pure strength. Anger equals power. Bruce Banner transforms into the incredible Hulk when enraged.";
    heroText.innerHTML = "HULK SMASH 💪";
  }

  if (hero === "captain") {
    title.innerHTML = "CAPTAIN AMERICA";
    desc.innerHTML = "Super soldier. The first Avenger. Steve Rogers leads with courage and unwavering moral principles.";
    heroText.innerHTML = "AMERICA'S HERO 🛡️";
  }

  if (hero === "black-widow") {
    title.innerHTML = "BLACK WIDOW";
    desc.innerHTML = "Master spy. Lethal assassin turned hero. Natasha Romanoff fights for redemption and justice.";
    heroText.innerHTML = "LETHAL & DEADLY 🤍";
  }

  if (hero === "spider") {
    title.innerHTML = "SPIDER-MAN";
    desc.innerHTML = "Your friendly neighborhood Spider-Man. Peter Parker balances heroism with everyday life.";
    heroText.innerHTML = "WITH GREAT POWER 🕷️";
  }
}

function closeModal() {
  document.getElementById("heroModal").style.display = "none";
}

function logout() {
  if (confirm("Are you sure you want to logout?")) {
    window.location.href = "/";
  }
}

function setMode(mode) {
  const overlay = document.querySelector(".hero-overlay");
  if (mode === "avengers") {
    overlay.style.background = "rgba(0, 71, 171, 0.5)";
    alert("⚡ Avengers Mode Activated!");
  }
  if (mode === "villains") {
    overlay.style.background = "rgba(139, 0, 0, 0.5)";
    alert("👹 Villains Mode Activated!");
  }
}

function fireRepulsor() {
  const blast = document.getElementById("blast");
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

document.addEventListener("DOMContentLoaded", function() {
  console.log("Marvel Heroes page loaded!");
});
