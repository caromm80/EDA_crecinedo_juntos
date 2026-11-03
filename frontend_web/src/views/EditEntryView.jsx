import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { useMood } from '../context/MoodContext';
import { GratitudeForm } from '../components/GratitudeForm';
import { ArrowLeft, AlertCircle } from 'lucide-react';

export const EditEntryView = () => {
  const { id } = useParams();
  const { getEntryById } = useMood();

  const entry = getEntryById(id);

  if (!entry) {
    return (
      <div className="card" style={{ maxWidth: '520px', margin: '2rem auto', textAlign: 'center', padding: '2.5rem' }}>
        <AlertCircle size={40} color="var(--coral-primary)" style={{ margin: '0 auto 1rem auto' }} />
        <h3 style={{ fontSize: '1.25rem', marginBottom: '0.5rem', color: 'var(--text-main)' }}>
          Entrada no encontrada
        </h3>
        <p style={{ fontSize: '0.88rem', color: 'var(--text-muted)', marginBottom: '1.5rem' }}>
          El registro con ID #{id} no existe o fue eliminado del almacenamiento local.
        </p>
        <Link to="/diario" className="btn-primary">
          <ArrowLeft size={16} />
          <span>Volver al Diario</span>
        </Link>
      </div>
    );
  }

  return (
    <div>
      <GratitudeForm initialData={entry} isEditing={true} />
    </div>
  );
};
