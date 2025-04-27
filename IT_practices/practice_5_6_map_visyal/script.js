 // --- Chart.js --- Створення графіку ---
const ctx = document.getElementById('visitsChart').getContext('2d');
const visitsChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень'],
    datasets: [{
      label: 'Відвідування',
      data: [120, 190, 300, 250, 400],
      backgroundColor: 'rgba(54, 162, 235, 0.7)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Статистика відвідувань за місяцями'
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Кількість'
        }
      }
    }
  }
});

// --- Leaflet.js --- Ініціалізація карти ---
const map = L.map('map').setView([50.4501, 30.5234], 10); // Київ

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap'
}).addTo(map);

// Додаємо маркери на карту
L.marker([50.4501, 30.5234]).addTo(map)
  .bindPopup('Київ: центр міста')
  .openPopup();

L.marker([50.4017, 30.2525]).addTo(map)
  .bindPopup('Аеропорт Бориспіль');

L.marker([50.4547, 30.5238]).addTo(map)
  .bindPopup('Пам\'ятник Богдану Хмельницькому');
