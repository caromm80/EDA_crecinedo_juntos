import React from 'react';
import { UserCheck, Code, Layers, Sparkles, CheckCircle2 } from 'lucide-react';

/**
 * COMPONENTE: TeamCredits
 * Especificación de la entrega Web 2:
 * 1. Un componente por persona asignado al equipo de desarrollo.
 * 2. Listado completo de los componentes desarrollados y proyectados en la arquitectura.
 */
export const TeamCredits = () => {
  const equipo = [
    {
      nombre: 'Carolina Morales',
      rol: 'Líder de Frontend & UX',
      componenteAsignado: '<LumiMonster /> & <MoodSelector />',
      descripcion: 'Diseño SVG vectorial exclusivo de la mascota Lumi, expresiones interactivas y selector visual de emociones sin emojis estándar.',
      avatarLetra: 'C',
      color: '#F43F5E'
    },
    {
      nombre: 'Mateo Restrepo',
      rol: 'Arquitectura SPA & Routing',
      componenteAsignado: '<MainLayout />, <AuthLayout /> & routes.jsx',
      descripcion: 'Estructuración de layouts modulares, navegación fluida sin recargas con React Router DOM v7 y footer reflexivo.',
      avatarLetra: 'M',
      color: '#FB923C'
    },
    {
      nombre: 'Valentina Gómez',
      rol: 'Estado Global & Persistencia',
      componenteAsignado: '<MoodContext /> & <ThemeContext />',
      descripcion: 'Implementación de Context API para CRUD global, gestión de 22 registros mock iniciales y conmutador de tema claro/oscuro.',
      avatarLetra: 'V',
      color: '#8B5CF6'
    },
    {
      nombre: 'Andrés Felipe',
      rol: 'Formularios & Validación',
      componenteAsignado: '<GratitudeForm /> & <MoodCard />',
      descripcion: 'Formularios controlados con React state, validación en tiempo real de caracteres, animaciones de confeti y edición de notas.',
      avatarLetra: 'A',
      color: '#10B981'
    },
    {
      nombre: 'Sofía Ramírez',
      rol: 'Analítica & Datos de Comunidad',
      componenteAsignado: '<ListaUsuarios /> & <MoodChart />',
      descripcion: 'Maquetación de la comunidad con 24 usuarios quemados en código, métricas descriptivas y gráficos de series temporales con Chart.js.',
      avatarLetra: 'S',
      color: '#F59E0B'
    }
  ];

  const catalogoComponentes = [
    { nombre: 'LumiMonster.jsx', estado: 'Listo ✅', categoria: 'UI / Ilustración', proposito: 'Mascota interactiva SVG con micro-animaciones y frases' },
    { nombre: 'MoodSelector.jsx', estado: 'Listo ✅', categoria: 'Formularios', proposito: 'Selector de escala 1 al 5 con tarjetas ilustradas' },
    { nombre: 'MoodChart.jsx', estado: 'Listo ✅', categoria: 'Dashboard / Gráficos', proposito: 'Visualización temporal con Chart.js y react-chartjs-2' },
    { nombre: 'StatWidget.jsx', estado: 'Listo ✅', categoria: 'Dashboard / Métricas', proposito: 'Tarjetas de estadísticas clave de gratitud y bienestar' },
    { nombre: 'MoodCard.jsx', estado: 'Listo ✅', categoria: 'Diario / Listas', proposito: 'Tarjeta individual de nota de gratitud con acciones CRUD' },
    { nombre: 'GratitudeForm.jsx', estado: 'Listo ✅', categoria: 'Formularios', proposito: 'Formulario controlado con validación para crear/editar' },
    { nombre: 'ListaUsuarios.jsx', estado: 'Listo ✅', categoria: 'Comunidad', proposito: 'Renderiza más de 20 usuarios quemados en código' },
    { nombre: 'Navbar.jsx', estado: 'Listo ✅', categoria: 'Navegación', proposito: 'Barra superior con toggle de tema, links SPA y perfil' },
    { nombre: 'Footer.jsx', estado: 'Listo ✅', categoria: 'Layout', proposito: 'Pie de página cálido con citas inspiracionales y créditos' },
    { nombre: 'MainLayout.jsx', estado: 'Listo ✅', categoria: 'Layout', proposito: 'Estructura principal con identificación de cada página' },
    { nombre: 'AuthLayout.jsx', estado: 'Listo ✅', categoria: 'Layout', proposito: 'Layout acogedor para pantallas de autenticación' },
    { nombre: 'ThemeContext.jsx', estado: 'Listo ✅', categoria: 'Context API', proposito: 'Proveedor de Tema Claro Cálido y Tema Noche Oscuro' },
    { nombre: 'MoodContext.jsx', estado: 'Listo ✅', categoria: 'Context API', proposito: 'Estado Global para CRUD completo de bienestar' },
    { nombre: 'AuthContext.jsx', estado: 'Listo ✅', categoria: 'Context API', proposito: 'Gestor global de sesión y perfil de usuario' },
    { nombre: 'routes.jsx', estado: 'Listo ✅', categoria: 'Enrutamiento', proposito: 'Definición de rutas SPA navegables con react-router-dom' }
  ];

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2.5rem' }}>
      {/* Sección 1: Un componente por persona */}
      <div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.25rem' }}>
          <UserCheck size={22} color="var(--peach-primary)" />
          <h2 style={{ fontSize: '1.4rem', color: 'var(--text-main)' }}>
            1. Asignación de Componentes por Integrante
          </h2>
        </div>

        <div className="grid-responsive-cards">
          {equipo.map((m, idx) => (
            <div
              key={idx}
              className="card"
              style={{
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                borderTop: `4px solid ${m.color}`
              }}
            >
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.75rem' }}>
                  <div
                    style={{
                      width: '42px',
                      height: '42px',
                      borderRadius: 'var(--radius-full)',
                      backgroundColor: m.color,
                      color: '#FFFFFF',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontWeight: 800,
                      fontSize: '1.1rem'
                    }}
                  >
                    {m.avatarLetra}
                  </div>
                  <div>
                    <h3 style={{ fontSize: '1.1rem', color: 'var(--text-main)' }}>{m.nombre}</h3>
                    <p style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>{m.rol}</p>
                  </div>
                </div>

                <div
                  style={{
                    backgroundColor: 'var(--bg-surface-soft)',
                    padding: '0.65rem 0.85rem',
                    borderRadius: 'var(--radius-md)',
                    marginBottom: '0.75rem'
                  }}
                >
                  <span style={{ fontSize: '0.72rem', fontWeight: 700, color: 'var(--peach-primary)', textTransform: 'uppercase' }}>
                    Componente Asignado:
                  </span>
                  <p style={{ fontSize: '0.95rem', fontWeight: 700, color: 'var(--text-main)' }}>
                    {m.componenteAsignado}
                  </p>
                </div>

                <p style={{ fontSize: '0.84rem', color: 'var(--text-muted)', lineHeight: 1.5 }}>
                  {m.descripcion}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Sección 2: Listado Total de Componentes Proyectados e Implementados */}
      <div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.25rem' }}>
          <Layers size={22} color="var(--peach-primary)" />
          <h2 style={{ fontSize: '1.4rem', color: 'var(--text-main)' }}>
            2. Listado Total de Componentes del Proyecto ({catalogoComponentes.length} Componentes)
          </h2>
        </div>

        <div className="card" style={{ padding: '0', overflow: 'hidden' }}>
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.88rem' }}>
              <thead>
                <tr style={{ backgroundColor: 'var(--bg-surface-soft)', borderBottom: '1px solid var(--border-subtle)' }}>
                  <th style={{ padding: '1rem', fontWeight: 700, color: 'var(--text-main)' }}>Componente</th>
                  <th style={{ padding: '1rem', fontWeight: 700, color: 'var(--text-main)' }}>Categoría</th>
                  <th style={{ padding: '1rem', fontWeight: 700, color: 'var(--text-main)' }}>Estado</th>
                  <th style={{ padding: '1rem', fontWeight: 700, color: 'var(--text-main)' }}>Propósito en la Arquitectura</th>
                </tr>
              </thead>
              <tbody>
                {catalogoComponentes.map((c, i) => (
                  <tr
                    key={i}
                    style={{
                      borderBottom: '1px solid var(--border-subtle)',
                      backgroundColor: i % 2 === 0 ? 'transparent' : 'var(--bg-surface-muted)'
                    }}
                  >
                    <td style={{ padding: '0.85rem 1rem', fontWeight: 700, color: 'var(--peach-primary)' }}>
                      <code>&lt;{c.nombre.replace('.jsx', '')} /&gt;</code>
                    </td>
                    <td style={{ padding: '0.85rem 1rem', color: 'var(--text-muted)' }}>
                      {c.categoria}
                    </td>
                    <td style={{ padding: '0.85rem 1rem' }}>
                      <span
                        style={{
                          backgroundColor: 'var(--mint-light)',
                          color: '#065F46',
                          padding: '3px 8px',
                          borderRadius: '10px',
                          fontSize: '0.78rem',
                          fontWeight: 700
                        }}
                      >
                        {c.estado}
                      </span>
                    </td>
                    <td style={{ padding: '0.85rem 1rem', color: 'var(--text-main)' }}>
                      {c.proposito}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};
