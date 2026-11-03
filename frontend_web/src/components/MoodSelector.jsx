import React from 'react';
import { LumiMonster } from './LumiMonster';

/**
 * COMPONENTE: MoodSelector
 * Selector interactivo de estado de ánimo en escala del 1 al 5.
 * Reemplaza emojis clásicos de teclado por tarjetas ilustradas y amigables.
 */
export const MoodSelector = ({ selectedMood = 4, onSelectMood }) => {
  const opciones = [
    { nivel: 5, nombre: 'Radiante', desc: '¡Lleno de energía y gratitud!', color: '#F59E0B' },
    { nivel: 4, nombre: 'Calmado', desc: 'Paz mental y bienestar', color: '#10B981' },
    { nivel: 3, nombre: 'Estable', desc: 'Un día normal y equilibrado', color: '#8B5CF6' },
    { nivel: 2, nombre: 'Pensativo', desc: 'Reflexivo o con cansancio', color: '#FB923C' },
    { nivel: 1, nombre: 'Apapacho', desc: 'Día sensible, necesito cariño', color: '#F43F5E' }
  ];

  return (
    <div style={{ margin: '1rem 0' }}>
      <label className="form-label" style={{ marginBottom: '0.75rem' }}>
        <span>✨ ¿Cómo se siente tu corazón hoy? (Selecciona una opción):</span>
      </label>
      
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))',
          gap: '0.85rem'
        }}
      >
        {opciones.map(opt => {
          const isSelected = selectedMood === opt.nivel;
          return (
            <button
              key={opt.nivel}
              type="button"
              onClick={() => onSelectMood(opt.nivel, opt.nombre)}
              style={{
                backgroundColor: isSelected ? 'var(--bg-surface)' : 'var(--bg-surface-soft)',
                border: isSelected ? `2.5px solid ${opt.color}` : '1.5px solid var(--border-subtle)',
                borderRadius: 'var(--radius-md)',
                padding: '0.85rem 0.5rem',
                cursor: 'pointer',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: '0.35rem',
                transform: isSelected ? 'translateY(-4px)' : 'none',
                boxShadow: isSelected ? `0 8px 20px ${opt.color}35` : 'var(--shadow-sm)',
                transition: 'var(--transition-smooth)'
              }}
            >
              <div style={{ pointerEvents: 'none' }}>
                <LumiMonster mood={opt.nivel} size={62} showBubble={false} interactive={false} />
              </div>
              <span style={{ fontWeight: 700, fontSize: '0.9rem', color: isSelected ? opt.color : 'var(--text-main)' }}>
                {opt.nombre}
              </span>
              <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)', textAlign: 'center', lineHeight: 1.2 }}>
                {opt.desc}
              </span>
              <span
                style={{
                  fontSize: '0.7rem',
                  fontWeight: 800,
                  backgroundColor: isSelected ? opt.color : 'var(--bg-surface-muted)',
                  color: isSelected ? '#FFFFFF' : 'var(--text-muted)',
                  borderRadius: '10px',
                  padding: '2px 8px',
                  marginTop: '4px'
                }}
              >
                {opt.nivel} / 5
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
