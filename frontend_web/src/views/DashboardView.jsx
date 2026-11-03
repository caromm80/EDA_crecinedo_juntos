import React from 'react';
import { Link } from 'react-router-dom';
import { useMood } from '../context/MoodContext';
import { useAuth } from '../context/AuthContext';
import { LumiMonster } from '../components/LumiMonster';
import { StatWidget } from '../components/StatWidget';
import { MoodChart } from '../components/MoodChart';
import { MoodCard } from '../components/MoodCard';
import { Sparkles, Heart, PlusCircle, ArrowRight, Sun, Award, Flame } from 'lucide-react';

export const DashboardView = () => {
  const { entries, getStats } = useMood();
  const { user } = useAuth();
  const stats = getStats();

  const ultimasEntradas = entries.slice(0, 3);
  const promedioNum = parseFloat(stats.promedioAnimo) || 4.2;
  const animoRedondeado = Math.round(promedioNum);

  return (
    <div>
      {/* Banner de Bienvenida con Lumi el Monstruito de la Gratitud */}
      <div
        className="card"
        style={{
          background: 'linear-gradient(135deg, var(--bg-surface), var(--bg-surface-soft))',
          border: '1.5px solid var(--border-subtle)',
          padding: '2rem 2.5rem',
          marginBottom: '2rem',
          display: 'flex',
          flexWrap: 'wrap',
          alignItems: 'center',
          justifyContent: 'space-between',
          gap: '2rem'
        }}
      >
        <div style={{ flex: '1 1 380px' }}>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.4rem', backgroundColor: 'var(--peach-light)', color: 'var(--peach-primary)', padding: '4px 12px', borderRadius: '12px', fontSize: '0.8rem', fontWeight: 700, marginBottom: '0.85rem' }}>
            <Sparkles size={14} />
            <span>¡Hola de nuevo, {user?.nombre?.split(' ')[0] || 'Amigo(a)'}!</span>
          </div>
          <h2 style={{ fontSize: '2rem', marginBottom: '0.5rem', color: 'var(--text-main)', lineHeight: 1.2 }}>
            Tu espacio seguro para cultivar bienestar y gratitud
          </h2>
          <p style={{ fontSize: '0.95rem', color: 'var(--text-muted)', marginBottom: '1.5rem', maxWidth: '520px' }}>
            Registrar cómo te sientes y agradecer por las cosas cotidianas entrena tu cerebro para la resiliencia y la alegría. Lumi está listo para acompañarte hoy.
          </p>

          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.85rem' }}>
            <Link to="/nueva-entrada" className="btn-primary">
              <PlusCircle size={18} />
              <span>Registrar Ánimo de Hoy</span>
            </Link>
            <Link to="/diario" className="btn-secondary">
              <span>Ver Mi Diario ({stats.total})</span>
              <ArrowRight size={16} />
            </Link>
          </div>
        </div>

        {/* Mascota Lumi interactiva animada */}
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', flex: '0 0 auto' }}>
          <LumiMonster mood={animoRedondeado} size={170} showBubble={true} interactive={true} />
        </div>
      </div>

      {/* Grid de Métricas y Estadísticas Clave */}
      <div className="grid-stats">
        <StatWidget
          title="Ánimo Promedio"
          value={`${stats.promedioAnimo} / 5.0`}
          subtitle="Basado en tus registros acumulados"
          icon={Sun}
          color="#F59E0B"
          bgColor="rgba(245, 158, 11, 0.15)"
        />

        <StatWidget
          title="Total Registros"
          value={stats.total}
          subtitle="Días de reflexión guardados"
          icon={Heart}
          color="#F43F5E"
          bgColor="rgba(244, 63, 94, 0.15)"
        />

        <StatWidget
          title="Racha Activa"
          value={`${stats.rachaDias} días`}
          subtitle="Constancia cultivando gratitud"
          icon={Flame}
          color="#FB923C"
          bgColor="rgba(251, 146, 60, 0.15)"
        />

        <StatWidget
          title="Días Positivos"
          value={`${stats.tasaPositiva}%`}
          subtitle="Índice de bienestar (Ánimo ≥ 3)"
          icon={Award}
          color="#10B981"
          bgColor="rgba(16, 185, 129, 0.15)"
        />
      </div>

      {/* Gráfico de Evolución Temporal (Chart.js) */}
      <MoodChart entries={entries} />

      {/* Vista previa de las últimas entradas */}
      <div style={{ marginTop: '2.5rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem' }}>
          <div>
            <h3 style={{ fontSize: '1.35rem', color: 'var(--text-main)' }}>
              Últimas Entradas en tu Diario
            </h3>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
              Tus reflexiones más recientes guardadas en el estado global
            </p>
          </div>

          <Link to="/diario" style={{ fontSize: '0.88rem', fontWeight: 600, color: 'var(--peach-primary)', display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
            <span>Ver todo el historial</span>
            <ArrowRight size={16} />
          </Link>
        </div>

        <div className="grid-responsive-cards">
          {ultimasEntradas.map(entry => (
            <MoodCard key={entry.id} entry={entry} />
          ))}
        </div>
      </div>
    </div>
  );
};
