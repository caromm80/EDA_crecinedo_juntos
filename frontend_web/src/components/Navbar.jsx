import React from 'react';
import { NavLink, Link } from 'react-router-dom';
import { useTheme } from '../context/ThemeContext';
import { useAuth } from '../context/AuthContext';
import { Sun, Moon, Sparkles, Heart, PlusCircle, BookOpen, Users, LayoutDashboard, Info, LogOut } from 'lucide-react';

export const Navbar = () => {
  const { isDark, toggleTheme } = useTheme();
  const { user, logout } = useAuth();

  return (
    <header
      style={{
        position: 'sticky',
        top: 0,
        zIndex: 100,
        backgroundColor: 'var(--bg-surface)',
        borderBottom: '1px solid var(--border-subtle)',
        backdropFilter: 'blur(12px)',
        transition: 'var(--transition-smooth)'
      }}
    >
      <div
        className="container"
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          height: '70px',
          padding: '0 1.25rem'
        }}
      >
        {/* Brand / Logo */}
        <Link
          to="/dashboard"
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.65rem',
            textDecoration: 'none'
          }}
        >
          <div
            style={{
              width: '42px',
              height: '42px',
              borderRadius: 'var(--radius-full)',
              background: 'linear-gradient(135deg, #FF9EAA, #FCD34D)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxShadow: '0 4px 12px rgba(251, 146, 60, 0.35)'
            }}
          >
            <Sparkles size={22} color="#FFFFFF" />
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
              <span style={{ fontSize: '1.35rem', fontWeight: 800, color: 'var(--text-main)', letterSpacing: '-0.02em' }}>
                Lumi
              </span>
              <span
                style={{
                  fontSize: '0.65rem',
                  fontWeight: 700,
                  backgroundColor: 'var(--peach-light)',
                  color: 'var(--peach-primary)',
                  padding: '2px 7px',
                  borderRadius: '10px'
                }}
              >
                Creciendo Juntos
              </span>
            </div>
            <p style={{ fontSize: '0.72rem', color: 'var(--text-muted)', lineHeight: 1 }}>
              Diario de Gratitud & Mood
            </p>
          </div>
        </Link>

        {/* Links de Navegación (SPA sin recarga) */}
        <nav style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <NavLink
            to="/dashboard"
            style={({ isActive }) => ({
              display: 'flex',
              alignItems: 'center',
              gap: '0.4rem',
              padding: '0.5rem 0.85rem',
              borderRadius: 'var(--radius-md)',
              fontSize: '0.88rem',
              fontWeight: 600,
              color: isActive ? 'var(--peach-primary)' : 'var(--text-muted)',
              backgroundColor: isActive ? 'var(--bg-surface-soft)' : 'transparent',
              transition: 'var(--transition-smooth)'
            })}
          >
            <LayoutDashboard size={18} />
            <span>Dashboard</span>
          </NavLink>

          <NavLink
            to="/diario"
            style={({ isActive }) => ({
              display: 'flex',
              alignItems: 'center',
              gap: '0.4rem',
              padding: '0.5rem 0.85rem',
              borderRadius: 'var(--radius-md)',
              fontSize: '0.88rem',
              fontWeight: 600,
              color: isActive ? 'var(--peach-primary)' : 'var(--text-muted)',
              backgroundColor: isActive ? 'var(--bg-surface-soft)' : 'transparent',
              transition: 'var(--transition-smooth)'
            })}
          >
            <BookOpen size={18} />
            <span>Diario</span>
          </NavLink>

          <NavLink
            to="/nueva-entrada"
            style={({ isActive }) => ({
              display: 'flex',
              alignItems: 'center',
              gap: '0.4rem',
              padding: '0.5rem 0.85rem',
              borderRadius: 'var(--radius-md)',
              fontSize: '0.88rem',
              fontWeight: 600,
              color: isActive ? 'var(--peach-primary)' : 'var(--text-muted)',
              backgroundColor: isActive ? 'var(--bg-surface-soft)' : 'transparent',
              transition: 'var(--transition-smooth)'
            })}
          >
            <PlusCircle size={18} />
            <span>Nueva Entrada</span>
          </NavLink>

          <NavLink
            to="/usuarios"
            style={({ isActive }) => ({
              display: 'flex',
              alignItems: 'center',
              gap: '0.4rem',
              padding: '0.5rem 0.85rem',
              borderRadius: 'var(--radius-md)',
              fontSize: '0.88rem',
              fontWeight: 600,
              color: isActive ? 'var(--peach-primary)' : 'var(--text-muted)',
              backgroundColor: isActive ? 'var(--bg-surface-soft)' : 'transparent',
              transition: 'var(--transition-smooth)'
            })}
          >
            <Users size={18} />
            <span>Comunidad (20+)</span>
          </NavLink>

          <NavLink
            to="/acerca-de"
            style={({ isActive }) => ({
              display: 'flex',
              alignItems: 'center',
              gap: '0.4rem',
              padding: '0.5rem 0.85rem',
              borderRadius: 'var(--radius-md)',
              fontSize: '0.88rem',
              fontWeight: 600,
              color: isActive ? 'var(--peach-primary)' : 'var(--text-muted)',
              backgroundColor: isActive ? 'var(--bg-surface-soft)' : 'transparent',
              transition: 'var(--transition-smooth)'
            })}
          >
            <Info size={18} />
            <span>Equipo</span>
          </NavLink>
        </nav>

        {/* Acciones del Navbar: Toggle Tema y Perfil */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          {/* Botón de Tema Claro/Oscuro */}
          <button
            onClick={toggleTheme}
            style={{
              background: 'var(--bg-surface-soft)',
              border: '1px solid var(--border-subtle)',
              borderRadius: 'var(--radius-full)',
              width: '38px',
              height: '38px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              cursor: 'pointer',
              color: 'var(--text-main)',
              transition: 'var(--transition-smooth)'
            }}
            title={isDark ? "Cambiar a modo cálido (Claro)" : "Cambiar a modo noche (Oscuro)"}
          >
            {isDark ? <Sun size={19} color="#FBBF24" /> : <Moon size={19} color="#8B5CF6" />}
          </button>

          {/* Pastilla de Usuario */}
          {user?.isLoggedIn ? (
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '0.6rem',
                backgroundColor: 'var(--bg-surface-soft)',
                border: '1px solid var(--border-subtle)',
                borderRadius: 'var(--radius-full)',
                padding: '0.25rem 0.75rem 0.25rem 0.4rem'
              }}
            >
              <div
                style={{
                  width: '28px',
                  height: '28px',
                  borderRadius: 'var(--radius-full)',
                  backgroundColor: 'var(--coral-light)',
                  color: 'var(--coral-primary)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontWeight: 700,
                  fontSize: '0.82rem'
                }}
              >
                {user.nombre ? user.nombre[0].toUpperCase() : 'U'}
              </div>
              <span style={{ fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-main)' }}>
                {user.nombre.split(' ')[0]}
              </span>
              <button
                onClick={logout}
                style={{
                  background: 'none',
                  border: 'none',
                  color: 'var(--text-subtle)',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center'
                }}
                title="Cerrar Sesión"
              >
                <LogOut size={15} />
              </button>
            </div>
          ) : (
            <Link to="/login" className="btn-primary" style={{ padding: '0.45rem 1rem', fontSize: '0.82rem' }}>
              Iniciar Sesión
            </Link>
          )}
        </div>
      </div>
    </header>
  );
};
