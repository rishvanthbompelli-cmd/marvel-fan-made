 
    // Check session on load
    async function checkSession() {
      try {
        const response = await fetch('/check-session');
        const data = await response.json();
        if (data.authenticated) {
          document.getElementById('logoutItem').style.display = 'block';
          document.getElementById('loginCard').style.display = 'none';
          document.querySelector('.subtitle').textContent = `Welcome back, ${data.user.fullName}!`;
        }
      } catch (e) {
        console.log('Session check failed');
      }
    }

    // Create floating particles
    function createParticles() {
      const container = document.getElementById('particles');
      const particleCount = 50;

      for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 5 + 's';
        particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
        container.appendChild(particle);
      }
    }

    // Lightning effect
    function createLightning() {
      const lightning = document.getElementById('lightning');
      setInterval(() => {
        if (Math.random() > 0.97) {
          lightning.style.opacity = 1;
          lightning.style.transition = 'opacity 0.1s';
          setTimeout(() => {
            lightning.style.opacity = 0;
          }, 100 + Math.random() * 200);
        }
      }, 2000);
    }

    // Initialize
    createParticles();
    createLightning();
    checkSession();

    // Form validation and login
    async function handleLogin(event) {
      event.preventDefault();
      
      const fullName = document.getElementById('fullName').value.trim();
      const emailPhone = document.getElementById('emailPhone').value.trim();
      const favoriteHero = document.getElementById('favoriteHero').value;

      if (!fullName || !emailPhone || !favoriteHero) {
        alert('Please fill in all fields!');
        return;
      }

      try {
        const response = await fetch('/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ fullName, emailPhone, favoriteHero })
        });

        const data = await response.json();

        if (data.success) {
          alert(data.message);
          
          // Save to localStorage if remember me is checked
          if (document.getElementById('rememberMe').checked) {
            localStorage.setItem('marvelUser', JSON.stringify({
              name: fullName,
              hero: favoriteHero
            }));
          }

          window.location.href = '/hero';
        } else {
          alert(data.message);
        }
      } catch (e) {
        alert('Login failed. Please try again.');
      }
    }

    // Logout
    async function handleLogout() {
      try {
        await fetch('/logout', { method: 'POST' });
        localStorage.removeItem('marvelUser');
        window.location.reload();
      } catch (e) {
        console.log('Logout failed');
      }
    }

    // Load saved data
    window.onload = function() {
      const saved = localStorage.getItem('marvelUser');
      if (saved) {
        const data = JSON.parse(saved);
        document.getElementById('fullName').value = data.name || '';
        document.getElementById('favoriteHero').value = data.hero || '';
        document.getElementById('rememberMe').checked = true;
      }
      checkSession();
    };
  