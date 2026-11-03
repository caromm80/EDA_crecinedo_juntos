import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useMood } from '../context/MoodContext';
import { LumiMonster } from './LumiMonster';
import { Calendar, Moon, Sparkles, Edit3, Trash2, Heart, Tag } from 'lucide-react';

export const MoodCard = ({ entry }) => {
  const { deleteEntry } = useMood();
  const [isDeleting, setIsDeleting] = useState(false);

  const handleDelete = () => {
    if (window.confirm(`¿Estás seguro de que deseas eliminar este registro del ${entry.fecha}?`)) {
      deleteEntry(entry.id);
    }
  };

  const getBadgeClass = (nivel) => {
    return `badge-emotion badge-${nivel}`;
  };

  return (
    <div
      className="card"
      style={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        position: 'relative',
        transition: 'var(--transition-smooth)'
      }}
    >
      <div>
        {/* Encabezado: Avatar de Lumi + Info Fecha */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <div style={{ pointerEvents: 'none' }}>
              <LumiMonster mood={entry.nivel_animo} size={50} showBubble={false} interactive={false} />
            </div>
            <div>
              <span className={getBadgeClass(entry.nivel_animo)}>
                <Sparkles size={12} />
                {entry.emocion} ({entry.nivel_animo}/5)
              </span>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem', fontSize: '0.75rem', color: 'var(--text-subtle)', marginTop: '0.25rem' }}>
                <Calendar size={13} />
                <span>{entry.fecha}</span>
                <span>•</span>
                <span>{entry.usuario}</span>
              </div>
            </div>
          </div>

          {/* Acciones de Edición y Borrado (CRUD) */}
          <div style={{ display: 'flex', gap: '0.35rem' }}>
            <Link
              to={`/editar/${entry.id}`}
              style={{
                background: 'var(--bg-surface-soft)',
                border: '1px solid var(--border-subtle)',
                borderRadius: 'var(--radius-sm)',
                padding: '0.4rem',
                color: 'var(--text-muted)',
                display: 'flex',
                alignItems: 'center',
                transition: 'var(--transition-smooth)'
              }}
              title="Editar entrada"
            >
              <Edit3 size={15} />
            </Link>

            <button
              onClick={handleDelete}
              style={{
                background: 'var(--bg-surface-soft)',
                border: '1px solid var(--border-subtle)',
                borderRadius: 'var(--radius-sm)',
                padding: '0.4rem',
                color: 'var(--coral-primary)',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                transition: 'var(--transition-smooth)'
              }}
              title="Eliminar entrada"
            >
              <Trash2 size={15} />
            </button>
          </div>
        </div>

        {/* Motivo de Gratitud */}
        <div
          style={{
            backgroundColor: 'var(--bg-surface-soft)',
            padding: '1rem',
            borderRadius: 'var(--radius-md)',
            borderLeft: '4px solid var(--peach-primary)',
            marginBottom: '1rem'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem', color: 'var(--peach-primary)', fontSize: '0.75rem', fontWeight: 700, marginBottom: '0.25rem' }}>
            <Heart size={13} fill="var(--peach-primary)" />
            <span>Agradecimiento del día:</span>
          </div>
          <p style={{ fontSize: '0.92rem', color: 'var(--text-main)', lineHeight: 1.5, fontStyle: 'italic' }}>
            "{entry.motivo_gratitud}"
          </p>
        </div>
      </div>

      {/* Pie de tarjeta con detalles (horas de sueño y categoría) */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          borderTop: '1px solid var(--border-subtle)',
          paddingTop: '0.75rem',
          fontSize: '0.78rem',
          color: 'var(--text-muted)'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
          <Tag size={13} color="var(--peach-primary)" />
          <span style={{ fontWeight: 600 }}>{entry.categoria || 'Bienestar'}</span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
          <Moon size={13} color="#8B5CF6" />
          <span>{entry.horas_sueno || 7.0} hrs de sueño</span>
        </div>
      </div>
    </div>
  );
};
