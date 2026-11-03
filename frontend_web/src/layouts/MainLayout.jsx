import React from 'react';
import { Outlet, useLocation } from 'react-router-dom';
import { Navbar } from '../components/Navbar';
import { Footer } from '../components/Footer';
import { Layers } from 'lucide-react';

export const MainLayout = () => {
  const location = useLocation();

  // Mapeo amigable del nombre de la página para cumplir con el requerimiento:
  // "Nombre de la pagina en cada componente"
  const getPageInfo = (path) => {
    if (path.startsWith('/dashboard')) return { title: 'Panel de Control (Dashboard)', desc: 'Evolución de tu ánimo y resumen de bienestar' };
    if (path.startsWith('/diario')) return { title: 'Historial del Diario de Gratitud', desc: 'Explora y gestiona tus notas diarias registradas' };
    if (path.startsWith('/nueva-entrada')) return { title: 'Registrar Gratitud y Ánimo', desc: 'Dedica 2 minutos a conectar con tus emociones de hoy' };
    if (path.startsWith('/editar')) return { title: 'Modificar Entrada del Diario', desc: 'Actualiza tus reflexiones o corrige detalles' };
    if (path.startsWith('/usuarios')) return { title: 'Directorio de la Comunidad', desc: 'Compañeros activos en el reto Creciendo Juntos' };
    if (path.startsWith('/acerca-de')) return { title: 'Equipo & Arquitectura de Componentes', desc: 'Distribución de roles y árbol de componentes del proyecto' };
    return { title: 'Lumi Mood Tracker', desc: 'Diario de Gratitud' };
  };

  const pageInfo = getPageInfo(location.pathname);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <Navbar />

      <main style={{ flex: 1, padding: '2rem 0' }}>
        <div className="container">
          {/* Header de la Página con Identificador Explícito */}
          <div style={{ marginBottom: '1.75rem' }}>
            <div className="page-signature-badge">
              <Layers size={14} />
              <span>Vista Activa: {pageInfo.title}</span>
            </div>
            <h1 style={{ fontSize: '1.85rem', marginBottom: '0.35rem', color: 'var(--text-main)' }}>
              {pageInfo.title}
            </h1>
            <p style={{ fontSize: '0.95rem', color: 'var(--text-muted)' }}>
              {pageInfo.desc}
            </p>
          </div>

          {/* Renderizado de la ruta activa */}
          <Outlet />
        </div>
      </main>

      <Footer />
    </div>
  );
};
