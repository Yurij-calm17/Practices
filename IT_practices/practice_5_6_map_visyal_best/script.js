let map;
let visitsChart;
let markers = [];
let allData = [];

document.addEventListener('DOMContentLoaded', async () => {
  // Завантаження даних із JSON
  const response = await fetch('data.json');
  allData = await response.json();

  initChart(allData);
  initMap();
  addMarkers(allData);

  // Обробник фільтра
  document.getElementById('monthFilter').addEventListener('change', filterData);
});

function initChart(data) {
  const ctx = document.getElementById('visitsChart').getContext('2d');
  visitsChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: data.map(item => item.month),
      datasets: [{
        label: 'Відвідування',
        data: data.map(() => Math.floor(Math.random() * 300 + 100)), // Генеруємо випадкові дані
        backgroundColor: 'rgba(54, 162, 235, 0.7)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      animation: {
        duration: 1000,
        easing: 'easeOutBounce'
      },
      plugins: {
        title: {
          display: true,
          text: 'Статистика відвідувань за місяцями'
        }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      },
      onClick: (e, elements) => {
        if (elements.length > 0) {
          const index = elements[0].index;
          const selectedData = allData[index];
          map.flyTo(selectedData.coords, 12);
        }
      }
    }
  });
}

function initMap() {
  map = L.map('map').setView([50.4501, 30.5234], 6); // Центр карти

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
  }).addTo(map);
}

function addMarkers(data) {
  // Спочатку видаляємо старі маркери
  markers.forEach(marker => map.removeLayer(marker));
  markers = [];

  data.forEach(item => {
    const marker = L.marker(item.coords)
      .addTo(map)
      .bindPopup(`<b>${item.name}</b><br>${item.info}`);
    markers.push(marker);
  });
}

function filterData() {
  const selectedMonth = document.getElementById('monthFilter').value;

  if (selectedMonth === 'all') {
    updateChart(allData);
    addMarkers(allData);
  } else {
    const filtered = allData.filter(item => item.month === selectedMonth);
    updateChart(filtered);
    addMarkers(filtered);

    if (filtered.length > 0) {
      map.flyTo(filtered[0].coords, 10);
    }
  }
}

function updateChart(data) {
  visitsChart.data.labels = data.map(item => item.month);
  visitsChart.data.datasets[0].data = data.map(() => Math.floor(Math.random() * 300 + 100));
  visitsChart.update();
}
