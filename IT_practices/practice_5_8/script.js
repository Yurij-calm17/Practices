// Дані для спрощеного та детального режимів
const simpleData = {
    labels: ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень'],
    datasets: [{
      label: 'Продажі ($)',
      data: [15000, 18000, 17000, 19000, 21000],
      backgroundColor: 'rgba(54, 162, 235, 0.7)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1
    }]
  };
  
  const detailedData = {
    labels: ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень'],
    datasets: [{
      label: 'Продажі ($)',
      data: [15000, 18000, 17000, 19000, 21000],
      backgroundColor: 'rgba(54, 162, 235, 0.7)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1
    }, {
      label: 'Витрати ($)',
      data: [5000, 6000, 5500, 6500, 7000],
      backgroundColor: 'rgba(255, 99, 132, 0.7)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1
    }]
  };
  
  // Створення графіку
  const ctx = document.getElementById('myChart').getContext('2d');
  let myChart = new Chart(ctx, {
    type: 'bar',
    data: simpleData,
    options: {
      plugins: {
        title: {
          display: true,
          text: 'Місячні показники продажів'
        },
        datalabels: {
          color: '#000',
          anchor: 'end',
          align: 'top',
          formatter: (value) => `${value.toLocaleString('uk-UA')}`
        }
      },
      animation: {
        duration: 1000,
        easing: 'easeInOutCubic'
      },
      scales: {
        x: {
          ticks: {
            color: '#333'
          },
          grid: {
            color: 'rgba(0,0,0,0.1)'
          }
        },
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Сума ($)'
          },
          ticks: {
            color: '#333'
          },
          grid: {
            color: 'rgba(0,0,0,0.1)'
          }
        }
      }
    },
    plugins: [ChartDataLabels]
  });
  
  // Функція оновлення кольорів графіка залежно від теми
  function applyThemeToChart() {
    const isDark = document.body.classList.contains('dark-mode');
  
    myChart.options.scales.x.ticks.color = isDark ? '#f1f1f1' : '#333';
    myChart.options.scales.y.ticks.color = isDark ? '#f1f1f1' : '#333';
  
    myChart.options.scales.x.grid.color = isDark ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.1)';
    myChart.options.scales.y.grid.color = isDark ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.1)';
  
    myChart.options.plugins.datalabels.color = isDark ? '#f1f1f1' : '#000';
  
    myChart.update();
  }
  
  // Перемикач режимів (Спрощений/Детальний)
  const simpleBtn = document.getElementById('simpleBtn');
  const detailedBtn = document.getElementById('detailedBtn');
  
  let currentMode = localStorage.getItem('mode') || 'simple';
  updateMode(currentMode);
  
  simpleBtn.addEventListener('click', () => {
    updateMode('simple');
  });
  
  detailedBtn.addEventListener('click', () => {
    updateMode('detailed');
  });
  
  function updateMode(mode) {
    currentMode = mode;
    localStorage.setItem('mode', mode);
  
    simpleBtn.classList.toggle('active', mode === 'simple');
    detailedBtn.classList.toggle('active', mode === 'detailed');
  
    // Анімація
    myChart.options.animation = {
      duration: 800,
      easing: 'easeInOutQuart'
    };
  
    myChart.data = (mode === 'simple') ? simpleData : detailedData;
    myChart.options.plugins.title.text = (mode === 'simple')
      ? 'Місячні показники продажів (Спрощено)'
      : 'Місячні показники продажів та витрат (Детально)';
    myChart.update();
  }
  
  // Перемикач теми (Світла/Темна)
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  let isDarkMode = localStorage.getItem('theme') === 'dark';
  
  if (isDarkMode) {
    document.body.classList.add('dark-mode');
    themeToggleBtn.innerText = '🌞 Світла Тема';
    applyThemeToChart();
  }
  
  themeToggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
  
    themeToggleBtn.innerText = isDarkMode ? '🌞 Світла Тема' : '🌙 Темна Тема';
  
    applyThemeToChart();
  });
  