// static/script.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('FlowFin - Revolutionizing Consumer Finance');

    // Example: Display a dynamic clock
    const clockElement = document.getElementById('clock');
    if (clockElement) {
        function updateClock() {
            const currentTime = new Date();
            const hours = currentTime.getHours();
            const minutes = currentTime.getMinutes();
            const seconds = currentTime.getSeconds();

            const formattedTime = `${hours}:${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
            clockElement.textContent = formattedTime;
        }

        setInterval(updateClock, 1000); // Update every second
        updateClock(); // Initial update
    }

    // Example: Create a responsive navigation menu
    const menuToggle = document.getElementById('menuToggle');
    const navigationMenu = document.getElementById('navigationMenu');
    if (menuToggle && navigationMenu) {
        menuToggle.addEventListener('click', function() {
            navigationMenu.classList.toggle('visible');
        });

        // Close the navigation menu when a menu item is clicked (for small screens)
        const menuItems = document.querySelectorAll('.menu-item');
        menuItems.forEach(function(item) {
            item.addEventListener('click', function() {
                if (window.innerWidth <= 768) {
                    navigationMenu.classList.remove('visible');
                }
            });
        });

        // Close the navigation menu when clicking outside it (for small screens)
        document.addEventListener('click', function(event) {
            if (window.innerWidth <= 768 && !navigationMenu.contains(event.target) && !menuToggle.contains(event.target)) {
                navigationMenu.classList.remove('visible');
            }
        });
    }

    // Example: Highlight and copy text on button click
    const copyButton = document.getElementById('copyButton');
    const textToCopy = document.getElementById('textToCopy');
    if (copyButton && textToCopy) {
        copyButton.addEventListener('click', function() {
            textToCopy.select();
            document.execCommand('copy');
            console.log('Text copied:', textToCopy.value);
        });
    }

});

// Add more JavaScript code as needed for your application
