import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import { useTheme } from '../context/ThemeContext';
import { LumiMonster } from '../components/LumiMonster';
import { Sun, Moon, Sparkles, ArrowLeft } from 'lucide-react';

export const AuthLayout = () => {
  const { isDark, toggleTheme } = useTheme();

  return (
    <div
      style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '2rem 1.5rem',
        backgroundColor: 'var(--bg-app)',
        position: 'relative'
      }}
    >
      {/* Botón superior de volver y cambio de tema */}
      <div
        style={{
          position: 'absolute',
          top: '1.5rem',
          left: '1.5rem',
          right: '1.5rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}
      >
        <Link
          to="/dashboard"
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.4rem',
            fontSize: '0.88rem',
            fontWeight: 600,
            color: 'var(--peach-primary)'
          }}
        >
          <ArrowLeft size={16} />
          <span>Volver al Dashboard</span>
        </Link>

        <button
          onClick={toggleTheme}
          style={{
            background: 'var(--bg-surface)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 'var(--radius-full)',
            width: '38px',
            height: '38px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            cursor: 'pointer',
            boxShadow: 'var(--shadow-sm)'
          }}
          title="Cambiar tema"
        >
          {isDark ? <Sun size={18} color="#FBBF24" /> : <Moon size={18} color="#8B5CF6" />}
        </button>
      </div>

      {/* Contenedor central cálido */}
      <div
        style={{
          maxWidth: '440px',
          width: '100%',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center'
        }}
      >
        {/* Lumi animado saludando */}
        <div style={{ marginBottom: '1.25rem' }}>
          <LumiMonster mood={5} size={150} showBubble={true} interactive={true} />
        </div>

        {/* Nombre de layout/componente */}
        <div className="page-signature-badge">
          <Sparkles size={13} />
          <span>Layout de Autenticación & Acceso</span>
        </div>

        {/* Tarjeta con el formulario */}
        <div
          className="card"
          style={{
            width: '100%',
            padding: '2rem 2.25rem',
            boxShadow: 'var(--shadow-lg)'
          }}
        >
          <Outlet />
        </div>

        <p style={{ marginTop: '1.5rem', fontSize: '0.8rem', color: 'var(--text-subtle)', textAlign: 'center' }}>
          Lumi Mood Tracker • CESDE Creciendo Juntos © 2026
        </p>
      </div>
    </div>
  );
};
