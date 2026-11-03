import React from 'react';
import { Heart, Sparkles, Smile, ShieldCheck } from 'lucide-react';

export const Footer = () => {
  return (
    <footer
      style={{
        backgroundColor: 'var(--bg-surface)',
        borderTop: '1px solid var(--border-subtle)',
        padding: '2.5rem 0 2rem 0',
        marginTop: '4rem',
        transition: 'var(--transition-smooth)'
      }}
    >
      <div className="container">
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))',
            gap: '2rem',
            marginBottom: '2rem'
          }}
        >
          {/* Columna 1: Presentación de Lumi */}
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.75rem' }}>
              <span style={{ fontSize: '1.25rem', fontWeight: 800 }}>🌸 Lumi</span>
              <span
                style={{
                  fontSize: '0.75rem',
                  backgroundColor: 'var(--mint-light)',
                  color: 'var(--mint-primary)',
                  padding: '2px 8px',
                  borderRadius: '12px',
                  fontWeight: 700
                }}
              >
                Creciendo Juntos
              </span>
            </div>
            <p style={{ fontSize: '0.86rem', color: 'var(--text-muted)', lineHeight: 1.6 }}>
              Plataforma para el registro diario del estado de ánimo y la práctica consciente de la gratitud.
              Diseñado con calidez para acompañar tu bienestar emocional día a día.
            </p>
          </div>

          {/* Columna 2: Frase del Día */}
          <div
            style={{
              backgroundColor: 'var(--bg-surface-soft)',
              padding: '1.25rem',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--border-subtle)'
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', color: 'var(--peach-primary)', marginBottom: '0.4rem' }}>
              <Sparkles size={16} />
              <span style={{ fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase' }}>
                Reflexión de Hoy
              </span>
            </div>
            <p style={{ fontSize: '0.88rem', fontStyle: 'italic', color: 'var(--text-main)', lineHeight: 1.5 }}>
              "La gratitud no cambia las cosas que te sucedieron, pero cambia profundamente la forma en que las vives."
            </p>
          </div>

          {/* Columna 3: Información Académica CESDE */}
          <div>
            <h4 style={{ fontSize: '0.92rem', marginBottom: '0.6rem', color: 'var(--text-main)' }}>
              Proyecto Integrador CESDE 2026
            </h4>
            <ul style={{ listStyle: 'none', fontSize: '0.84rem', color: 'var(--text-muted)', lineHeight: 1.9 }}>
              <li>• Momento 1: Consola, Funciones y Colecciones</li>
              <li>• Momento 2: Pandas, EDA y Entornos Virtuales</li>
              <li>• Momento Web: React, Vite, Context API & Chart.js</li>
              <li>• Versionamiento: Git Flow & Ramas</li>
            </ul>
          </div>
        </div>

        {/* Barra inferior de copyright */}
        <div
          style={{
            borderTop: '1px solid var(--border-subtle)',
            paddingTop: '1.25rem',
            display: 'flex',
            flexWrap: 'wrap',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: '1rem',
            fontSize: '0.8rem',
            color: 'var(--text-subtle)'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
            <span>Hecho con</span>
            <Heart size={14} color="#F43F5E" fill="#F43F5E" />
            <span>por el equipo de Creciendo Juntos © 2026</span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
            <ShieldCheck size={14} color="#10B981" />
            <span>Tus datos de gratitud se guardan localmente con total privacidad</span>
          </div>
        </div>
      </div>
    </footer>
  );
};
