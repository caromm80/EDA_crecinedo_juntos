import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js';
import { Line, Bar } from 'react-chartjs-2';
import { useTheme } from '../context/ThemeContext';
import { TrendingUp, PieChart as PieIcon } from 'lucide-react';

// Registrar los controladores y componentes necesarios de Chart.js
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  Filler
);

export const MoodChart = ({ entries = [] }) => {
  const { isDark } = useTheme();

  // Color de texto y rejilla adaptable según el tema activo
  const textColor = isDark ? '#F1F5F9' : '#334155';
  const gridColor = isDark ? 'rgba(255, 255, 255, 0.08)' : 'rgba(0, 0, 0, 0.06)';

  // Ordenar cronológicamente para la línea de tiempo (últimos 14 registros)
  const entradasOrdenadas = [...entries]
    .sort((a, b) => new Date(a.fecha) - new Date(b.fecha))
    .slice(-14);

  const labelsFechas = entradasOrdenadas.map(e => {
    const f = new Date(e.fecha + 'T00:00:00');
    return f.toLocaleDateString('es-CO', { day: 'numeric', month: 'short' });
  });

  const datosAnimo = entradasOrdenadas.map(e => e.nivel_animo);
  const datosSueno = entradasOrdenadas.map(e => e.horas_sueno || 7.0);

  // Configuración del gráfico de evolución temporal (Línea)
  const lineChartData = {
    labels: labelsFechas,
    datasets: [
      {
        label: 'Estado de Ánimo (1 a 5)',
        data: datosAnimo,
        borderColor: '#F97316',
        backgroundColor: 'rgba(249, 115, 22, 0.18)',
        fill: true,
        tension: 0.4,
        pointBackgroundColor: '#F97316',
        pointBorderColor: '#FFFFFF',
        pointBorderWidth: 2,
        pointRadius: 5,
        pointHoverRadius: 8
      },
      {
        label: 'Horas de Sueño',
        data: datosSueno,
        borderColor: '#8B5CF6',
        backgroundColor: 'transparent',
        borderDash: [5, 5],
        tension: 0.3,
        pointBackgroundColor: '#8B5CF6',
        pointRadius: 3
      }
    ]
  };

  const lineOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        labels: {
          color: textColor,
          font: { family: "'Plus Jakarta Sans', sans-serif", weight: '600' }
        }
      },
      tooltip: {
        backgroundColor: isDark ? '#1E1A2D' : '#FFFFFF',
        titleColor: isDark ? '#FFFFFF' : '#1E1B4B',
        bodyColor: isDark ? '#CBD5E1' : '#475569',
        borderColor: '#F97316',
        borderWidth: 1.5,
        padding: 10,
        boxPadding: 4
      }
    },
    scales: {
      y: {
        min: 1,
        max: 10,
        ticks: { color: textColor, stepSize: 1 },
        grid: { color: gridColor }
      },
      x: {
        ticks: { color: textColor },
        grid: { color: gridColor }
      }
    }
  };

  // Conteo de distribución por tipo de emoción
  const conteoEmociones = {
    Radiante: 0,
    Calmado: 0,
    Estable: 0,
    Pensativo: 0,
    Apapacho: 0
  };

  entries.forEach(e => {
    const em = e.emocion;
    if (conteoEmociones[em] !== undefined) {
      conteoEmociones[em] += 1;
    } else {
      conteoEmociones['Estable'] += 1;
    }
  });

  const barChartData = {
    labels: ['Radiante (5)', 'Calmado (4)', 'Estable (3)', 'Pensativo (2)', 'Apapacho (1)'],
    datasets: [
      {
        label: 'Frecuencia de Días',
        data: [
          conteoEmociones.Radiante,
          conteoEmociones.Calmado,
          conteoEmociones.Estable,
          conteoEmociones.Pensativo,
          conteoEmociones.Apapacho
        ],
        backgroundColor: [
          '#F59E0B',
          '#10B981',
          '#8B5CF6',
          '#FB923C',
          '#F43F5E'
        ],
        borderRadius: 8
      }
    ]
  };

  const barOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false }
    },
    scales: {
      y: {
        ticks: { color: textColor, precision: 0 },
        grid: { color: gridColor }
      },
      x: {
        ticks: { color: textColor, font: { size: 11, weight: '600' } },
        grid: { display: false }
      }
    }
  };

  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: '1.5rem', marginBottom: '2.5rem' }}>
      {/* Gráfico 1: Evolución Temporal */}
      <div className="card" style={{ padding: '1.5rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.25rem' }}>
          <TrendingUp size={20} color="var(--peach-primary)" />
          <h3 style={{ fontSize: '1.1rem', color: 'var(--text-main)' }}>
            Evolución del Estado de Ánimo y Sueño
          </h3>
        </div>
        <div style={{ height: '260px' }}>
          <Line data={lineChartData} options={lineOptions} />
        </div>
        <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textAlign: 'center', marginTop: '0.75rem' }}>
          Muestra los últimos 14 registros de gratitud de la cuenta.
        </p>
      </div>

      {/* Gráfico 2: Distribución de Emociones */}
      <div className="card" style={{ padding: '1.5rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.25rem' }}>
          <PieIcon size={20} color="#8B5CF6" />
          <h3 style={{ fontSize: '1.1rem', color: 'var(--text-main)' }}>
            Distribución de Emociones en el Tiempo
          </h3>
        </div>
        <div style={{ height: '260px' }}>
          <Bar data={barChartData} options={barOptions} />
        </div>
        <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textAlign: 'center', marginTop: '0.75rem' }}>
          Conteo acumulado de tus estados emocionales registrados con Lumi.
        </p>
      </div>
    </div>
  );
};
