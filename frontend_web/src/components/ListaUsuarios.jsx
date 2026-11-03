import React, { useState } from 'react';
import { Users, Search, Award, MapPin, Calendar, Heart, Sparkles } from 'lucide-react';
import { LumiMonster } from './LumiMonster';

/**
 * COMPONENTE REQUERIDO: <ListaUsuarios />
 * Contiene AL MENOS 20 usuarios quemados en código y renderiza cada uno de ellos.
 * Cumple con la especificación exacta de la Semana 4-5 de React y Momento 1 Web.
 */
export const ListaUsuarios = () => {
  const [busqueda, setBusqueda] = useState('');
  const [filtroOcupacion, setFiltroOcupacion] = useState('todos');

  // Arreglo de 24 usuarios quemados en código con datos enriquecidos
  const usuariosQuemados = [
    { id: 1, nombre: 'Carolina Morales', ciudad: 'Medellín', ocupacion: 'Estudiante', rachaDias: 18, animoProm: 4.8, gratitudFavorita: 'La perseverancia en mis estudios y el apoyo de mi familia.', moodFav: 5 },
    { id: 2, nombre: 'Mateo Restrepo', ciudad: 'Envigado', ocupacion: 'Desarrollador', rachaDias: 14, animoProm: 4.5, gratitudFavorita: 'Un buen café caliente y solucionar errores de código.', moodFav: 4 },
    { id: 3, nombre: 'Valentina Gómez', ciudad: 'Bogotá', ocupacion: 'Estudiante', rachaDias: 12, animoProm: 3.9, gratitudFavorita: 'La tranquilidad de una tarde de lectura con lluvia.', moodFav: 3 },
    { id: 4, nombre: 'Andrés Felipe Gómez', ciudad: 'Cali', ocupacion: 'Independiente', rachaDias: 9, animoProm: 4.1, gratitudFavorita: 'Salir en bicicleta y sentir el viento fresco.', moodFav: 4 },
    { id: 5, nombre: 'Sofía Ramírez', ciudad: 'Medellín', ocupacion: 'Docente', rachaDias: 21, animoProm: 4.9, gratitudFavorita: 'Ver a mis estudiantes comprender nuevos temas con emoción.', moodFav: 5 },
    { id: 6, nombre: 'Santiago López', ciudad: 'Manizales', ocupacion: 'Investigador', rachaDias: 15, animoProm: 4.2, gratitudFavorita: 'Los descubrimientos en el laboratorio y la música clásica.', moodFav: 4 },
    { id: 7, nombre: 'Camila Torres', ciudad: 'Bucaramanga', ocupacion: 'Profesional', rachaDias: 7, animoProm: 3.7, gratitudFavorita: 'Compartir la cena con mis padres sin prisa.', moodFav: 3 },
    { id: 8, nombre: 'Daniel Castro', ciudad: 'Pereira', ocupacion: 'Estudiante', rachaDias: 16, animoProm: 4.6, gratitudFavorita: 'Los proyectos de software completados con mis compañeros.', moodFav: 5 },
    { id: 9, nombre: 'Mariana Vargas', ciudad: 'Cartagena', ocupacion: 'Emprendedor', rachaDias: 11, animoProm: 4.3, gratitudFavorita: 'La brisa del mar y clientes felices con mi trabajo.', moodFav: 4 },
    { id: 10, nombre: 'Sebastián Herrera', ciudad: 'Bogotá', ocupacion: 'Desarrollador', rachaDias: 8, animoProm: 3.8, gratitudFavorita: 'Las herramientas open source que facilitan la vida.', moodFav: 3 },
    { id: 11, nombre: 'Lucía Mendoza', ciudad: 'Medellín', ocupacion: 'Profesional', rachaDias: 25, animoProm: 5.0, gratitudFavorita: 'Estar en paz mental y gozar de plena salud.', moodFav: 5 },
    { id: 12, nombre: 'Alejandro Morales', ciudad: 'Cali', ocupacion: 'Independiente', rachaDias: 10, animoProm: 4.0, gratitudFavorita: 'La libertad de organizar mis horarios de forma consciente.', moodFav: 4 },
    { id: 13, nombre: 'Valeria Rojas', ciudad: 'Barranquilla', ocupacion: 'Estudiante', rachaDias: 13, animoProm: 4.7, gratitudFavorita: 'Superar el miedo escénico al exponer en clases.', moodFav: 5 },
    { id: 14, nombre: 'Nicolás Ospina', ciudad: 'Envigado', ocupacion: 'Investigador', rachaDias: 19, animoProm: 4.4, gratitudFavorita: 'Poder leer artículos científicos interesantes cada día.', moodFav: 4 },
    { id: 15, nombre: 'Paula Aguirre', ciudad: 'Medellín', ocupacion: 'Docente', rachaDias: 14, animoProm: 4.6, gratitudFavorita: 'La sonrisa sincera de mis hijos al llegar a casa.', moodFav: 5 },
    { id: 16, nombre: 'Felipe Salazar', ciudad: 'Bogotá', ocupacion: 'Estudiante', rachaDias: 6, animoProm: 3.5, gratitudFavorita: 'Descansar tras una semana pesada de exámenes parciales.', moodFav: 2 },
    { id: 17, nombre: 'Gabriela Duarte', ciudad: 'Pereira', ocupacion: 'Emprendedor', rachaDias: 20, animoProm: 4.8, gratitudFavorita: 'Ver nacer nuevos emprendimientos con impacto social.', moodFav: 5 },
    { id: 18, nombre: 'Esteban Cárdenas', ciudad: 'Manizales', ocupacion: 'Profesional', rachaDias: 12, animoProm: 4.2, gratitudFavorita: 'La paciencia aprendida a lo largo de los años.', moodFav: 4 },
    { id: 19, nombre: 'Isabella Cruz', ciudad: 'Cartagena', ocupacion: 'Estudiante', rachaDias: 17, animoProm: 4.7, gratitudFavorita: 'Nadar en el mar y recargar energía positiva.', moodFav: 5 },
    { id: 20, nombre: 'Julián Pineda', ciudad: 'Bucaramanga', ocupacion: 'Desarrollador', rachaDias: 11, animoProm: 4.1, gratitudFavorita: 'La colaboración generosa en comunidades de desarrollo.', moodFav: 4 },
    { id: 21, nombre: 'Laura Quintero', ciudad: 'Medellín', ocupacion: 'Profesional', rachaDias: 22, animoProm: 4.9, gratitudFavorita: 'Comenzar cada mañana agradeciendo por tres cosas pequeñas.', moodFav: 5 },
    { id: 22, nombre: 'Samuel Bedoya', ciudad: 'Envigado', ocupacion: 'Estudiante', rachaDias: 8, animoProm: 3.6, gratitudFavorita: 'Aprender de los errores en vez de frustrarme.', moodFav: 3 },
    { id: 23, nombre: 'Manuela Henao', ciudad: 'Bogotá', ocupacion: 'Independiente', rachaDias: 15, animoProm: 4.5, gratitudFavorita: 'Los clientes comprensivos y el trabajo bien hecho.', moodFav: 4 },
    { id: 24, nombre: 'David Marín', ciudad: 'Cali', ocupacion: 'Desarrollador', rachaDias: 13, animoProm: 4.3, gratitudFavorita: 'Un código limpio, modular y fácil de entender.', moodFav: 4 }
  ];

  // Filtrado reactivo en el estado local
  const usuariosFiltrados = usuariosQuemados.filter(u => {
    const coincideBusqueda =
      u.nombre.toLowerCase().includes(busqueda.toLowerCase()) ||
      u.ciudad.toLowerCase().includes(busqueda.toLowerCase()) ||
      u.gratitudFavorita.toLowerCase().includes(busqueda.toLowerCase());

    const coincideOcupacion =
      filtroOcupacion === 'todos' || u.ocupacion.toLowerCase() === filtroOcupacion.toLowerCase();

    return coincideBusqueda && coincideOcupacion;
  });

  return (
    <div>
      {/* Badge identificador del componente para evaluación docente */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem', marginBottom: '1.5rem' }}>
        <div className="page-signature-badge">
          <Users size={14} />
          <span>Componente: &lt;ListaUsuarios /&gt; (Total: {usuariosQuemados.length} usuarios quemados en código)</span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.84rem', color: 'var(--text-muted)' }}>
          <Award size={16} color="#F59E0B" />
          <span>Comunidad activa en el reto de gratitud 2026</span>
        </div>
      </div>

      {/* Barra de Filtros y Búsqueda */}
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
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', flex: '1 1 280px' }}>
          <Search size={18} color="var(--text-subtle)" />
          <input
            type="text"
            className="form-input"
            placeholder="Buscar por nombre, ciudad o motivo de gratitud..."
            value={busqueda}
            onChange={(e) => setBusqueda(e.target.value)}
            style={{ padding: '0.55rem 0.85rem' }}
          />
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-muted)' }}>
            Ocupación:
          </label>
          <select
            className="form-select"
            value={filtroOcupacion}
            onChange={(e) => setFiltroOcupacion(e.target.value)}
            style={{ padding: '0.55rem 0.85rem', width: 'auto' }}
          >
            <option value="todos">Todas las ocupaciones</option>
            <option value="Estudiante">Estudiante</option>
            <option value="Desarrollador">Desarrollador</option>
            <option value="Docente">Docente</option>
            <option value="Investigador">Investigador</option>
            <option value="Profesional">Profesional</option>
            <option value="Independiente">Independiente</option>
            <option value="Emprendedor">Emprendedor</option>
          </select>
        </div>
      </div>

      {/* Mensaje de resultados */}
      <p style={{ fontSize: '0.88rem', color: 'var(--text-muted)', marginBottom: '1.25rem' }}>
        Mostrando <strong>{usuariosFiltrados.length}</strong> de {usuariosQuemados.length} miembros registrados.
      </p>

      {/* Grilla de Usuarios */}
      <div className="grid-responsive-cards">
        {usuariosFiltrados.map((u) => (
          <div
            key={u.id}
            className="card"
            style={{
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'space-between',
              position: 'relative',
              overflow: 'hidden'
            }}
          >
            {/* Cabecera de la tarjeta con avatar de Lumi */}
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1rem' }}>
                <div style={{ pointerEvents: 'none' }}>
                  <LumiMonster mood={u.moodFav} size={58} showBubble={false} interactive={false} />
                </div>
                <div>
                  <h3 style={{ fontSize: '1.1rem', color: 'var(--text-main)', marginBottom: '0.15rem' }}>
                    {u.nombre}
                  </h3>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem', fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                    <MapPin size={13} color="var(--peach-primary)" />
                    <span>{u.ciudad}</span>
                    <span>•</span>
                    <span style={{ fontWeight: 600 }}>{u.ocupacion}</span>
                  </div>
                </div>
              </div>

              {/* Cita de gratitud favorita */}
              <div
                style={{
                  backgroundColor: 'var(--bg-surface-soft)',
                  borderLeft: '3px solid var(--peach-primary)',
                  padding: '0.75rem 0.85rem',
                  borderRadius: '0 8px 8px 0',
                  marginBottom: '1rem'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.7rem', color: 'var(--peach-primary)', fontWeight: 700, marginBottom: '0.2rem' }}>
                  <Heart size={12} fill="var(--peach-primary)" />
                  <span>Motivo de Gratitud</span>
                </div>
                <p style={{ fontSize: '0.83rem', fontStyle: 'italic', color: 'var(--text-main)', lineHeight: 1.4 }}>
                  "{u.gratitudFavorita}"
                </p>
              </div>
            </div>

            {/* Métricas del usuario (Racha y Ánimo Promedio) */}
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                borderTop: '1px solid var(--border-subtle)',
                paddingTop: '0.75rem',
                fontSize: '0.8rem'
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.3rem', color: '#F59E0B', fontWeight: 700 }}>
                <Sparkles size={14} />
                <span>Racha: {u.rachaDias} días</span>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '0.3rem', color: '#10B981', fontWeight: 700 }}>
                <span>Ánimo: {u.animoProm} / 5.0</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
