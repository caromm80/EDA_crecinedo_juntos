import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { User, Mail, Sparkles, ArrowRight } from 'lucide-react';

export const LoginView = () => {
  const { login } = useAuth();
  const navigate = useNavigate();

  const [nombre, setNombre] = useState('Carolina Morales');
  const [email, setEmail] = useState('carolina@cesde.edu.co');

  const handleSubmit = (e) => {
    e.preventDefault();
    login(nombre, email);
    navigate('/dashboard');
  };

  return (
    <div>
      <div style={{ textAlign: 'center', marginBottom: '1.75rem' }}>
        <h2 style={{ fontSize: '1.5rem', color: 'var(--text-main)', marginBottom: '0.4rem' }}>
          ¡Bienvenido(a) a Lumi!
        </h2>
        <p style={{ fontSize: '0.88rem', color: 'var(--text-muted)' }}>
          Ingresa tus datos para personalizar tu diario de gratitud y estado de ánimo
        </p>
      </div>

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="form-label">
            <User size={16} color="var(--peach-primary)" />
            <span>Tu Nombre Completo:</span>
          </label>
          <input
            type="text"
            className="form-input"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            placeholder="Ej: Carolina Morales"
            required
          />
        </div>

        <div className="form-group">
          <label className="form-label">
            <Mail size={16} color="var(--peach-primary)" />
            <span>Correo Electrónico:</span>
          </label>
          <input
            type="email"
            className="form-input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="ejemplo@cesde.edu.co"
            required
          />
        </div>

        <button
          type="submit"
          className="btn-primary"
          style={{ width: '100%', justifyContent: 'center', marginTop: '1.25rem', padding: '0.85rem' }}
        >
          <span>Comenzar mi viaje con Lumi</span>
          <ArrowRight size={18} />
        </button>
      </form>
    </div>
  );
};
