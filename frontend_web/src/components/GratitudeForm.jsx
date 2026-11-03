import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useMood } from '../context/MoodContext';
import { useAuth } from '../context/AuthContext';
import { MoodSelector } from './MoodSelector';
import { Heart, Sparkles, Calendar, User, Moon, Zap, Tag, Save, CheckCircle2 } from 'lucide-react';
import confetti from 'canvas-confetti';

/**
 * COMPONENTE: GratitudeForm
 * Formulario completamente controlado por estado local (Semana 9 de React).
 * Maneja tanto la creación de nuevas notas como la edición de existentes.
 */
export const GratitudeForm = ({ initialData = null, isEditing = false }) => {
  const { addEntry, updateEntry } = useMood();
  const { user } = useAuth();
  const navigate = useNavigate();

  // Estados controlados para cada campo del formulario
  const [fecha, setFecha] = useState(new Date().toISOString().split('T')[0]);
  const [usuario, setUsuario] = useState(user?.nombre || 'Carolina Morales');
  const [nivelAnimo, setNivelAnimo] = useState(5);
  const [emocion, setEmocion] = useState('Radiante');
  const [categoria, setCategoria] = useState('Bienestar');
  const [motivoGratitud, setMotivoGratitud] = useState('');
  const [horasSueno, setHorasSueno] = useState(8.0);
  const [energiaPct, setEnergiaPct] = useState(90);

  // Estados de validación y feedback
  const [error, setError] = useState('');
  const [exito, setExito] = useState(false);

  // Cargar datos iniciales en caso de edición
  useEffect(() => {
    if (initialData) {
      setFecha(initialData.fecha || new Date().toISOString().split('T')[0]);
      setUsuario(initialData.usuario || user?.nombre || '');
      setNivelAnimo(Number(initialData.nivel_animo) || 4);
      setEmocion(initialData.emocion || 'Calmado');
      setCategoria(initialData.categoria || 'Bienestar');
      setMotivoGratitud(initialData.motivo_gratitud || '');
      setHorasSueno(Number(initialData.horas_sueno) || 7.5);
      setEnergiaPct(Number(initialData.energia_pct) || 85);
    }
  }, [initialData, user]);

  const handleSelectMood = (nivel, nombreEmocion) => {
    setNivelAnimo(nivel);
    setEmocion(nombreEmocion);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validaciones
    if (!motivoGratitud.trim() || motivoGratitud.trim().length < 6) {
      setError('Por favor escribe al menos 6 caracteres describiendo por qué estás agradecido hoy.');
      return;
    }

    setError('');

    const payload = {
      fecha,
      usuario: usuario.trim(),
      nivel_animo: Number(nivelAnimo),
      emocion,
      categoria,
      motivo_gratitud: motivoGratitud.trim(),
      horas_sueno: Number(horasSueno),
      energia_pct: Number(energiaPct)
    };

    if (isEditing && initialData?.id) {
      updateEntry(initialData.id, payload);
    } else {
      addEntry(payload);
      // Animación de confeti de celebración
      try {
        confetti({
          particleCount: 80,
          spread: 60,
          origin: { y: 0.65 },
          colors: ['#FF9EAA', '#FCD34D', '#10B981', '#8B5CF6']
        });
      } catch (err) {
        console.log(err);
      }
    }

    setExito(true);
    setTimeout(() => {
      navigate('/diario');
    }, 1200);
  };

  return (
    <form onSubmit={handleSubmit} className="card" style={{ maxWidth: '780px', margin: '0 auto', padding: '2rem 2.25rem' }}>
      {/* Alerta de éxito o error */}
      {error && (
        <div
          style={{
            backgroundColor: 'var(--coral-light)',
            color: 'var(--coral-primary)',
            padding: '0.85rem 1rem',
            borderRadius: 'var(--radius-md)',
            marginBottom: '1.25rem',
            fontSize: '0.88rem',
            fontWeight: 600,
            border: '1px solid rgba(244, 63, 94, 0.3)'
          }}
        >
          ⚠️ {error}
        </div>
      )}

      {exito && (
        <div
          style={{
            backgroundColor: 'var(--mint-light)',
            color: '#065F46',
            padding: '0.85rem 1rem',
            borderRadius: 'var(--radius-md)',
            marginBottom: '1.25rem',
            fontSize: '0.9rem',
            fontWeight: 600,
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            border: '1px solid rgba(16, 185, 129, 0.3)'
          }}
        >
          <CheckCircle2 size={18} />
          <span>¡Registro {isEditing ? 'actualizado' : 'guardado'} con éxito! Redirigiendo a tu diario...</span>
        </div>
      )}

      {/* Grid de Fecha y Usuario */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1.25rem' }}>
        <div className="form-group">
          <label className="form-label">
            <Calendar size={16} color="var(--peach-primary)" />
            <span>Fecha del Registro:</span>
          </label>
          <input
            type="date"
            className="form-input"
            value={fecha}
            onChange={(e) => setFecha(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label className="form-label">
            <User size={16} color="var(--peach-primary)" />
            <span>Tu Nombre / Usuario:</span>
          </label>
          <input
            type="text"
            className="form-input"
            placeholder="Ej: Carolina Morales"
            value={usuario}
            onChange={(e) => setUsuario(e.target.value)}
            required
          />
        </div>
      </div>

      {/* Selector de Estado de Ánimo Ilustrado */}
      <MoodSelector selectedMood={nivelAnimo} onSelectMood={handleSelectMood} />

      {/* Motivo de Gratitud */}
      <div className="form-group">
        <label className="form-label">
          <Heart size={16} color="var(--coral-primary)" fill="var(--coral-primary)" />
          <span>¿Por qué estás agradecido(a) hoy? (El corazón de tu diario):</span>
        </label>
        <textarea
          className="form-textarea"
          rows={4}
          placeholder="Escribe al menos una cosa positiva del día: un detalle de un amigo, haber terminado un trabajo, una comida rica, el canto de las aves..."
          value={motivoGratitud}
          onChange={(e) => setMotivoGratitud(e.target.value)}
          required
        />
        <div style={{ display: 'flex', justifyContent: 'flex-end', fontSize: '0.75rem', color: 'var(--text-subtle)', marginTop: '0.2rem' }}>
          {motivoGratitud.length} caracteres
        </div>
      </div>

      {/* Categoría y Horas de Sueño */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.25rem' }}>
        <div className="form-group">
          <label className="form-label">
            <Tag size={16} color="var(--peach-primary)" />
            <span>Categoría:</span>
          </label>
          <select
            className="form-select"
            value={categoria}
            onChange={(e) => setCategoria(e.target.value)}
          >
            <option value="Bienestar">Bienestar & Salud</option>
            <option value="Crecimiento Personal">Crecimiento Personal</option>
            <option value="Estudio">Estudio / Académico</option>
            <option value="Trabajo">Trabajo / Proyectos</option>
            <option value="Familia">Familia & Hogar</option>
            <option value="Amistad">Amistad & Relaciones</option>
            <option value="Naturaleza">Naturaleza & Clima</option>
            <option value="Creatividad">Creatividad & Hobbies</option>
          </select>
        </div>

        <div className="form-group">
          <label className="form-label">
            <Moon size={16} color="#8B5CF6" />
            <span>Horas de Sueño Anoche:</span>
          </label>
          <input
            type="number"
            step="0.5"
            min="1"
            max="16"
            className="form-input"
            value={horasSueno}
            onChange={(e) => setHorasSueno(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label className="form-label">
            <Zap size={16} color="#F59E0B" />
            <span>Nivel de Energía: {energiaPct}%</span>
          </label>
          <input
            type="range"
            min="10"
            max="100"
            step="5"
            value={energiaPct}
            onChange={(e) => setEnergiaPct(e.target.value)}
            style={{ accentColor: 'var(--peach-primary)', marginTop: '0.5rem', cursor: 'pointer' }}
          />
        </div>
      </div>

      {/* Botón de Enviar */}
      <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '1rem', marginTop: '1.5rem', borderTop: '1px solid var(--border-subtle)', paddingTop: '1.5rem' }}>
        <button
          type="button"
          onClick={() => navigate('/diario')}
          className="btn-secondary"
        >
          Cancelar
        </button>

        <button type="submit" className="btn-primary">
          <Save size={18} />
          <span>{isEditing ? 'Guardar Cambios' : 'Registrar en Mi Diario ✨'}</span>
        </button>
      </div>
    </form>
  );
};
