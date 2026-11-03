import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useMood } from '../context/MoodContext';
import { MoodCard } from '../components/MoodCard';
import { PlusCircle, Search, Filter, BookOpen, Sparkles } from 'lucide-react';

export const EntriesListView = () => {
  const { entries } = useMood();
  const [busqueda, setBusqueda] = useState('');
  const [filtroEmocion, setFiltroEmocion] = useState('todas');
  const [filtroCategoria, setFiltroCategoria] = useState('todas');

  const entradasFiltradas = entries.filter(e => {
    const texto = (e.motivo_gratitud + ' ' + e.usuario + ' ' + (e.categoria || '')).toLowerCase();
    const coincideBusqueda = texto.includes(busqueda.toLowerCase());

    const coincideEmocion =
      filtroEmocion === 'todas' || e.emocion.toLowerCase() === filtroEmocion.toLowerCase();

    const coincideCategoria =
      filtroCategoria === 'todas' || (e.categoria && e.categoria.toLowerCase() === filtroCategoria.toLowerCase());

    return coincideBusqueda && coincideEmocion && coincideCategoria;
  });

  return (
    <div>
      {/* Barra de Acciones y Filtros */}
      <div
        className="card"
        style={{
          padding: '1.25rem 1.5rem',
          marginBottom: '2rem',
          display: 'flex',
          flexWrap: 'wrap',
          gap: '1rem',
          alignItems: 'center',
          justifyContent: 'space-between'
        }}
      >
        {/* Buscador */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', flex: '1 1 260px' }}>
          <Search size={18} color="var(--text-subtle)" />
          <input
            type="text"
            className="form-input"
            placeholder="Buscar por palabra clave o gratitud..."
            value={busqueda}
            onChange={(e) => setBusqueda(e.target.value)}
            style={{ padding: '0.55rem 0.85rem' }}
          />
        </div>

        {/* Filtro Emoción */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
          <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-muted)' }}>
            Emoción:
          </label>
          <select
            className="form-select"
            value={filtroEmocion}
            onChange={(e) => setFiltroEmocion(e.target.value)}
            style={{ padding: '0.55rem 0.85rem', width: 'auto' }}
          >
            <option value="todas">Todas las emociones</option>
            <option value="Radiante">Radiante (5)</option>
            <option value="Calmado">Calmado (4)</option>
            <option value="Estable">Estable (3)</option>
            <option value="Pensativo">Pensativo (2)</option>
            <option value="Apapacho">Apapacho (1)</option>
          </select>
        </div>

        {/* Filtro Categoría */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
          <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-muted)' }}>
            Categoría:
          </label>
          <select
            className="form-select"
            value={filtroCategoria}
            onChange={(e) => setFiltroCategoria(e.target.value)}
            style={{ padding: '0.55rem 0.85rem', width: 'auto' }}
          >
            <option value="todas">Todas las categorías</option>
            <option value="Bienestar">Bienestar</option>
            <option value="Crecimiento Personal">Crecimiento Personal</option>
            <option value="Estudio">Estudio</option>
            <option value="Trabajo">Trabajo</option>
            <option value="Familia">Familia</option>
            <option value="Amistad">Amistad</option>
            <option value="Salud">Salud</option>
          </select>
        </div>

        {/* Botón Nueva Entrada */}
        <Link to="/nueva-entrada" className="btn-primary" style={{ padding: '0.55rem 1.25rem' }}>
          <PlusCircle size={16} />
          <span>Escribir Nota</span>
        </Link>
      </div>

      {/* Resumen de conteo */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem' }}>
        <p style={{ fontSize: '0.88rem', color: 'var(--text-muted)' }}>
          Mostrando <strong>{entradasFiltradas.length}</strong> de {entries.length} notas en tu diario
        </p>

        {busqueda && (
          <button
            onClick={() => { setBusqueda(''); setFiltroEmocion('todas'); setFiltroCategoria('todas'); }}
            style={{ background: 'none', border: 'none', color: 'var(--peach-primary)', fontSize: '0.82rem', cursor: 'pointer', fontWeight: 600 }}
          >
            Limpiar filtros
          </button>
        )}
      </div>

      {/* Grilla de Entradas */}
      {entradasFiltradas.length > 0 ? (
        <div className="grid-responsive-cards">
          {entradasFiltradas.map((entry) => (
            <MoodCard key={entry.id} entry={entry} />
          ))}
        </div>
      ) : (
        <div
          className="card"
          style={{
            textAlign: 'center',
            padding: '3rem 2rem',
            maxWidth: '520px',
            margin: '2rem auto'
          }}
        >
          <BookOpen size={42} color="var(--peach-primary)" style={{ margin: '0 auto 1rem auto' }} />
          <h3 style={{ fontSize: '1.25rem', marginBottom: '0.5rem', color: 'var(--text-main)' }}>
            No se encontraron entradas con estos filtros
          </h3>
          <p style={{ fontSize: '0.88rem', color: 'var(--text-muted)', marginBottom: '1.5rem' }}>
            Prueba ajustando los términos de búsqueda o escribe una nueva nota de gratitud para hoy.
          </p>
          <Link to="/nueva-entrada" className="btn-primary">
            <PlusCircle size={16} />
            <span>Crear Nueva Entrada</span>
          </Link>
        </div>
      )}
    </div>
  );
};
